"""game_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

##add model
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('captcha/', include('captcha.urls'))
]

## add urlpatterns
#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#    url(r'^index/', views.index),
#    url(r'^login/', views.login),
#    url(r'^register/', views.register),
#    url(r'^logout/', views.logout),
#    url(r'^captcha', include('captcha.urls'))  # 验证码
#]




