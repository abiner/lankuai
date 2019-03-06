from django.db import models

#商务合同
class Business(models.Model):
    pactNo = models.CharField(r'合同编号',max_length=20)
    projectname = models.CharField(r'项目名称',max_length=40)
    signedname = models.CharField(r'签约名称',max_length=40)
    signedsubject = models.CharField(r'签约主体',max_length=40)
    billingunit = models.CharField(r'开票单位',max_length=40)
    executedate = models.CharField(r'执行日期',max_length=20)
    begindate = models.CharField(r'开始日期',max_length=20)
    overdate = models.CharField(r'结束日期',max_length=20)
    pacttotalsum = models.CharField(r'合同总额',max_length=20)
    monthlyfee = models.CharField(r'月均费用',max_length=20)
    Agreedpaymenttime = models.CharField(r'约定付款时间',max_length=20,null=True,blank=True)
    knotrate = models.CharField(r'结费方式',max_length=20)
    accountmanager = models.CharField(r'客户负责人',max_length=20)
    projectaddress = models.CharField(r'项目地址',max_length=40)
    followuppeople = models.CharField(r'项目跟进人',max_length=20)
    servertype = models.CharField(r'服务类型',max_length=40,null=True,blank=True)
    servicemode = models.CharField(r'服务方式',max_length=20)
    isDelete = models.BooleanField(default=False)
#business
    class Meta:
        db_table = 'business'
        verbose_name = '商务合同'
        verbose_name_plural = '商务合同'
    @classmethod
    def createbusiness(cls ,pactno, pname, sname, ssubject, bunit, edate, bdate, odate, psum, mfee, Amenttime, ktrate
                       , amanager, paddress, fuppeople, stype ,smode,isD=False):
        cwl = cls(pactNo=pactno ,projectname=pname , signedname=sname , signedsubject=ssubject , billingunit=bunit
                  , executedate=edate ,begindate=bdate , overdate=odate , pacttotalsum=psum , monthlyfee=mfee
                  , Agreedpaymenttime=Amenttime , knotrate=ktrate ,accountmanager=amanager , projectaddress=paddress
                  , followuppeople=fuppeople , servertype=stype , servicemode=smode )
        return cwl

#合同附带文件
class files(models.Model):
    pactNo = models.CharField(r'合同编号',max_length=20)
    file = models.FileField(max_length=255 ,upload_to='contractfile')
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'files'
        verbose_name = '合同附带文件'
        verbose_name_plural = '合同附带文件'

    @classmethod
    def createfiles(cls ,pact ,fil ,isD=False):
        f = cls(pactNo=pact ,file=fil)
        return f
