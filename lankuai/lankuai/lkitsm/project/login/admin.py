from django.contrib import admin
from . models import User ,Role ,Jobgrade ,technicalGrade

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Jobgrade)
admin.site.register(technicalGrade)

