# django_crud
![Total visitor](https://visitor-count-badge.herokuapp.com/total.svg?repo_id=jumpserver)
![Visitors in today](https://visitor-count-badge.herokuapp.com/today.svg?repo_id=jumpserver)
[![Python3](https://img.shields.io/badge/python-3.7-green.svg?style=plastic)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-2.2-brightgreen.svg?style=plastic)](https://www.djangoproject.com/)

## ��Ŀ����

python3.7.1��django2.2.5,ʵ��ע�ᣬ��½����ӣ�ɾ�����޸ģ���ѯ�Ȼ������ܡ����ֱ�ѧ���ܡ�

## ��Ŀ��װ

```
$ git clone https://github.com/fanyaow/django_crud.git
$ cd django_crud
$ pip install -r requirements.txt
```
### ���ݿ�����
�½�mysql���ݿ�django_curdb,����django_curdbĿ¼�µ�setting.py
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
### ��pycharm��terminal����ִ��
```
 python manage.py makemigrations
 python manage.py migrate
 ```
### ��������
```
python manage.py runserver 
```
 ���ָ���˿�ִ��
 ```
 python manage.py runserver 127.0.0.1:8000
 ```

### ��������ʣ�
http://127.0.0.1:8000
## ��Ŀ��ͼ
### ��½ҳ��
![login](https://github.com/fanyaow/django_crud/blob/master/static/temp/1.png)
### ע��ҳ����󶼻�����Ӧ�Ĵ�����ʾ
![login](https://github.com/fanyaow/django_crud/blob/master/static/temp/1.png)
### ע��ҳ��
![register](https://github.com/fanyaow/django_crud/blob/master/static/temp/2.png)
### ��½����ҳ
![index](https://github.com/fanyaow/django_crud/blob/master/static/temp/3.png)
### ����ѧ��ҳ�棬ע��ͼƬ����Ҫ�ϴ���û�������жϣ������ύ�ᱨ��
![add](https://github.com/fanyaow/django_crud/blob/master/static/temp/4.png)
### �޸�ҳ��
![update](https://github.com/fanyaow/django_crud/blob/master/static/temp/5.png)
### ��ѯҳ��
#### ��ѯǰ
![query](https://github.com/fanyaow/django_crud/blob/master/static/temp/6.png)
#### ��ѯ��
![query](https://github.com/fanyaow/django_crud/blob/master/static/temp/7.png)
### ɾ����ֱ�ӻص���ҳ
![query](https://github.com/fanyaow/django_crud/blob/master/static/temp/8.png)

