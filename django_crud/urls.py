from django.contrib import admin
from django.urls import path, re_path, include

# 注意要引入 url
from django.conf.urls import url
# 注意要引入自己的 views
from django.views.static import serve

from django_crud.settings import MEDIA_ROOT
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),# captcha
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # path('login/', views.login),   # 前往所有学生的网页
    path('addPage/', views.add_page),     # 前往新增学生的网页
    path('addStudent/', views.add_student),   # 添加学生的 dao 操作
    path('search/', views.search_student),   # 根据 t_name 查找学生的 dao 操作
    path('get/<int:student_id>/', views.search_student_id),   # 根据 id 查找学生的 dao 操作
    path('updateStudent/', views.update_student),   # 修改学生的 dao 操作
    path('delete/<int:student_id>/', views.delete_student),   # 删除学生的 dao 操作

    #index login register logout
    path('index/', views.index),
    path('', views.index),
    path('login/', views.login,name='login'),
    path('register/', views.register),
    path('logout/', views.logout),
]
