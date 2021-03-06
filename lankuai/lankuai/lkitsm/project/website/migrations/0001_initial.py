# Generated by Django 2.1.3 on 2019-04-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='china_regionalTablet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
                ('parent', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'china',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finalTime', models.CharField(max_length=20, verbose_name='完成时间')),
                ('wOrderNo', models.CharField(max_length=50, verbose_name='工单号')),
                ('process', models.CharField(max_length=200, verbose_name='处理过程')),
                ('wState', models.CharField(max_length=20, verbose_name='工单状态')),
                ('fHandler', models.CharField(max_length=20, verbose_name='流转处理人')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '处理过程',
                'verbose_name_plural': '处理过程',
                'db_table': 'Process',
            },
        ),
        migrations.CreateModel(
            name='WorkList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billingTime', models.CharField(max_length=20, verbose_name='开单时间')),
                ('workOrderNo', models.CharField(max_length=50, verbose_name='工单号')),
                ('unitName', models.CharField(max_length=20, verbose_name='单位名称')),
                ('clientName', models.CharField(max_length=20, verbose_name='客户姓名')),
                ('clientPho', models.CharField(max_length=50, verbose_name='客户电话')),
                ('clientAddress', models.CharField(max_length=100, verbose_name='客户位置')),
                ('faultClass', models.CharField(max_length=20, verbose_name='故障大类')),
                ('faultClasss', models.CharField(max_length=20, verbose_name='故障小类')),
                ('faultDetail', models.CharField(max_length=20, verbose_name='故障明细')),
                ('incidentCla', models.CharField(max_length=20, verbose_name='事件分类')),
                ('incidentRank', models.CharField(max_length=20, verbose_name='事件级别')),
                ('incidentState', models.CharField(max_length=20, verbose_name='事件状态')),
                ('incidentTheme', models.CharField(max_length=100, verbose_name='事件主题')),
                ('incidentDescribe', models.CharField(max_length=100, verbose_name='事件描述')),
                ('manageCourse', models.CharField(max_length=200, verbose_name='处理过程')),
                ('creator', models.CharField(max_length=20, verbose_name='创建人')),
                ('workState', models.CharField(max_length=20, verbose_name='工单状态')),
                ('flowHandler', models.CharField(max_length=20, verbose_name='流转处理人')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '工单系统',
                'verbose_name_plural': '工单系统',
                'db_table': 'WorkList',
            },
        ),
    ]
