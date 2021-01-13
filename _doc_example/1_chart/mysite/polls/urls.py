# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
]
