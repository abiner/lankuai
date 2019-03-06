
from django.contrib import admin

from .models import Workflow,managerApproval ,Classify ,Notice

admin.site.register(Workflow)

admin.site.register(managerApproval)

admin.site.register(Classify)

admin.site.register(Notice)