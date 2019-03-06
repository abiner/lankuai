from django.db import models

#故障信息表
class failureMessages(models.Model):
    #故障 fault
    #faultID,fname,inunits,phone,faultclass,brandtype,equipmentID,faultdescribe,subtime,eventlevel
    faultID = models.CharField(r'故障ID' ,max_length=50 ,primary_key=True)
    fname = models.CharField(r'故障申请人姓名' ,max_length=20)
    inunits = models.CharField(r'故障申请人所在单位' ,max_length=50)
    phone = models.CharField(r'申请人联系电话' ,max_length=50)
    faultclass = models.CharField(r'故障分类' ,max_length=20)
    brandtype = models.CharField(r'设备名称型号' ,max_length=20 ,null=True,blank=True)
    equipmentID = models.CharField(r'设备ID' ,max_length=50 ,null=True,blank=True)
    faultdescribe = models.CharField(r'故障描述' ,max_length=200)
    subtime = models.DateTimeField(r'提交时间' ,auto_now_add=True)
    eventlevel = models.IntegerField(r'初始状态' ,default= -1)#默认-1刚提交，0驳回，100成功
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'failureMessages'
        verbose_name = '维修，故障信息表'
        verbose_name_plural = '维修，故障信息表'
    @classmethod
    def createfailureMessages(cls ,faultid ,fname ,inunits ,phone ,faultc ,brandtype ,equipmentID,faultdescribe,subtime,eventlevel ,isD=False):
        failurem = cls(faultID=faultid ,fname=fname,inunits=inunits,phone=phone,faultclass=faultc,brandtype=brandtype
                       ,equipmentID=equipmentID,faultdescribe=faultdescribe,subtime=subtime,eventlevel=eventlevel)
        return failurem

#故障信息表之故障分类
class faultType(models.Model):
    ftid = models.IntegerField(r"维修，故障类型ID")
    wapplytype = models.CharField(r"维修，故障类型" ,max_length=20)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'faultType'
        verbose_name = '故障信息表之故障分类'
        verbose_name_plural = '故障信息表之故障分类'

#维修 ，打印机与非打印机上门人选   打印机故障，候选人一，候选人二，ID对应    个人  部门ID，添加其他人时，请注意
#打印机黄振明  7 ，采购部唐涛  4，
class theDoorOf(models.Model):
    tdoid = models.IntegerField(r"ID")
    repairtype = models.CharField(r"故障类型" ,max_length=20)
    tdoname = models.CharField(r"姓名" ,max_length=20)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'theDoorOf'
        verbose_name = '维修 ，打印机与非打印机上门人选'
        verbose_name_plural = '维修 ，打印机与非打印机上门人选'

#进阶 ，状态转变
class State(models.Model):
    #某故障ID被某类型的谁，从某状态改为某状态，状态是eventlevel
    my_workflow_id = models.IntegerField(u'故障id')  # 故障id
    participant_type = models.IntegerField(u'参与者类型')  # 1.个人（唐黄，） 2.部门（部门经理）
    participant = models.CharField(u'参与者', max_length=30)  # 提交者
    name = models.CharField(u'名称', max_length=30)
    source_state_id = models.IntegerField(u'原状态id')     #默认-1       1
    dest_state_id = models.IntegerField(u'目标状态id')      #1          2
    is_end_state = models.BooleanField(u'是否为最终状态')#两种最终状态，0失败，100成功
    gmt_created = models.DateTimeField(u'创建时间', auto_now_add=True)
    gmt_modified = models.DateTimeField(u'修改时间', auto_now=True)
    is_deleted = models.BooleanField(u'已删除', default=False)
    class Meta:
        db_table = 'state'
        verbose_name = '维修，故障进阶状态'
        verbose_name_plural = '维修，故障进阶状态'

#故障原因和成本价表
class cost(models.Model):
    #faultID,cname,cause,supplies,costprice,subtime
    faultID = models.CharField(r'故障ID', max_length=50)
    cname = models.CharField(r'检测人姓名' ,max_length=20)
    cause = models.CharField(r'故障原因描述' ,max_length=200 ,null=True,blank=True)
    supplies = models.CharField(r'可能使用耗材量说明' ,max_length=200 ,null=True,blank=True)
    costprice = models.CharField(r'耗材成本总价' ,max_length=200 ,blank=True)
    subtime = models.DateTimeField(r'提交时间' ,auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'cost'
        verbose_name = '维修，故障原因和成本价表'
        verbose_name_plural = '维修，故障原因和成本价表'
    @classmethod
    def createcost(cls ,faultID ,cname,cause,supplies,costprice,subtime,isD=False):
        co = cls(faultID=faultID ,cname=cname,cause=cause,supplies=supplies,costprice=costprice,subtime=subtime)
        return co

#部门经理报价表
class quote(models.Model):
    #故障ID ，部门经理姓名，报价，备注，提交时间
    #faultID,oname,quo,comment,subtime
    faultID = models.CharField(r'故障ID', max_length=50)
    oname = models.CharField(r'部门经理姓名' ,max_length=20)
    quo = models.CharField(r'报价' ,max_length=20)
    comment = models.CharField(r'备注' ,max_length=200)
    subtime = models.DateTimeField(r'提交时间' ,auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'quote'
        verbose_name = '维修，部门经理报价表'
        verbose_name_plural = '维修，部门经理报价表'
    @classmethod
    def createquote(cls ,faultID,oname,quo,comment,subtime,isD=False):
        quot = cls(faultID=faultID,oname=oname,quo=quo,comment=comment,subtime=subtime)
        return quot

#检测人维修结果
class repairResult(models.Model):
    #故障ID ，检测人姓名，备注，提交时间
    #faultID,rname,comment,subtime
    faultID = models.CharField(r'故障ID', max_length=50)
    rname = models.CharField(r'检测人姓名' ,max_length=20)
    comment = models.CharField(r'备注' ,max_length=200)
    subtime = models.DateTimeField(r'提交时间' ,auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'repairResult'
        verbose_name = '维修，维修结果'
        verbose_name_plural = '维修，维修结果'
    @classmethod
    def createquote(cls ,faultID,oname,quo,comment,subtime,isD=False):
        quot = cls(faultID=faultID,oname=oname,quo=quo,comment=comment,subtime=subtime)
        return quot


#采购，
#   商品 goods 采购 purchase 申请 applyfor 成本 cost 经理 manager 同意 consent 发起人 initiator 收货人 consignee

class Goods(models.Model):
    purchaseID = models.IntegerField(u"采购ID")
    gname = models.CharField(u"商品名称" ,max_length=20)
    gamount = models.IntegerField(u"商品数量")
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'goods'
        verbose_name = '采购，商品表'
        verbose_name_plural = '采购，商品表'
    @classmethod
    def creategoods(cls ,purchaseID ,gname ,gamount,isD=False):
        goods = cls(purchaseID=purchaseID,gname=gname,gamount=gamount)
        return goods

#采购申请表
class purchaseApplyFor(models.Model):
    purchaseID = models.IntegerField(u"采购ID")
    pdemp = models.CharField(u"申请人部门" ,max_length=20)
    pname = models.CharField(u"申请人姓名" ,max_length=20)
    pdate = models.DateTimeField(u"申请时间" ,auto_now_add=True)
    pcomment = models.CharField(u"备注" ,max_length=200)
    pcourse = models.IntegerField(u"状态" ,default= -1)#默认-1刚提交，0驳回，100成功
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'purchaseapplyfor'
        verbose_name = '采购，采购申请表'
        verbose_name_plural = '采购，采购申请表'
    @classmethod
    def createpurchaseApplyFor(cls ,pid ,pdemp ,pname ,pdate ,pcomment ,pcourse ,isD=False):
        paf = cls(purchaseID=pid ,pdemp=pdemp ,pname=pname ,pdate=pdate ,pcomment=pcomment ,pcourse=pcourse)
        return paf

#商品成本表
class goodsCost(models.Model):
    purchaseID = models.IntegerField(u"采购ID")
    gcgprice = models.IntegerField(u"商品成本单价")
    suggestprice = models.IntegerField(u"单个商品建议售价")
    goodsprofit = models.IntegerField(u"单个商品利润")
    gcdate = models.DateTimeField(u"填写时间" ,auto_now_add=True)
    pcomment = models.CharField(u"备注" ,max_length=200)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'goodscost'
        verbose_name = '采购，商品成本表'
        verbose_name_plural = '采购，商品成本表'
    @classmethod
    def creategoodsCost(cls ,purchaseID ,gcgprice ,suggestprice ,goodsprofit ,gcdate ,pcomment,isD=False):
        gc = cls(purchaseID=purchaseID ,gcgprice=gcgprice ,suggestprice=suggestprice ,goodsprofit=goodsprofit ,gcdate=gcdate ,pcomment=pcomment)
        return gc



#部门经理同意表                                                增加部门经理姓名
class managerConsent(models.Model):
    purchaseID = models.IntegerField(u"采购ID")
    affirmprice = models.IntegerField(u"确认单个商品售价")
    mcdate = models.DateTimeField(u"同意时间" ,auto_now_add=True)
    pcomment = models.CharField(u"备注" ,max_length=200)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'managerconsent'
        verbose_name = '采购，部门经理同意采购表'
        verbose_name_plural = '采购，部门经理同意采购表'
    @classmethod
    def createmanagerConsent(cls ,purchaseID ,affirmprice ,mcdate ,pcomment ,isD=False):
        mc = cls(purchaseID=purchaseID ,affirmprice=affirmprice ,mcdate=mcdate ,pcomment=pcomment)
        return mc

#发起人收货表
class Consignee(models.Model):
    purchaseID = models.IntegerField(u"采购ID")
    cgdate = models.DateTimeField(u"收货时间" ,auto_now_add=True)
    pcomment = models.CharField(u"备注" ,max_length=200)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'consignee'
        verbose_name = '采购，发起人收货表'
        verbose_name_plural = '采购，发起人收货表'
    @classmethod
    def createconsignee(cls ,purchaseID ,cgdate ,pcomment ,isD=False):
        cg = cls(purchaseID=purchaseID ,cgdate=cgdate ,pcomment=pcomment)
        return cg
























