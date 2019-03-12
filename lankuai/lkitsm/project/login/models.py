from django.db import models



# 员工信息                  可能需要添加到字段   ：登录时间，上次登录时间，登录次数

class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    year = (
        ("thisyear", '应届'),
        ("laseyear", '往届'),
    )

    uname = models.CharField(u'姓名', max_length=40 ,primary_key=True)
    upasswd = models.CharField(u'系统密码', max_length=40)
    ugender = models.CharField(max_length=32 ,choices=gender ,default="男" ,null=True ,blank=True)  # 性别
    uCreatedate = models.DateField(u'入职日期' ,auto_now_add=True ,null=True ,blank=True)  # 入职日期手动填写
    uupoto = models.ImageField(u'照片',upload_to='headportrait' ,null=True ,blank=True)  # ,upload_to='',max_length=400#路径为空，表示让django自己选择setting.py中设置的路径，上传的图片会自动保存到static的根目录
    uworkid = models.CharField(u'工号', max_length=100 ,null=True ,blank=True)   #唯一,位数统一,
    uidcard = models.CharField(u'身份证号码' ,max_length=100 ,null=True ,blank=True)
    ubirthday = models.DateField(u"出生年月日" ,auto_now_add=True ,null=True ,blank=True)
    uphone = models.CharField(u'手机号码' ,max_length=100)
    uemail = models.EmailField(u'邮箱地址' ,null=True ,blank=True)  # 自动验证邮件格式
    ufirstcontact = models.CharField(u'联系人姓名', max_length=40 ,null=True ,blank=True)
    uconphone = models.CharField(u'联系人号码' ,max_length=40,null=True ,blank=True)
    uaddress = models.CharField(u'现住址', max_length=200,null=True ,blank=True)
    ueduschool = models.CharField(u'毕业院校', max_length=100,null=True ,blank=True)
    ueducation = models.CharField(u'学历', max_length=20,null=True ,blank=True)
    uorigin = models.CharField(u'籍贯', max_length=20,null=True ,blank=True)
    udepname = models.CharField(u"所在部门" ,max_length=40,null=True ,blank=True)
    unit = models.CharField(u"所在单位" ,max_length=40,null=True ,blank=True)          #所在单位
    role = models.IntegerField(u'角色层级')                                         #角色层级 员工0	，	部门主管1		，部门经理2	，总经理3
    jobgrade = models.IntegerField(u'岗位级别' ,null=True ,blank=True)   # 临时-1 实习0，试用1，正式2	，1星3，2星4，3星5，4星6，5星7
    technicalgrade = models.IntegerField(u'技术等级' ,null=True ,blank=True)#技术等级：12345
    ulasttime = models.DateField(u"最后修改日期" ,auto_now=True)                                        # 获取修改日期
    isDelect = models.BooleanField(default=True)                                  # 是否在职状态,默认在职，为False则已离职，不可登录
    utoken = models.CharField(max_length=50)                                        #登录验证
    isDelete = models.BooleanField(default=False)

    # 临时工程师 专用：姓名，密码，号码，报道日期，现住址，上级，学历，往届与应届
    #页面需要手动输入显示： 姓名，密码，号码，现住址，上级，学历，往届与应届
    reporttime = models.DateField(u"报道日期", auto_now=True ,null=True ,blank=True)
    manager = models.CharField(u"上级姓名", max_length=40, null=True, blank=True)
    howyear = models.CharField(max_length=40, choices=year ,null=True, blank=True)

    def __str__(self):
        return '%s' % self.uname  # 返回属性的显示内同

    class Meta:
        verbose_name = '员工表'
        verbose_name_plural = '员工表'
        db_table = 'user'
    @classmethod
    def createUser(cls ,uname,upasswd,ugender,uCreatedate,uupoto,uworkid,uidcard,ubirthday ,uphone,uemail,ufirstcontact,uconphone
                   ,uaddress,ueduschool,ueducation,uorigin,udepname,unit,role,jobgrade,technicalgrade,ulasttime
                   ,isDelect,utoken ,reporttime ,manager ,howyear ,isD=False):
        user = cls(uname=uname,upasswd=upasswd ,ugender=ugender ,uCreatedate=uCreatedate ,uupoto=uupoto ,uworkid=uworkid
            ,uidcard=uidcard ,ubirthday=ubirthday ,uphone=uphone ,uemail=uemail ,ufirstcontact=ufirstcontact ,uconphone=uconphone
            ,uaddress=uaddress ,ueduschool=ueduschool ,ueducation=ueducation ,uorigin=uorigin
            ,udepname=udepname ,unit=unit ,role=role ,jobgrade=jobgrade ,technicalgrade=technicalgrade
            ,ulasttime=ulasttime ,isDelect=isDelect ,utoken=utoken ,reporttime=reporttime ,manager=manager ,howyear=howyear)
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


# 组织表（TOrganization）
class TOrganization(models.Model):
    to_id = models.IntegerField(u"组id" ,primary_key=True)
    parent_to_id = models.IntegerField(u"父组id")
    org_name = models.CharField(u"组名称" ,max_length=64)
    gen_time = models.DateField(u"创建时间" ,auto_now=True)
    description = models.CharField(u"组织描述" ,max_length=200)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.org_name  # 返回属性的显示内同

    class Meta:
        verbose_name = '组织表'
        verbose_name_plural = '组织表'
        db_table = 'torganization'



# 角色表（TRole）
class TRole(models.Model):
    tr_id = models.IntegerField(u"角色id" ,primary_key=True)
    parent_tr_id = models.IntegerField(u"父级角色id")
    role_name = models.CharField(u"角色名称" ,max_length=64)
    gen_time = models.DateField(u"创建时间" ,auto_now=True)
    description = models.CharField(u"组织描述", max_length=200)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.role_name  # 返回属性的显示内同

    class Meta:
        verbose_name = '角色表'
        verbose_name_plural = '角色表'
        db_table = 'trole'

# 权限表（TRight）
class TRight(models.Model):
    tr_id = models.IntegerField(u"权限id" ,primary_key=True)
    parent_tr_id = models.IntegerField(u"父权限")
    right_name = models.CharField(u"权限名称" ,max_length=64)
    description = models.CharField(u"组织描述", max_length=200)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.right_name  # 返回属性的显示内同

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = '权限表'
        db_table = 'tright'

# 组表（TGroup）
class TGroup(models.Model):
    trr_id = models.IntegerField(u"组id" ,primary_key=True)
    parent_tg_id = models.IntegerField(u"父组id")
    group_name = models.CharField(u"组名称" ,max_length=64)
    gen_time = models.DateField(u"创建时间" ,auto_now=True)
    description = models.CharField(u"组描述", max_length=200)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.group_name  # 返回属性的显示内同

    class Meta:
        verbose_name = '组表'
        verbose_name_plural = '组表'
        db_table = 'tgroup'


# 角色权限表（TRoleRightRelation）
class TRoleRightRelation(models.Model):
    type = (
        (0, '可访问'),
        (1, '可授权'),
    )
    trr_id = models.IntegerField(u"记录标识" ,primary_key=True)
    Role_id = models.ForeignKey("TRole" ,on_delete=models.CASCADE)
    right_id = models.ForeignKey("TRight", on_delete=models.CASCADE)
    right_type = models.CharField(u"权限类型" ,max_length=32 ,choices=type ,default="可访问")
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.trr_id  # 返回属性的显示内同

    class Meta:
        verbose_name = '角色权限表'
        verbose_name_plural = '角色权限表'
        db_table = 'trolerightrelation'


# 组权限表（TGroupRightRelation）
class TGroupRightRelation(models.Model):
    type = (
        (0, '可访问'),
        (1, '可授权'),
    )
    tgr_id = models.IntegerField(u"记录标识" ,primary_key=True)
    tg_id = models.ForeignKey("TGroup" ,on_delete=models.CASCADE) # 组
    tr_id = models.ForeignKey("TRight", on_delete=models.CASCADE) # 权限
    right_type = models.CharField(u"权限类型" ,max_length=32 ,choices=type ,default="可访问")
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.tgr_id  # 返回属性的显示内同

    class Meta:
        verbose_name = '组权限表'
        verbose_name_plural = '组权限表'
        db_table = 'tgrouprightrelation'


# 组角色表（TGroupRoleRelation）
class TGroupRoleRelation(models.Model):
    tgr_id = models.IntegerField(u"记录标识", primary_key=True)
    tg_id = models.ForeignKey("TGroup", on_delete=models.CASCADE)#关联组
    tr_id = models.ForeignKey("TRole", on_delete=models.CASCADE)#关联角色
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.tgr_id  # 返回属性的显示内同

    class Meta:
        verbose_name = '组角色表'
        verbose_name_plural = '组角色表'
        db_table = 'tgrouprolerelation'

# 用户权限表（TUserRightRelation）
class TUserRightRelation(models.Model):
    type = (
        (0, '可访问'),
        (1, '可授权'),
    )
    tur_id = models.IntegerField(u"记录标识", primary_key=True)
    tu_id = models.ForeignKey("User", on_delete=models.CASCADE) #关联用户
    tr_id = models.ForeignKey("TRight", on_delete=models.CASCADE) #关联权限
    right_type = models.CharField(u"权限类型", max_length=32, choices=type, default="可访问")
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.tur_id  # 返回属性的显示内同

    class Meta:
        verbose_name = '用户权限表'
        verbose_name_plural = '用户权限表'
        db_table = 'tuserrightrelation'

# 用户角色表（TUserRoleRelation）
class TUserRoleRelation(models.Model):
    tur_id = models.IntegerField(u"记录标识", primary_key=True)
    tu_id = models.ForeignKey("User", on_delete=models.CASCADE) #关联用户
    tr_id = models.ForeignKey("TRole", on_delete=models.CASCADE) # 管理角色
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.tur_id  # 返回属性的显示内同

    class Meta:
        verbose_name = '用户角色表'
        verbose_name_plural = '用户角色表'
        db_table = 'tuserrolerelation'

# 用户组表（TUserGroupRelation）
class TUserGroupRelation(models.Model):
    tur_id = models.IntegerField(u"记录标识", primary_key=True)
    tu_id = models.ForeignKey("User", on_delete=models.CASCADE) #关联用户
    tg_id = models.ForeignKey("TGroup", on_delete=models.CASCADE) #关联组
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % self.tur_id  # 返回属性的显示内同

    class Meta:
        verbose_name = '用户组表'
        verbose_name_plural = '用户组表'
        db_table = 'tusergrouprelation'

# 操作日志表（TLog）
class TLog(models.Model):
    log_id = models.IntegerField(u"日志id" ,primary_key=True)
    tu_id = models.ForeignKey("User" ,on_delete=models.CASCADE) #操作人
    op_type = models.IntegerField(u"操作类型")
    content = models.CharField(u"操作内容" ,max_length=200)
    isDelete = models.BooleanField(default=False)
    gen_time = models.DateField(u"操作时间" ,auto_now=True)

    def __str__(self):
        return '%s' % self.content  # 返回属性的显示内同

    class Meta:
        verbose_name = '操作日志表'
        verbose_name_plural = '操作日志表'
        db_table = 'tlog'



