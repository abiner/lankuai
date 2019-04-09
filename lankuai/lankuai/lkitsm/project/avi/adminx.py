import xadmin
from .models import Video ,Grade ,Isee


#创建注册类
class VideoAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['uploader' ,'imgpath' ,'uppath' ,'describe' ,'uploaddate' ,'kind' ,'score' ,'haveseen']


    #每页显示多少个
    list_per_page=20

    # 配置在哪些字段搜索
    search_fields = ['uploader', 'describe' ,'kind']

    #配置过滤字段
    list_filter = ['uploader', 'describe' ,'kind']

    #显示详情
    show_detail_fields = ['id']

    #数据刷新时间
    refresh_times=(30,60)

    # 导出类型   默认已经有了
    #list_export = ('xls', 'xml', 'json')

    # 导出字段 默认是全部
    #list_export_fields = ()

xadmin.site.register(Video, VideoAdmin)