# Generated by Django 2.1.3 on 2019-03-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20, verbose_name='用户')),
                ('gid', models.IntegerField(verbose_name='视频ID')),
                ('gtotal', models.IntegerField(verbose_name='总分数')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '计算分数',
                'verbose_name_plural': '计算分数',
                'db_table': 'Grade',
            },
        ),
        migrations.CreateModel(
            name='Isee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=20, verbose_name='用户')),
                ('igid', models.IntegerField(verbose_name='视频ID')),
                ('iseetime', models.DateField(auto_now_add=True, verbose_name='观看时间')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '睇过未',
                'verbose_name_plural': '睇过未',
                'db_table': 'Isee',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploader', models.CharField(max_length=20, verbose_name='上传者')),
                ('imgpath', models.ImageField(upload_to='img')),
                ('uppath', models.FileField(upload_to='uppath')),
                ('describe', models.CharField(max_length=100, verbose_name='标题')),
                ('uploaddate', models.DateField(auto_now_add=True, verbose_name='上传日期')),
                ('kind', models.CharField(max_length=20, verbose_name='所属种类')),
                ('score', models.IntegerField(verbose_name='观看该影片可得分数')),
                ('haveseen', models.CharField(default='未睇过', max_length=20, verbose_name='看过没呀')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '展示存取视频',
                'verbose_name_plural': '展示存取视频',
                'db_table': 'video',
            },
        ),
    ]
