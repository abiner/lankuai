
'''

新添一个故障分类，在（打印机，非打印）故障中使用，因为会有第三个可能

'''
from django.db import models
from datetime import *

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
    manageCourse = models.CharField(r'处理过程', max_length=200)
    creator = models.CharField(r'创建人' ,max_length=20)
    workState = models.CharField(r'工单状态', max_length=20)
    flowHandler = models.CharField("流转处理人" ,max_length=20)
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



