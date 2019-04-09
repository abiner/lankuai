from django.db import models
from datetime import *
# Create your models here.

#公司内部部门
class Departments(models.Model):
    depname=models.CharField(u'部门名称',max_length=40)
    depmanagerid=models.CharField(u'部门经理',max_length=40)
    def __str__(self):
        return '%s' % self.depname#返回属性的显示内同
    class Meta:
        verbose_name='公司内部门'
        verbose_name_plural='公司内部门'

#公司工程师信息
class User(models.Model):
    uname=models.CharField(u'姓名',max_length=40)
    upasswd=models.CharField(u'系统密码',max_length=40)
    uCreatedate=models.DateField(U'入职日期',auto_now_add=True)#获取创建日期
    uupoto=models.ImageField(u'照片')
    userworkid=models.CharField(u'工号',max_length=20)
    uidcard=models.IntegerField(u'身份证号码')
    utelphone=models.IntegerField(u'手机号码')
    uemail=models.EmailField(u'邮箱地址')#自动验证邮件格式
    ufirstcontact=models.CharField(u'联系人姓名',max_length=40)
    uconphone=models.IntegerField(u'联系人号码')
    uaddress=models.CharField(u'住址',max_length=100)
    ugender=models.BooleanField(default=True)#性别
    ueduschool=models.CharField(u'毕业院校',max_length=40)
    ueducation=models.CharField(u'学历',max_length=20)
    uorigin=models.CharField(u'籍贯',max_length=20)
    isDelect=models.BooleanField(default=False)#是否在职状态
    uprojectname=models.ForeignKey("Projects",on_delete=models.CASCADE,)  #所属项目------------
    udepname=models.ForeignKey("Departments",on_delete=models.CASCADE,)#所属部门---------------
    ulasttime=models.DateField(auto_now=True)#获取修改日期
    def __str__(self):
        return '%s' % self.uname#返回属性的显示内同
    class Meta:
        verbose_name='工程师信息表'
        verbose_name_plural='工程师信息表'
#***********************************************************************************************
######没有注册到数据库





#***********************************************************************************************
#_____________________________________WEBOA_____________________________________________________
#工程师培训学习考核记录
#工程师岗位状态转换流程记录--项目岗位转换
#调休/事假/病假/加班申请等
#试工--入职--正式--级别提升申请
#公司服务事件记录表

#项目信息
class Projects(models.Model):
    pname=models.CharField(u'项目名称',max_length=100)
    pname=models.CharField(u'项目简称',max_length=100)
    paddress=models.CharField(u'项目地址',max_length=100)
    pcreatedate=models.DateField(auto_now_add=True)
    plastdate=models.DateField(auto_now=True)
    def __str__(self):
        return '%s' % self.pname#返回属性的显示内同
    class Meta:
        verbose_name='项目信息表'
        verbose_name_plural='项目信息表'

#项目客户部门信息
class CustomerDep (models.Model):
    cdname=models.CharField(u'项目部门',max_length=100)
    dpname=models.ForeignKey("Projects",on_delete=models.CASCADE,)#项目名称------------
    def __str__(self):
        return '%s' % self.cdname#返回属性的显示内同
    class Meta:
        verbose_name='项目部门表'
        verbose_name_plural='项目部门表'

#项目客户信息
class Customersess(models.Model):
    cname=models.CharField(u'客户姓名',max_length=40)
    cphone=models.IntegerField(u'客户电话')
    # cpasswd=models.CharField(u'登陆密码',max_length=40)
    cprojectname=models.ForeignKey("Projects",on_delete=models.CASCADE,)#客户所属项目-----------
    cdepname=models.ForeignKey("CustomerDep",on_delete=models.CASCADE,)#客户所属部门----------
    def __str__(self):
        return '%s' % self.cname#返回属性的显示内同
    class Meta:
        verbose_name='客户人员信息表'
        verbose_name_plural='客户人员信息表'

#______________________________________ITIL______________________________________________________
class Itilworklog(models.Model):
    pass

class Itsla(models.Model):
    pass

class Itfaulttpye(models.Model):
    pass













