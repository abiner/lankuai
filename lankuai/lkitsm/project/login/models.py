from django.db import models


'''
记录标识,tu_id,bigint,      pk, not null
所属组织,to_id,             fk, not null





'''

# 员工信息                  可能需要添加到字段   ：登录时间，上次登录时间，登录次数
class User(models.Model):
    uname = models.CharField(u'姓名', max_length=40 ,primary_key=True)
    upasswd = models.CharField(u'系统密码', max_length=40)
    ugender = models.BooleanField(default=True)  # 性别
    uCreatedate = models.DateField(u'入职日期' ,auto_now_add=True)  # 入职日期手动填写
    uupoto = models.ImageField(u'照片',upload_to='headportrait' ,null=True ,blank=True)  # ,upload_to='',max_length=400#路径为空，表示让django自己选择setting.py中设置的路径，上传的图片会自动保存到static的根目录
    uworkid = models.CharField(u'工号', max_length=100)   #唯一,位数统一,
    uidcard = models.CharField(u'身份证号码' ,max_length=100)
    ubirthday = models.DateField(u"出生年月日" ,auto_now_add=True)
    uphone = models.CharField(u'手机号码' ,max_length=100)
    uemail = models.EmailField(u'邮箱地址')  # 自动验证邮件格式
    ufirstcontact = models.CharField(u'联系人姓名', max_length=40 ,null=True ,blank=True)
    uconphone = models.CharField(u'联系人号码' ,max_length=40,null=True ,blank=True)
    uaddress = models.CharField(u'现住址', max_length=200,null=True ,blank=True)
    ueduschool = models.CharField(u'毕业院校', max_length=100,null=True ,blank=True)
    ueducation = models.CharField(u'学历', max_length=20,null=True ,blank=True)
    uorigin = models.CharField(u'籍贯', max_length=20,null=True ,blank=True)
    udepname = models.CharField(u"所在部门" ,max_length=40,null=True ,blank=True)
    unit = models.CharField(u"所在单位" ,max_length=40,null=True ,blank=True)          #所在单位
    role = models.IntegerField(u'角色层级')                                         #角色层级 员工0	，	部门主管1		，部门经理2	，总经理3
    jobgrade = models.IntegerField(u'岗位级别' ,null=True ,blank=True)   #实习0，试用1，正式2	，1星3，2星4，3星5，4星6，5星7
    technicalgrade = models.IntegerField(u'技术等级' ,null=True ,blank=True)#技术等级：12345
    ulasttime = models.DateField(u"最后修改日期" ,auto_now=True)                                        # 获取修改日期
    isDelect = models.BooleanField(default=True)                                  # 是否在职状态,默认在职，为False则已离职，不可登录
    utoken = models.CharField(max_length=50)                                        #登录验证
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.uname  # 返回属性的显示内同

    class Meta:
        verbose_name = '员工表'
        verbose_name_plural = '员工表'
        db_table = 'user'
    @classmethod
    def createUser(cls ,uname,upasswd,ugender,uCreatedate,uupoto,uworkid,uidcard,ubirthday ,uphone,uemail,ufirstcontact,uconphone
                   ,uaddress,ueduschool,ueducation,uorigin,udepname,unit,role,jobgrade,technicalgrade,ulasttime
                   ,isDelect,utoken ,isD=False):
        user = cls(uname=uname,upasswd=upasswd ,ugender=ugender ,uCreatedate=uCreatedate ,uupoto=uupoto ,uworkid=uworkid
            ,uidcard=uidcard ,ubirthday=ubirthday ,uphone=uphone ,uemail=uemail ,ufirstcontact=ufirstcontact ,uconphone=uconphone
            ,uaddress=uaddress ,ueduschool=ueduschool ,ueducation=ueducation ,uorigin=uorigin
            ,udepname=udepname ,unit=unit ,role=role ,jobgrade=jobgrade ,technicalgrade=technicalgrade
            ,ulasttime=ulasttime ,isDelect=isDelect ,utoken=utoken)
        return user


# 部门，单位，角色层级，
# 角色层级 员工0	，	部门主管1		，部门经理2	，总经理3
class Role(models.Model):
    roleid = models.IntegerField(u"角色ID" ,primary_key=True)
    rrole = models.CharField(u"角色" ,max_length=40)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.rrole  # 返回属性的显示内同

    class Meta:
        verbose_name = '角色层级表'
        verbose_name_plural = '角色层级表'
        db_table = 'role'

# 岗位级别表 实习0，试用1，正式2	，1星3，2星4，3星5，4星6，5星7
class Jobgrade(models.Model):
    jobID = models.IntegerField(u"岗位ID" ,primary_key=True)
    jjobgrade = models.CharField(u"岗位级别" ,max_length=40)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.jjobgrade  # 返回属性的显示内同

    class Meta:
        verbose_name = '岗位级别表'
        verbose_name_plural = '岗位级别表'
        db_table = 'jobgrade'

# 技术等级表 技术等级：12345
class technicalGrade(models.Model):
    tgid = models.IntegerField(u"技术等级ID" ,primary_key=True)
    tgtechnicalgrade = models.CharField(u"技术等级" ,max_length=40)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.tgtechnicalgrade  # 返回属性的显示内同

    class Meta:
        verbose_name = '技术等级表'
        verbose_name_plural = '技术等级表'
        db_table = 'technicalgrade'



