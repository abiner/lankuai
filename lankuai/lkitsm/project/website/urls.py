from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.urls import re_path

urlpatterns = [
    # url(r'^accounts/login/', django.contrib.auth.views.login),


    #处理工作流mhrworkfolw
    url(r'^(\d{14})/$', views.mdispose),
    url(r'addmdispose$', views.addmdispose),



    # 工单系统
    url(r'^writeWorkList$', views.writeWorkList),


    # writeWorkList提交过来的数据,写入数据库操作
    url('addWriteWorkList', views.addWriteWorkList),

    # 我创办的 Iestablishdelay
    url(r'^Iestablish/(\d+)$', views.Iestablishpage),

    #我创办的，继续处理
    url(r'^Iestablish/[a-z0-9]{11,14}', views.goon),



    # 我的待办
    url(r'^delay/(\d+)$', views.delaypage),

    #继续处理
    url(r'^delay/[a-z0-9]{11,14}', views.goon),
    #在继续处理
    url(r'^addProcess' ,views.addProcess),

    # 查看所有工单,兼职分页
    url(r'^allWorkOrder/(\d+)$', views.allpage),
    #继续处理
    url(r'^allWorkOrder/[a-z0-9]{11,14}', views.goon),

    #url(r'^allW/(\d+)$', views.allpage),

    url(r'^main.html', views.main),
    url(r'^nav.htm', views.nav),
    #url(r'^form', views.form),
    #url(r'^index$', views.index),
    url(r'^table', views.table),
    # url(r'^/test', views.test3),
    url('hrms$', views.hrms),
    #url('hrworkfolw$', views.hrwfolw),
    url('test', views.test),
    #url('form', views.form),

    # url('newhelpdeskitem', views.ithelpdesk),


]
