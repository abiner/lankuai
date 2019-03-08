# Generated by Django 2.1.3 on 2019-03-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField(verbose_name='栏目ID')),
                ('classify', models.CharField(max_length=30, verbose_name='所在栏目')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '栏目表',
                'verbose_name_plural': '栏目表',
                'db_table': 'classify',
            },
        ),
        migrations.CreateModel(
            name='managerApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maid', models.CharField(max_length=40, verbose_name='流水号')),
                ('approvaler', models.CharField(max_length=40, verbose_name='审批人')),
                ('approvalopinion', models.CharField(max_length=400, verbose_name='审批意见')),
                ('approvaltime', models.CharField(max_length=20, verbose_name='审批时间')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '经理审批表',
                'verbose_name_plural': '经理审批表',
                'db_table': 'managerApproval',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moticeid', models.CharField(max_length=40, verbose_name='公告ID')),
                ('nname', models.CharField(max_length=20, verbose_name='作者')),
                ('headline', models.CharField(max_length=30, verbose_name='文章标题')),
                ('issuetime', models.CharField(max_length=30, verbose_name='发布时间')),
                ('nclassify', models.CharField(max_length=30, verbose_name='所有栏目')),
                ('audit', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='noticeImg', verbose_name='图片文件')),
                ('article', models.TextField(verbose_name='文章内容')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '人事公告表',
                'verbose_name_plural': '人事公告表',
                'db_table': 'notice',
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wid', models.CharField(max_length=40, verbose_name='流水号')),
                ('wname', models.CharField(max_length=40, verbose_name='姓名')),
                ('wdepname', models.CharField(max_length=40, verbose_name='运维组')),
                ('wapplytype', models.CharField(max_length=40, verbose_name='申请类型')),
                ('wbegin', models.CharField(max_length=20, verbose_name='开始日期')),
                ('wfinish', models.CharField(max_length=20, verbose_name='结束日期')),
                ('wreasons', models.CharField(max_length=300, verbose_name='事由')),
                ('hierarchy0', models.IntegerField(verbose_name='事件层级')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '工作流',
                'verbose_name_plural': '工作流',
                'db_table': 'Workflow',
            },
        ),
    ]
