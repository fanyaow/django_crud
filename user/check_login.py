#!/usr/bin/env python
# encoding: utf-8
'''
@author: fyw
@file: check_login.py
@time: 19-9-10 上午11:12
@desc:study devops
'''

from functools import wraps
# 说明：这个装饰器的作用，就是在每个视图函数被调用时，都验证下有没法有登录，
# 如果有过登录，则可以执行新的视图函数，
# 否则没有登录则自动跳转到登录页面。
from django.http import HttpResponseRedirect
from django.shortcuts import reverse


# 如果未登录则转到登陆页面

def login(func):
    def login_fun(request, *args, **kwargs):
        if 'is_login' in request.session:
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect(reverse("login"))
            red.set_cookie('url', request.get_full_path())
            # 保证用户再登陆验证之后仍点击到希望的页面
            return red
    return login_fun

"""
http://127.0.0.1:8000/200/?type=10
request.path :表示当前路径，为/200/
request.get_full_path():表示完整路径，为/200/?type=10
"""
