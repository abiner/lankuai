
'''

新添一个故障分类，在（打印机，非打印）故障中使用，因为会有第三个可能

'''
from django.db import models
from datetime import *
# 公司部门
class Departments(models.Model):
    did = models.IntegerField(r"部门ID")
    depname = models.CharField(r"部门名称", max_length=20)
    dname = models.CharField(r"部门简称" ,max_length=20)#部门简称的意义在于需要定义前端button name属性，只因为部门ID关联着工作流的事件进度
    manager = models.CharField(u'部门经理', max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return '(%s%s)' % (self.depname ,self.dname)  # 返回属性的显示内同

    class Meta:
        verbose_name = '公司内部门'
        verbose_name_plural = '公司内部门'
        db_table = 'Departments'


# 单位/项目信息
class UnitName(models.Model):
    dname = models.CharField(r'单位负责人', max_length=20)  # 部门负责人
    unitName = models.CharField(r'单位名称', max_length=20 ,primary_key=True)  # 单位名称
    uname = models.CharField(r'单位简称', max_length=10)  # 单位简称
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return '(%s)' % (self.unitName)

    class Meta:
        verbose_name = '单位名称'
        verbose_name_plural = '单位名称'
        db_table = 'UnitName'


# 故障类
class china_regionalTablet(models.Model):
    name = models.CharField(max_length=20)          # 故障名称
    level = models.IntegerField()                   # 故障层级
    parent = models.IntegerField()                  # 故障分类
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        db_table = 'china'


# 工单系统
class WorkList(models.Model):

    billingTime = models.CharField(r'开单时间',max_length=20)
    workOrderNo = models.CharField(r'工单号' ,max_length=50)
    unitName = models.CharField(r"单位名称"  ,max_length=20)
    clientName = models.CharField(r'客户姓名', max_length=20)
    clientPho = models.CharField(r'客户电话' ,max_length=50)
    clientAddress = models.CharField(r'客户位置', max_length=100)

    faultClass = models.CharField(r'故障大类', max_length=20)
    faultClasss = models.CharField(r'故障小类', max_length=20)
    faultDetail = models.CharField(r'故障明细', max_length=20)

    incidentCla = models.CharField(r'事件分类', max_length=20)
    incidentRank = models.CharField(r'事件级别', max_length=20)
    incidentState = models.CharField(r'事件状态', max_length=20)
    incidentTheme = models.CharField(r'事件主题', max_length=100)
    incidentDescribe = models.CharField(r'事件描述', max_length=100)
    manageCourse = models.CharField(r'处理过程', max_length=200 ,null=True)
    creator = models.CharField(r'创建人' ,max_length=20)
    workState = models.CharField(r'工单状态', max_length=20)
    flowHandler = models.CharField("流转处理人" ,max_length=20 ,null=True)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'WorkList'
        verbose_name = '工单系统'
        verbose_name_plural = '工单系统'
    @classmethod
    def createWorkList(cls ,billingT, workNo, unitN, clientN, clientP, clientA, faultC, faultCs, faultD, incidentC
                       , incidentR, incidentS, incidentT, incidentD, manageC, cre ,workS, flowH, isD=False):
        cwl = cls(billingTime = billingT,workOrderNo = workNo,unitName = unitN,clientName = clientN,clientPho = clientP
                  ,clientAddress = clientA,faultClass = faultC,faultClasss = faultCs,faultDetail = faultD
                  ,incidentCla = incidentC,incidentRank = incidentR,incidentState = incidentS, incidentTheme = incidentT
                  ,incidentDescribe = incidentD,manageCourse = manageC,creator = cre ,workState = workS,flowHandler = flowH)
        return cwl






class Process(models.Model):
    finalTime = models.CharField(r'完成时间' ,max_length=20)
    wOrderNo = models.CharField(r'工单号' ,max_length=50)
    process = models.CharField(r'处理过程' ,max_length=200)
    wState = models.CharField(r'工单状态', max_length=20)
    fHandler = models.CharField(r'流转处理人' ,max_length=20)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'Process'
        verbose_name = '处理过程'
        verbose_name_plural = '处理过程'
    @classmethod
    def createProcess(cls ,fTime,won ,pro ,wsta ,fhand ,isD = False):
        p = cls(finalTime = fTime ,wOrderNo = won ,process = pro ,wState=wsta ,fHandler = fhand)
        return p



# ***********************************************************************************************
######没有注册到数据库


# ***********************************************************************************************
# _____________________________________WEBOA_____________________________________________________
# 工程师培训学习考核记录
# 工程师岗位状态转换流程记录--项目岗位转换
# 调休/事假/病假/加班申请等
# 试工--入职--正式--级别提升申请
# 公司服务事件记录表


# 项目客户部门信息
class CustomerDep(models.Model):
    cdname = models.CharField(u'项目部门', max_length=100)
    dpname = models.ForeignKey("UnitName", on_delete=models.CASCADE, )  # 项目名称------------

    def __str__(self):
        return '%s' % self.cdname  # 返回属性的显示内同

    class Meta:
        verbose_name = '项目部门表'
        verbose_name_plural = '项目部门表'
        db_table = 'CustomerDep'


# 项目客户信息
class Customersess(models.Model):
    cname = models.CharField(u'客户姓名', max_length=40)
    cphone = models.IntegerField(u'客户电话')
    # cpasswd=models.CharField(u'登陆密码',max_length=40)
    cprojectname = models.ForeignKey("UnitName", on_delete=models.CASCADE, )  # 客户所属项目-----------
    cdepname = models.ForeignKey("CustomerDep", on_delete=models.CASCADE, )  # 客户所属部门----------

    def __str__(self):
        return '%s' % self.cname  # 返回属性的显示内同

    class Meta:
        verbose_name = '客户人员信息表'
        verbose_name_plural = '客户人员信息表'
        db_table = 'Customersess'


# ______________________________________ITIL______________________________________________________
class Itilworklog(models.Model):
    pass


class Itsla(models.Model):
    pass


class Itfaulttpye(models.Model):
    pass
