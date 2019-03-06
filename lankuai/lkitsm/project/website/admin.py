from django.contrib import admin

# Register your models here.
from . models import Departments,Customersess,CustomerDep,UnitName ,WorkList
# 将模板注册到后台，这样可以在后台管理

admin.site.register(Departments)
admin.site.register(Customersess)
admin.site.register(CustomerDep)
admin.site.register(UnitName)
admin.site.register(WorkList)


