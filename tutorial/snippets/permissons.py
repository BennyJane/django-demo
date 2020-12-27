# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : tutorial
# Time       ：2020/12/27 20:43
# Warning    ：The Hard Way Is Easier
from rest_framework import permissions


# todo 自定义权限类

class IsOwnerOrReadOnly(permissions.BasePermission):
    """只允许所有者编辑，其他登录者可以查看"""

    def has_object_permission(self, request, view, obj):
        # permissions.SAFE_METHODS: get options head
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
