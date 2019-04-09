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
                  # 门必须得锁紧，课堂首页显示视频，有分页所以需要加上页码
                  url(r'^(\d+)$', views.media),

                  # 上传
                  url(r'^upload$', views.form),

                  # 某视频
                  url(r'^avi(\d+)$', views.avi),

                  url(r'^add(\d+)$', views.addIsee),

                      # 主页，更多 more
                  url(r'^addok$', views.addok),

                  url(r'^media/(?P<path>.*)/$', serve, {'document_root': settings.MEDIA_ROOT}),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
