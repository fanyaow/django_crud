#!/usr/bin/env python
# encoding: utf-8
'''
@author: fyw
@file: send_mail_test.py
@time: 19-9-10 上午9:35
@desc:study devops
'''

import os
from django.core.mail import EmailMultiAlternatives
from django.core.mail.backends import smtp

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_crud.settings'


if __name__ == '__main__':

    subject, from_email, to = '来自fyw的测试邮件', 'yaowen_2019@sina.com', 'yaowen_2013@qq.com'
    text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()