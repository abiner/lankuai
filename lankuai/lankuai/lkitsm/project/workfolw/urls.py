from django.urls import re_path
from . import views
from django.views.static import serve
from project import settings
from django.conf.urls.static import static

urlpatterns = [

                  re_path(r'^$', views.workfolw),
                  # 增加工作流
                  re_path(r'^addworkfolw$', views.addworkfolw),

                  # 我的工作流
                  re_path(r'^myfolw/(\d+)$', views.myfolw),

                  # 我审批过的工作流
                  re_path(r'^IAppro/(\d+)$', views.IAppro),

                  # 我具体的某条工作流
                  re_path(r'^myfolw/(\d{14})/$', views.onefolw),

                  # 我审批过的具体的某条工作流
                  re_path(r'^IAppro/(\d{14})/', views.onefolw),

                  # 公告
                  re_path(r'^notice$', views.notice),

                  # 公告 增加公告 addnotice
                  re_path(r'^addnotice$', views.addnotice),

                  # 公告 展示具体公告 inform
                  re_path(r'^(\d{13})$', views.inform),

                  # 公告 同意展示具体公告
                  re_path(r'^addyes$', views.addyes),

                  # 公告 我发布的公告
                  re_path(r'^mynotice/(\d+)$', views.mynotice),

                  # 公告 我发布的公告
                  re_path(r'^alnotice/(\d+)$', views.alnotice),

                  # 主页，更多 more
                  re_path(r'^addworkfolwok/$', views.addworkfolwok),

                  re_path(r'^media/(?P<path>.*)/$', serve, {'document_root': settings.MEDIA_ROOT}),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
