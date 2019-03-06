from django.db import models


# 展示视频，存取视频
class Video(models.Model):
    uploader = models.CharField(r'上传者', max_length=20)
    imgpath = models.ImageField(upload_to='img')  #
    uppath = models.FileField(upload_to='uppath')  # 定义上传路径
    describe = models.CharField(r'标题', max_length=100)
    uploaddate = models.DateField(r'上传日期', auto_now_add=True)
    kind = models.CharField(r'所属种类', max_length=20)
    score = models.IntegerField(r'观看该影片可得分数')
    haveseen = models.CharField(r'看过没呀', max_length=20, default="未睇过")
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.uploader
    class Meta:
        verbose_name = '展示存取视频'
        verbose_name_plural = '展示存取视频'
        db_table = 'video'
    @classmethod
    def createvideo(cls, upl, img, upp, des, uploadd, ki, isD=False):
        v = cls(uploader=upl, imgpath=img, uppath=upp, describe=des, uploaddate=uploadd, kind=ki)
        return v

#分数表
class Grade(models.Model):
    gname = models.CharField(r'用户', max_length=20)
    gid = models.IntegerField(r'视频ID')
    gtotal = models.IntegerField(r'总分数')
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gtotal
    class Meta:
        verbose_name = '计算分数'
        verbose_name_plural = '计算分数'
        db_table = 'Grade'
    @classmethod
    def creategrade(cls ,name ,id ,total ,isD = False):
        g = cls(gname=name ,gid=id ,gtotal=total)
        return g

#谁看过
class Isee(models.Model):
    iname = models.CharField(r'用户', max_length=20)
    igid = models.IntegerField(r'视频ID')
    iseetime = models.DateField(r'观看时间' ,auto_now_add=True)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.iname
    class Meta:
        verbose_name = '睇过未'
        verbose_name_plural = '睇过未'
        db_table = 'Isee'
    @classmethod
    def createisee(cls ,name ,gid ,seetime ,isD = False):
        isee = cls(iname=name ,igid=gid ,iseetime=seetime)
        return isee
