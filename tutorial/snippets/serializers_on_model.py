# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : tutorial
# Time       ：2020/12/27 11:54
# Warning    ：The Hard Way Is Easier
from rest_framework import serializers
from snippets.models import Snippet
from snippets.models import LANGUAGE_CHOICES
from snippets.models import STYLE_CHOICES


"""
ModelSerializer类只是创建序列化器类的捷径：
1. 自动确定的一组字段。
2. create()和update()方法的简单默认实现。
"""

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style"]
