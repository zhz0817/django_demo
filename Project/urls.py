# -*- coding: utf-8 -*-
"""djangoProject URL Configuration

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
from django.urls import path
from Project import views
from Project import tests
urlpatterns = [
    path('addStudent', views.addStudent),
    path('selectStudent', views.selectStudent),
    path('deleteStudent', views.deleteStudent),
    path('updateStudent', views.updateStudent),
    path('test1', tests.test1),
    path('test2', tests.test2),
]
