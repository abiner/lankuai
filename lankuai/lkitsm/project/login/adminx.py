#导入xamin模块
import xadmin
#导入School表
from .models import User ,Role ,Jobgrade ,technicalGrade

#创建注册类
class UserAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['uname' ,'ugender' ,'uCreatedate' ,'uworkid' ,'uidcard' ,'uphone' ,'uemail'
        ,'ufirstcontact' ,'uconphone' ,'uaddress' ,'ueduschool' ,'ueducation' ,'uorigin' ,'udepname' ,'unit' ,'role'
        ,'jobgrade' ,'technicalgrade' ,'ulasttime' ,'isDelect' ,'utoken' ,'isDelete']

    #每页显示多少个
    list_per_page=20

    # 配置在哪些字段搜索
    search_fields = ['uname', 'uphone' ,'role' ,'uphone' ,'jobgrade' ,'technicalgrade']

    #配置过滤字段
    list_filter = ['uname', 'uphone' ,'role' ,'uphone' ,'jobgrade' ,'technicalgrade']

    #显示详情
    show_detail_fields=['uname']

    #数据刷新时间
    refresh_times=(30,60)

    # 导出类型   默认已经有了
    #list_export = ('xls', 'xml', 'json')

    # 导出字段 默认是全部
    #list_export_fields = ()

xadmin.site.register(User, UserAdmin)
