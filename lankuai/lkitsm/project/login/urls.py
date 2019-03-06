from django.conf.urls import url
from django.contrib import admin
from login import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^login/$', views.login),
    # 注销
    url(r'^logout$', views.logout),

    # 注册
    url(r'^register/$', views.register),

    # 新增用户 adduser
    url(r'^adduser$', views.adduser),

    # 管理用户页面 logout
    url(r'^logoutuser/(\d+)$', views.logoutuser),

    # 重置密码操作 resetpsswd/工单号
    url(r'^resetpsswd/(\d{8})/$', views.resetpsswd),

    # 注销页面操作 subtractuser/工单号
    url(r'^logoutuser/(\d{8})/$', views.subtractuser),



]


