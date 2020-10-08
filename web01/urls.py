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
from server.post.view import add_post
from server.user.view import *

urlpatterns = [
    path('', index.IndexPrint),
    path("register/userReg", user_register),
    path('login/userLogin', user_login),
    path('modify/userModify', user_modify),
    path('get/userGet', user_get),
    url(r'add_post$', add_post, ),

]
