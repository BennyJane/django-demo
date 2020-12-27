# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : tutorial
# Time       ：2020/12/27 12:33
# Warning    ：The Hard Way Is Easier
from django.urls import path
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views_rest_viewSet

snippet_list = views_rest_viewSet.SnippetViewSet.as_view({
    "get": "list",
    "post": "create",
})

snippet_detail = views_rest_viewSet.SnippetViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})
snippet_highlight = views_rest_viewSet.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = views_rest_viewSet.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views_rest_viewSet.UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', views_rest_viewSet.api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
