from rest_framework import generics
from rest_framework import renderers
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from snippets.permissons import IsOwnerOrReadOnly
from snippets.models import Snippet
from snippets.serializers_on_model import SnippetSerializer as final_SnippetSerializer
from snippets.serializers_on_model import UserSerializer as final_UserSerializer
from django.contrib.auth.models import User


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetHighlight(generics.GenericAPIView):
    model = Snippet
    renderer_classes = (renderers.StaticHTMLRenderer,)
    queryset = Snippet.objects.all()

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = final_SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    """
    请注意，我们还使用了@action装饰器来创建名为的自定义操作highlight。这个装饰可以用来添加不符合标准的任何自定义端点create/ update/delete风格。
    默认情况下，使用@action装饰器的自定义操作将响应GET请求。methods如果需要响应POST请求的操作，则可以使用参数。
    默认情况下，自定义操作的URL取决于方法名称本身。如果要更改url的构造方式，可以将其url_path作为装饰关键字参数。
    """

    @action(detail=True, render_class=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = final_UserSerializer
