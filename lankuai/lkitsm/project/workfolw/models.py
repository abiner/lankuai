from django.db import models
#员工申请表
class Workflow(models.Model):
    wid = models.CharField(r'流水号' ,max_length=40)
    wname = models.CharField(r'姓名', max_length=40)
    wdepname = models.CharField(r'运维组',max_length=40)
    wapplytype = models.CharField(r'申请类型' ,max_length=40)
    wbegin = models.CharField(r'开始日期' ,max_length=20)
    wfinish = models.CharField(r'结束日期' ,max_length=20)
    wreasons = models.CharField(r'事由' ,max_length=300)
    hierarchy0 = models.IntegerField(r'事件层级')#申请表单进度到哪了 ,0驳回,100同意，默认为本部门编号
    isDelete = models.BooleanField(default=False)

    class Meta:
        verbose_name = '工作流'
        verbose_name_plural = '工作流'
        db_table = 'Workflow'
    @classmethod
    def createWorkflow(cls ,wid ,name ,depname ,applytype ,begin ,finish ,reasons ,hierarchy0,isD = False):
        workflow = cls(wid=wid ,wname=name ,wdepname=depname ,wapplytype=applytype ,wbegin=begin ,wfinish=finish ,wreasons=reasons ,hierarchy0=hierarchy0)
        return workflow

#manager审批表
class managerApproval(models.Model):
    maid = models.CharField(r'流水号' ,max_length=40)
    approvaler = models.CharField(r'审批人' ,max_length=40)
    approvalopinion = models.CharField(r'审批意见' ,max_length=400)
    approvaltime = models.CharField(r'审批时间' ,max_length=20)
    isDelete = models.BooleanField(default=False)

    class Meta:
        verbose_name = '经理审批表'
        verbose_name_plural = '经理审批表'
        db_table = 'managerApproval'
    @classmethod
    def createmanagerApproval(cls ,id ,approval ,approvalopinion ,approvalt,isD = False):
        mapproval = cls(maid=id ,approvaler=approval ,approvalopinion = approvalopinion ,approvaltime=approvalt)
        return mapproval

#人事公告表
class Notice(models.Model):
    moticeid = models.CharField(r"公告ID" ,max_length=40)
    nname = models.CharField(r"作者" ,max_length=20)
    headline = models.CharField(r"文章标题" ,max_length=30)
    issuetime = models.CharField(r"发布时间" ,max_length=30)
    nclassify = models.CharField("所有栏目",max_length=30)      #需要什么栏目自己写数据库建起来
    audit = models.BooleanField(default=False)                  #总经理有权审核是否发布
    picture = models.ImageField(upload_to='noticeImg' ,verbose_name="图片文件" ,null=True ,blank=True)
    article = models.TextField(r"文章内容")
    isDelete = models.BooleanField(default=False)

    class Meta:
        verbose_name = '人事公告表'
        verbose_name_plural = '人事公告表'
        db_table = 'notice'
    @classmethod
    def createnotice(cls ,moticeid ,nname,headline ,issuetime ,nclassify ,audit, picture ,article ,isD = False):
        notict = cls(moticeid=moticeid ,nname = nname ,headline=headline ,issuetime=issuetime ,nclassify=nclassify ,audit=audit ,picture=picture ,article=article)
        return notict

#栏目表
class Classify(models.Model):
    cid = models.IntegerField(r"栏目ID")
    classify = models.CharField(r"所在栏目" ,max_length=30)
    isDelete = models.BooleanField(default=False)
    class Meta:
        verbose_name = '栏目表'
        verbose_name_plural = '栏目表'
        db_table = 'classify'



