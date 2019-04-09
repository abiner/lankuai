from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
# from project.settings import MEDIA_ROOT
from project import settings

urlpatterns = [
                  # 维修 repair
                  url(r'^repair$', views.repair),

                  # 新增维修单 addrepair
                  url(r'^addrepair$', views.addrepair),

                  # 新增成本价表单 addCostPrice
                  url(r'^addCostPrice$', views.addCostPrice),

                  # 维修，不同角色不同显示及提交
                  url(r'^(\d{15})$', views.verif),

                  # 增加 报价表
                  url(r'^addquote$', views.addquote),

                  # mycontract/1，发起人查看进程
                  url(r'^myrepair/(\d+)$', views.myrepair),

                  # mycontract/xxxxxxxxxxxxxxx，发起人查看某条具体进程
                  url(r'^myrepair/(\d{14})/$', views.onerepair),

                  # 采购 buyer
                  url(r'^buyer$', views.buyer),

                  # 新增采购 addpurchase
                  url(r'^addpurchase$', views.addpurchase),

                  # 采购，采购部唐涛提交成本价
                  url(r'^(\d{10})$', views.costprice),

                  # 采购 ，增加成本表 addgoodscost
                  url(r'^addgoodscost$', views.addgoodscost),

                  # 部门经理同意 addmanageryes
                  url(r'^addmanageryes$', views.addmanageryes),

                  # 发起人确认收货
                  url(r'^addconsignee$', views.addconsignee),

                  # 发起人查看进程
                  url(r'^mypurchase/(\d+)$', views.mypurchase),

                  # 发起人查看具体某条进程 mypurchase
                  url(r'^mypurchase/(\d{9})/$', views.onepurchase),

                  # 主页，更多 more
                  url(r'^addrepairok/$', views.addrepairok),

                  # addCostPriceok
                  url(r'^addCostPriceok/$', views.addCostPriceok),

                  # repairANDbuyer/addpurchaseok/
                  url(r'^repairANDbuyer/addpurchaseok/$', views.addpurchaseok),

                  url(r'^media/(?P<path>.*)/$', serve, {'document_root': settings.MEDIA_ROOT}),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
