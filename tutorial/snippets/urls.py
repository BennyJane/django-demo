# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : tutorial
# Time       ：2020/12/27 12:33
# Warning    ：The Hard Way Is Easier
from django.urls import path
from snippets import views

# 版本1.0： django原生写法
urlpatterns1 = [
    path('snippets1/', views.snippet_list),
    path('snippets1/<int:pk>', views.snippet_detail),
]

# 版本2.0 rest扩展使用视图函数
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_rest_func

urlpatterns2 = format_suffix_patterns([
    path('snippets2/', views_rest_func.snippet_list),
    path('snippets2/<int:pk>', views_rest_func.snippet_detail)
])

# 版本3.0 rest扩展使用视图类
from snippets import views_rest_class

urlpatterns3 = format_suffix_patterns([
    path('snippets3/', views_rest_class.SnippetList.as_view()),  # 调用类方法 as_view()
    path('snippets3/<int:pk>', views_rest_class.SnippetDetail.as_view())
])

# 版本4.0 使用扩展类：进一步减少代码重复率
from snippets import views_rest_mixins

urlpatterns4 = format_suffix_patterns([
    path('snippets4/', views_rest_mixins.SnippetList.as_view()),  # 调用类方法 as_view()
    path('snippets4/<int:pk>', views_rest_mixins.SnippetDetail.as_view())
])

# 版本5.0 使用通用类：绝杀 + user 视图
from snippets import views_rest_comClass

urlpatterns5 = format_suffix_patterns([
    path('', views_rest_comClass.api_root),
    path('snippets/', views_rest_comClass.SnippetList.as_view(),
         name='snippet-list'),  # 调用类方法 as_view()
    path('snippets/<int:pk>', views_rest_comClass.SnippetDetail.as_view(),
         name='snippet-detail'),
    path("users/", views_rest_comClass.UserList.as_view(),
         name='user-list'),
    path("users/<int:pk>", views_rest_comClass.UserInstance.as_view(),
         name='user-list'),
    path("snippets/<int:pk>/highlight", views_rest_comClass.SnippetHighlight.as_view(),
         name='snippet-list')
])

# 版本final
from snippets import views_rest_final

urlpatterns6 = format_suffix_patterns([
    path('', views_rest_final.api_root),
    path('snippets/', views_rest_final.SnippetList.as_view(),
         name='snippet-list'),  # 调用类方法 as_view()
    path('snippets/<int:pk>', views_rest_final.SnippetDetail.as_view(),
         name='snippet-detail'),
    path("users/", views_rest_final.UserList.as_view(),
         name='user-list'),
    path("users/<int:pk>", views_rest_final.UserInstance.as_view(),
         name='user-detail'),
    path("snippets/<int:pk>/highlight", views_rest_final.SnippetHighlight.as_view(),
         name='snippet-highlight')
])

# 源码： 从该模块中读取 urlpatterns 变量
# urlpatterns = urlpatterns1 + urlpatterns2 + urlpatterns3 + urlpatterns4 + urlpatterns5
# urlpatterns = urlpatterns5
urlpatterns = urlpatterns6
