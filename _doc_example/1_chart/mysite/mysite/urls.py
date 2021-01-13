"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 真实可访问路由： /polls/
    path('polls/', include('polls.urls')),  # 批量引入其他应用中的路由
]


"""
path(route, view, kwargs=None, name=None, Pattern=None)
- route: 匹配URL的准则（类似正则表达式），响应请求时，会从 urlpatterns的第一项开始，按顺序一次匹配列表中的像，直到找到匹配的项
- view: 路由对应的视图函数， 并传入HttpRequest对象作为第一个参数，被捕获的参数以关键字参数的形式传入
- kwargs: 任意个关键字参数，可以作为字典传递给目标视图函数
- name: 为URL取别名，方便再django的任意地方调用它，尤其时模板中： 该特性允许只修改一个文件就可以全局的修改某个URL的模式

"""