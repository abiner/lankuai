#导入xamin模块
import xadmin
#导入School表
from .models import failureMessages ,purchaseApplyFor ,Goods

#创建注册类
class failureMessagesAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['faultID' ,'fname' ,'inunits' ,'phone' ,'faultclass' ,'brandtype' ,'equipmentID' ,'faultdescribe' ,'subtime' ,'eventlevel']

    #每页显示多少个
    list_per_page=20

    # 配置在哪些字段搜索
    search_fields = ['faultID', 'fname' ,'inunits']

    #配置过滤字段
    list_filter = ['faultID', 'fname' ,'inunits']

    #显示详情
    show_detail_fields=['faultID']

    #数据刷新时间
    refresh_times=(30,60)

    # 导出类型   默认已经有了
    #list_export = ('xls', 'xml', 'json')

    # 导出字段 默认是全部
    #list_export_fields = ()

xadmin.site.register(failureMessages ,failureMessagesAdmin)

#创建注册类
class purchaseApplyForAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['purchaseID' ,'pdemp' ,'pname' ,'pdate' ,'pcomment' ,'pcourse']
    #每页显示多少个
    list_per_page=20

    # 配置在哪些字段搜索
    search_fields = ['purchaseID', 'pname' ,'pcourse']

    #配置过滤字段
    list_filter = ['purchaseID', 'pname' ,'pcourse']

    #显示详情
    show_detail_fields=['purchaseID']

    #数据刷新时间
    refresh_times=(30,60)

    # 导出类型   默认已经有了
    #list_export = ('xls', 'xml', 'json')

    # 导出字段 默认是全部
    #list_export_fields = ()

xadmin.site.register(purchaseApplyFor, purchaseApplyForAdmin)


#创建注册类
class GoodsAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['purchaseID' ,'gname' ,'gamount']
    #每页显示多少个
    list_per_page=20

    # 配置在哪些字段搜索
    search_fields = ['purchaseID', 'gname']

    #配置过滤字段
    list_filter = ['purchaseID', 'gname']

    #显示详情
    show_detail_fields=['purchaseID']

    #数据刷新时间
    refresh_times=(30,60)

    # 导出类型   默认已经有了
    #list_export = ('xls', 'xml', 'json')

    # 导出字段 默认是全部
    #list_export_fields = ()

xadmin.site.register(Goods, GoodsAdmin)
