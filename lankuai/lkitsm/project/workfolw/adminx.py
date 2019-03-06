#导入xamin模块
import xadmin
#导入School表
from .models import Workflow ,Notice

#创建注册类
class WorkflowAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['wid' ,'wname' ,'wdepname' ,'wapplytype' ,'wbegin' ,'wfinish' ,'wreasons' ,'hierarchy0']
    #每页显示多少个
    list_per_page=20

    # 配置在哪些字段搜索
    search_fields = ['wid', 'wname' ,'wapplytype' ,'hierarchy0']

    #配置过滤字段
    list_filter=['wid', 'wname' ,'wapplytype' ,'hierarchy0']

    #显示详情
    show_detail_fields=['workOrderNo']

    #数据刷新时间
    refresh_times=(30,60)

    # 导出类型   默认已经有了
    #list_export = ('xls', 'xml', 'json')

    # 导出字段 默认是全部
    #list_export_fields = ()

xadmin.site.register(Workflow, WorkflowAdmin)

#创建注册类
class NoticeAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['moticeid' ,'nname' ,'headline' ,'issuetime' ,'nclassify' ,'audit' ,'picture' ,'article']
    #每页显示多少个
    list_per_page=20

    # 配置在哪些字段搜索
    search_fields = ['moticeid', 'nname']

    #配置过滤字段
    list_filter=['moticeid', 'nname']

    #显示详情
    show_detail_fields=['moticeid']

    #数据刷新时间
    refresh_times=(30,60)

    # 导出类型   默认已经有了
    #list_export = ('xls', 'xml', 'json')

    # 导出字段 默认是全部
    #list_export_fields = ()

xadmin.site.register(Notice, NoticeAdmin)
