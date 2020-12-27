from rest_framework import generics
from rest_framework import renderers
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from snippets.permissons import IsOwnerOrReadOnly
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer
from django.contrib.auth.models import User


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


# 使用混入类，进一步提高代码复用率
# 逻辑： 继承generics.GenericAPIView基类，提供了核心功能；添加扩展类 mixins，提供 .list .create等方法
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # 添加权限： 非登录只允许阅读，登录则可以修改任何人的数据；
    # IsOwnerOrReadOnly; 只能修改个人的数据
    # 登录用户都允许新增数据
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # TODO 实现添加数据时，绑定用户
    # WHY： 因为用户信息并在request.data内，但可以通过request.user获取
    # 重写视图函数类的 .perform_create方法，修改.save的作用，可以处理request内的任意信息
    # 重写后， create() 方法将会获取额外的字段 `owner`
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


"""
class SnippetList(generics.ListCreateAPIView):
    model = Snippet
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user
"""


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class SnippetHighlight(generics.GenericAPIView):
    model = Snippet
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer

    queryset = User.objects.all()


class UserInstance(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

    queryset = User.objects.all()
