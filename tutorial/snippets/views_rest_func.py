from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


"""
rest扩展：
Request类对django中的 HttpRequest,进行了封装，新增数据性 request.data
Response类替换HttpResponse

装饰器：
api_view

为URI添加可选的格式后缀
让视图函数接收位置参数： format=None
"""


@api_view(["GET", "POST"])
def snippet_list(request, format=None):
    """
    列出所有snippet，或者创建一个snippet
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        # 数据库数据 =》 python数据类型
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)  # 转json类型
    if request.method == 'POST':
        # rest扩展，封装了新的Request类型
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):
    """检索、更新、删除"""
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=204)


