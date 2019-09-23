# django_crud
![Total visitor](https://visitor-count-badge.herokuapp.com/total.svg?repo_id=jumpserver)
![Visitors in today](https://visitor-count-badge.herokuapp.com/today.svg?repo_id=jumpserver)
[![Python3](https://img.shields.io/badge/python-3.7-green.svg?style=plastic)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-2.2-brightgreen.svg?style=plastic)](https://www.djangoproject.com/)

## 项目介绍

python3.7.1，django2.2.5,实现注册，登陆，填加，删除，修改，查询等基础功能。新手必学技能。

## 项目安装

```
$ git clone https://github.com/fanyaow/django_crud.git
$ cd django_crud
$ pip install -r requirements.txt
```
### 数据库配置
新建mysql数据库django_curdb,配置django_curdb目录下的setting.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_crud',
        'USER': 'root',
        'PASSWORD': 'abc123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", 'charset': 'utf8', },
    }
}
```
### 在pycharm的terminal窗口执行
python manage.py makemigrations
python manage.py migrate
### 启动服务
python manage.py runserver 
如果指定端口执行
python manage.py runserver 127.0.0.1:8000

### 浏览器访问：
http://127.0.0.1:8000
## 项目截图
![index](https://github.com/fanyaow/django_crud/tree/master/static/temp/1.png
