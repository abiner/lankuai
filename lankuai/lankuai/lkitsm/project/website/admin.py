from django.contrib import admin

# Register your models here.
from . models import WorkList
# 将模板注册到后台，这样可以在后台管理

admin.site.register(WorkList)


