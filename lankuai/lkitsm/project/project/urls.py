"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
import xadmin

urlpatterns = [
    # 系统自带后台 admin
    #path('admin/', admin.site.urls),

    # 使用xadmin后台
    path('admin/' ,xadmin.site.urls),

    #login
    path(r'', include('login.urls')),
    #工单系统
    path(r'', include('website.urls')),
    #蓝快课堂
    path(r'media/', include('avi.urls')),

    #人事管理 之工作流1
    path(r'hrworkfolw/', include('workfolw.urls')),
    #人事管理 之工作流2
    path(r'mrworkfolw/', include('workfolw.urls')),
    #人事管理 之公告管理
    path(r'', include('workfolw.urls')),

    #商务管理
    path(r'business/', include('business.urls')),

    #维修 ，采购 repairANDbuyer
    path(r'repairANDbuyer/', include('repairANDbuyer.urls')),

    #path('', include('workflow-master.urls')),
]


