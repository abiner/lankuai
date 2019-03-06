
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import re_path
from project import settings
urlpatterns = [

    # 商务管理
    url('^$', views.busines),
    # addbusiness提交过来的数据,写入数据库操作
    url('addbusiness', views.addbusiness),

    #所有合同
    url('^alcontract/(\d+)$' ,views.allcontract),

    #我的合同
    url('^mycontract/(\d+)$' ,views.mycontract),

    #合同详情
    url('^([a-zA-Z0-9]*)$' ,views.contractdetails),

    url(r'^media/(?P<path>.*)/$', serve, {'document_root': settings.MEDIA_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''

    # 查看所有工单,兼职分页
    url(r'^allWorkOrder/(\d+)$', views.allpage),
'''



