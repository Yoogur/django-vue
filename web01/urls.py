"""web01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path

from server import index
from server.post.view import *
from server.user.view import *

urlpatterns = [
    path('', index.IndexPrint),

    path("user/register", user_register),
    path('user/login', user_login),
    path('user/modify', user_modify),
    path('user/getByUsername', user_get),

    path('post/publish', post_publish),
    path('post/delete', post_del),
    path('post/getByTitle', get_by_title),
    path('post/showall', show_posts)
]
