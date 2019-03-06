#导入xamin模块
import xadmin
#导入School表
from .models import WorkList ,Process

#创建注册类
class WorkListAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['billingTime' ,'workOrderNo' ,'unitName' ,'clientName' ,'clientPho' ,'clientAddress' ,'faultClass'
        ,'incidentCla' ,'incidentRank' ,'incidentState' ,'incidentTheme' ,'incidentDescribe' ,'manageCourse' ,'creator'
        ,'workState' ,'flowHandler']
    #每页显示多少个
    list_per_page=20

    # 配置在哪些字段搜索
    search_fields = ['unitName', 'workState' ,'creator']

    #配置过滤字段
    list_filter=['unitName', 'workState' ,'creator' ,'faultClass' ,'incidentRank']

    #显示详情
    show_detail_fields=['workOrderNo']

    #数据刷新时间
    refresh_times=(30,60)

    # 导出类型   默认已经有了
    #list_export = ('xls', 'xml', 'json')

    # 导出字段 默认是全部
    #list_export_fields = ()

xadmin.site.register(WorkList, WorkListAdmin)

#创建注册类
class ProcessAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['finalTime' ,'wOrderNo' ,'process' ,'wState' ,'fHandler']
    #每页显示多少个
    list_per_page=20

    # 配置在哪些字段搜索
    search_fields = ['wState']

    #配置过滤字段
    list_filter=['wState']

    #显示详情
    show_detail_fields=['finalTime' ,'wOrderNo' ,'process' ,'wState' ,'fHandler']

    #数据刷新时间
    refresh_times=(30,60)

    # 导出类型   默认已经有了
    #list_export = ('xls', 'xml', 'json')

    # 导出字段 默认是全部
    #list_export_fields = ()

xadmin.site.register(Process, ProcessAdmin)


