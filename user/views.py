from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from django.forms import forms
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings    # 获取 settings.py 里边配置的信息
import os

from user import check_login
from user.models import student_info,User
from . import models
from . import forms

# 1.1.前往 index 页（all）

# index
def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    data = student_info.objects.all()
    content = {'data': data}
    return render(request, 'index.html',content)

#  login

def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            print('你输入的账号和密码为：',username,':',password)

            try:
                user = User.objects.get(name=username)

            except:
                message = '用户不存在！'

                return render(request, 'login.html', locals())
            print('数据库中的用户和密码为：' ,'****', user.name, ':', user.password)
            if check_password(password,user.password):    # 不能这样设置user.password == make_password(password):
                request.session['is_login']=True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login.html', locals())
        else:
            return render(request, 'login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login.html', locals())


# register

def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            print(username,password1,password2,email,sex)
            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'register.html', locals())
                print(same_name_user)
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'register.html', locals())
                print(same_email_user)
                new_user = models.User()
                new_user.name = username
                new_user.password = make_password(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")
# 1.2.前往 add 页
@check_login.login
def add_page( request ):
    return render(request, 'student/add.html')

# 2.增
@check_login.login
def add_student(request):
    t_name = request.POST['tName']
    t_age = request.POST['tAge']
    t_pwd = request.POST['tPwd']
    t_image = request.FILES['tImage']
    fname = os.path.join(settings.MEDIA_ROOT, t_image.name)
    with open(fname, 'wb') as pic:
        for c in t_image.chunks():
            pic.write(c)

    student=student_info()
    student.t_name=t_name
    student.t_age=t_age
    student.t_pwd=t_pwd
    # 存访问路径到数据库
    student.t_image = os.path.join("/media/", t_image.name)
    student.save()

    return redirect('/index')

# 3.1.查 - name
def search_student(request):
    t_name = request.GET['search']
    student=student_info.objects.filter(t_name=t_name)
    content={'data':student}
    return render(request,'student/all.html', content)

# 3.2.查 - id
def search_student_id(request,student_id):
    student=student_info.objects.filter(id=student_id)
    content = {'data': student}
    print(content)
    return  render(request,'student/update.html',content)

# 4.改
@check_login.login
def update_student(request):

    id=request.POST['t_id']
    t_name = request.POST['tName']
    t_age = request.POST['tAge']
    # 缺陷：文件必传
    t_image = request.FILES['tImage']

    fname = os.path.join(settings.MEDIA_ROOT, t_image.name)
    with open(fname, 'wb') as pic:
        for c in t_image.chunks():
            pic.write(c)
    t_image = os.path.join("/media/", t_image.name)

    student_info.objects.filter(id=id).update(t_name=t_name,t_age=t_age,t_image=t_image)
    return redirect('/index')

# 5.删
@check_login.login
def delete_student(request,student_id):
    student_info.objects.filter(id=student_id).delete()
    return redirect('/index')



