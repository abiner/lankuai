from django.contrib import admin

# Register your models here.

from . models import failureMessages ,cost,quote,repairResult ,faultType ,theDoorOf ,State ,Goods ,purchaseApplyFor \
    ,goodsCost ,managerConsent ,Consignee
admin.site.register(failureMessages)
admin.site.register(cost)
admin.site.register(quote)
admin.site.register(repairResult)
admin.site.register(faultType)
admin.site.register(theDoorOf)
admin.site.register(State)

admin.site.register(Goods)
admin.site.register(purchaseApplyFor)
admin.site.register(goodsCost)
admin.site.register(managerConsent)
admin.site.register(Consignee)








