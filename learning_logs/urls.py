#!/usr/bin/env python
#conding=utf-8
from django.conf.urls import url
from . import views

"""定义learning_logs的URL模式"""
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    
    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),
]
