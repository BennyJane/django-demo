# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : tutorial
# Time       ：2020/12/27 11:54
# Warning    ：The Hard Way Is Easier
from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet
from snippets.models import LANGUAGE_CHOICES
from snippets.models import STYLE_CHOICES


# 实现数据转换： 数据模型类 =》 python内置类型 =》 json字符串
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # serializers 提供了字段验证方法
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={"base_template": "textarea.html"})  # 设置字段在某些情况下如何显示
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")
    # TODO 添加用户
    # ReadOnlyField: 只读属性，可用于展示，但不会映射到数据库中
    # 等效： CharField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight',
                                                        format='html')

    class Meta:
        model = Snippet
        fields = [
            "url", "id", "highlight", "owner", "title", "code",
            "linenos", "language", "style"
        ]

    def create(self, validated_data):
        """
        通过接收的数据，创建Snippet实例
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """通过接收的数据，更新或者返回Snippet数据"""
        instance.title = validated_data.get("title", instance.title)  # 获取title，设置默认值
        instance.code = validated_data.get("code", instance.code)
        instance.linenos = validated_data.get("linenos", instance.linenos)
        instance.language = validated_data.get("language", instance.language)
        instance.style = validated_data.get("style", instance.style)

        instance.save()
        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets时关联在User上的，实际数据表中并没有该字段
    # 在使用ModelSerializer时，需要显示添加该字段
    snippets = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name="snippet-detail",
                                                   read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
