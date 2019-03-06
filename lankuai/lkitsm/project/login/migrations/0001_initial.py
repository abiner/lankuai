# Generated by Django 2.1.3 on 2019-02-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobgrade',
            fields=[
                ('jobID', models.IntegerField(primary_key=True, serialize=False, verbose_name='岗位ID')),
                ('jjobgrade', models.CharField(max_length=40, verbose_name='岗位级别')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '岗位级别表',
                'verbose_name_plural': '岗位级别表',
                'db_table': 'jobgrade',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('roleid', models.IntegerField(primary_key=True, serialize=False, verbose_name='角色ID')),
                ('rrole', models.CharField(max_length=40, verbose_name='角色')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '角色层级表',
                'verbose_name_plural': '角色层级表',
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='technicalGrade',
            fields=[
                ('tgid', models.IntegerField(primary_key=True, serialize=False, verbose_name='技术等级ID')),
                ('tgtechnicalgrade', models.CharField(max_length=40, verbose_name='技术等级')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '技术等级表',
                'verbose_name_plural': '技术等级表',
                'db_table': 'technicalgrade',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uname', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='姓名')),
                ('upasswd', models.CharField(max_length=40, verbose_name='系统密码')),
                ('ugender', models.BooleanField(default=True)),
                ('uCreatedate', models.DateField(auto_now_add=True, verbose_name='入职日期')),
                ('uupoto', models.ImageField(blank=True, null=True, upload_to='headportrait', verbose_name='照片')),
                ('uworkid', models.CharField(max_length=100, verbose_name='工号')),
                ('uidcard', models.CharField(max_length=100, verbose_name='身份证号码')),
                ('ubirthday', models.DateField(auto_now_add=True, verbose_name='出生年月日')),
                ('uphone', models.CharField(max_length=100, verbose_name='手机号码')),
                ('uemail', models.EmailField(max_length=254, verbose_name='邮箱地址')),
                ('ufirstcontact', models.CharField(blank=True, max_length=40, null=True, verbose_name='联系人姓名')),
                ('uconphone', models.CharField(blank=True, max_length=40, null=True, verbose_name='联系人号码')),
                ('uaddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='现住址')),
                ('ueduschool', models.CharField(blank=True, max_length=100, null=True, verbose_name='毕业院校')),
                ('ueducation', models.CharField(blank=True, max_length=20, null=True, verbose_name='学历')),
                ('uorigin', models.CharField(blank=True, max_length=20, null=True, verbose_name='籍贯')),
                ('udepname', models.CharField(blank=True, max_length=40, null=True, verbose_name='所在部门')),
                ('unit', models.CharField(blank=True, max_length=40, null=True, verbose_name='所在单位')),
                ('role', models.IntegerField(verbose_name='角色层级')),
                ('jobgrade', models.IntegerField(blank=True, null=True, verbose_name='岗位级别')),
                ('technicalgrade', models.IntegerField(blank=True, null=True, verbose_name='技术等级')),
                ('ulasttime', models.DateField(auto_now=True, verbose_name='最后修改日期')),
                ('isDelect', models.BooleanField(default=True)),
                ('utoken', models.CharField(max_length=50)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '员工表',
                'verbose_name_plural': '员工表',
                'db_table': 'user',
            },
        ),
    ]