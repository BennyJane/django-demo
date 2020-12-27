# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : tutorial
# Time       ：2020/12/27 12:33
# Warning    ：The Hard Way Is Easier
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

"""
因为我们使用的是ViewSet类而不是View类，所以实际上我们不需要自己设计URL conf。
使用Router类可以自动处理将资源连接到视图和url的约定。我们需要做的就是向路由器注册适当的视图集，
然后让其余的工作完成。


向路由器注册视图集类似于提供urlpattern。我们包含两个参数-视图的URL前缀和视图集本身。
DefaultRouter我们正在使用的类还会自动为我们创建API根视图，
因此我们现在可以api_root从views模块中删除方法。
"""

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
