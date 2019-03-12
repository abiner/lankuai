from django.shortcuts import render, redirect
from .models import User ,Role ,Jobgrade ,technicalGrade
from django import forms
from website.models import Departments ,UnitName
from workfolw.models import Workflow ,managerApproval ,Notice ,Classify
from repairANDbuyer.models import failureMessages ,Goods ,purchaseApplyFor ,goodsCost ,managerConsent ,Consignee
import os ,time ,random

# 定义表单模型
class UserloginForm(forms.Form):
    username = forms.CharField(label='用户名 :', max_length=50)
    password = forms.CharField(label='密码 :', widget=forms.PasswordInput())


#login 判断账号密码，进入index
def login(request):
    #不能同时在线两个同一账号
    #if request.session.get('is_login', None):
        #return redirect('/login')
    if request.method == "POST":
        uf = UserloginForm(request.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(uname__exact=username, upasswd__exact=password).filter(isDelect=True)
            if not user:
                message = "账号密码不正确！或账号已注销！"
                # 登录失败跳转回原来登录页面
                return render(request, 'login/login.html', {'message': message})
            else:
                # 如果当前登录用户为 0 或 1 则传数据为hrworkfolw ，如果为 3 或 4 则传数据为 mrworkfolw
                # 当前登录用户层级为？，显示？
                user = User.objects.get(uname=username)

                # 保存session信息,是否登录，登录用户名
                request.session["is_login"] = True
                request.session["username"] = user.uname

                return redirect('/index')
                #return render(request ,"login/index.html")
    return render(request, 'login/login.html')

import datetime
from repairANDbuyer.models import State
#根据用户信息，显示相关信息
def index(request):
    username = request.session['username']
    print(username ,"当前登录用户")
    user = User.objects.get(uname=username)
    if user.udepname:
        dep = Departments.objects.get(depname=user.udepname)
        print("dep.id:", dep.id, "每个人登录后都会显示部门ID，此部门ID对应事件层级==================================")

    #公告 ，任何人都可以看到 noticeList 是多条数据，我们需要把多条数据里 audit=True 的取出来
    noticeList = Notice.objects.all().filter(audit=True).order_by("-issuetime")[:5]

    role3noticeList = Notice.objects.all().filter(audit=False).order_by("-issuetime")[:5]

    if user.role == 0:  # 工程师
        role = 0
        print(user.role ,"是不是0呢？")
        # 工作流 ，取出自己的申请表单
        lookOverList = Workflow.objects.filter(wname=username).order_by("wbegin")[:5]

        #采购 ，申请人为自己，并到了收货，你需要确认收货时间
        pafList = purchaseApplyFor.objects.filter(pname=username).filter(pcourse=3)
        print(pafList ,"看看有没有单")

        return render(request ,'login/index.html', {'username': username, "lookOverList": lookOverList, "details": "通过"
                                                 ,"myrole": "hrworkfolw", "role": role, "what": "none" ,"pafList":pafList
                                                ,"noticeList":noticeList ,"display":"none"})

    elif user.role == 1:  # 部门主管暂时有黄唐
        role = 1
        # 取出自己的申请表单
        lookOverList = Workflow.objects.filter(wname=username)
        e2List = failureMessages.objects.filter(eventlevel=1)

        #如果登录的是采购部的部门经理，则显示采购层级为1的数值
        if username == "唐涛":
            pafList = purchaseApplyFor.objects.filter(pcourse=1)
            print(pafList ,"是否有东西------------------------------")
            return render(request, 'login/index.html', {'username': username, "myrole": "hrworkfolw"
                , "lookOverList": lookOverList, "e2List": e2List, "role": role ,"pafList":pafList ,"noticeList":noticeList ,"display":"none"})

        return render(request ,'login/index.html', {'username': username, "myrole": "hrworkfolw"
            ,"lookOverList": lookOverList ,"e2List":e2List ,"role":role ,"noticeList":noticeList ,"display":"none"})

    elif user.role == 2:  # 部门经理
        #工作流  取出名字为自己的申请表单
        role = 2
        lookOverList = Workflow.objects.filter(wname=username)
        print("user.role == 2:我的角色等级================================================")

        #工作流  审批别人的单
        approvalPending = Workflow.objects.filter(hierarchy0=dep.id)  # 只显示事件层级为本部门ID
        print("已知我的角色为部门经理，此时的部门ID是：------------------------" ,dep.id ,"-----------------------------------")
        print(approvalPending, "wf======================表示取出所有事件在dep.id的申请单============================")

        #维修审批暂只给小郑 ,把申请数据，和申请数据对应的报价表展示出来 #采购审批，暂给小郑
        if username == "郑敏龙":
            print("这是维修审批----------------------------------------")
            e2List = failureMessages.objects.filter(eventlevel=2)

            print("这是采购审批----------------------------------------")
            pafList = purchaseApplyFor.objects.filter(pcourse=2)


            return render(request, 'login/index.html',
                          {'username': username, "lookOverList": lookOverList, "approvalPending": approvalPending
                              , "details": "未审批", "myrole": "mrworkfolw","e2List":e2List ,"role":role ,"pafList":pafList
                              ,"noticeList":noticeList ,"display":"none" })
        elif user.udepname == "人事部":
            uList = []
            now = datetime.datetime.now()
            print(now ,"现在时间 ,及各式" ,type(now))
            strnow = now.strftime("%m-%d")          #现在的时间是str格式
            userList = User.objects.all()
            for item in userList:
                birthday = item.ubirthday
                print(birthday ,"这个同学的生日是多少啊" ,item.uname)
                strbirthday = birthday.strftime("%m-%d")
                userbirthday = datetime.datetime.strptime(strbirthday ,"%m-%d")
                nowtime = datetime.datetime.strptime(strnow ,"%m-%d")
                timecha = userbirthday - nowtime
                print(type(timecha) ,"讲道理，这是个数字" ,type(timecha.days) ,timecha.days)
                inttimecha = timecha.days
                if inttimecha <= 30 and inttimecha >= 0:
                    uList.append(item)
            return render(request, 'login/index.html' ,{'username': username, "lookOverList": lookOverList
                                   ,"approvalPending": approvalPending , "details": "未审批", "myrole": "mrworkfolw"
                                    , "role": role, "noticeList": noticeList , "display": "none" ,"uList":uList})

        else:
            return render(request, 'login/index.html',
                          {'username': username, "lookOverList": lookOverList, "approvalPending": approvalPending
                              , "details": "未审批", "myrole": "mrworkfolw",  "role": role ,"noticeList": noticeList
                              , "display": "none"})
        #如果登录用户是人事部经理




    elif user.role == 3:  # 总经理
        role = 3
        # 取出自己的申请表单
        lookOverList = Workflow.objects.filter(wname=username)
        print("user.role == 3:================================================")
        print("dep.id:", dep.id, "这里是总经理的部门，dep.id是多少呢")
        approvalPending = Workflow.objects.all().filter(hierarchy0=dep.id)
        return render(request ,'login/index.html' ,{'username': username, "approvalPending": approvalPending, "myrole": "mrworkfolw",
                                   'lookOverList': lookOverList ,"role":role ,"noticeList":noticeList ,"role3noticeList":role3noticeList ,"display":"block"})


# 注册界面
def register(request):
    roleList = Role.objects.all()
    depList = Departments.objects.all()
    unitname = UnitName.objects.all()
    jobList = Jobgrade.objects.all()


    return render(request, 'login/register.html', {'title': '注册' , "roleList":roleList , "depList":depList , "unitname":unitname ,"jobList":jobList})

from django.conf import settings
def adduser(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        upasswd = request.POST.get("upasswd")
        ugender = request.POST.get("ugender")
        uCreatedate = request.POST.get("uCreatedate")
        print(type(uCreatedate) ,"入职日期-----------------------的类型")

        uworkid = request.POST.get("uworkid")
        uidcard = request.POST.get("uidcard")
        uphone = request.POST.get("uphone")
        uemail = request.POST.get("uemail")
        ufirstcontact = request.POST.get("ufirstcontact")
        uconphone = request.POST.get("uconphone")
        uaddress = request.POST.get("uaddress")
        ueduschool = request.POST.get("ueduschool")
        ueducation = request.POST.get("ueducation")
        uorigin = request.POST.get("uorigin")

        job = request.POST.get("jobgrade")# 岗位级别 #实习0，试用1，正式2	，1星3，2星4，3星5，4星6，5星7
        jobg = Jobgrade.objects.get(jjobgrade=job)
        print(type(jobg.jobID) ,"jobg.jobID------------------的类型")
        jobgrade = jobg.jobID

        udepname = request.POST.get("udepname")
        unit = request.POST.get("unit")
        ubirthday = request.POST.get("ubirthday")
        print(ubirthday ,"生日日期--------------------------------")
        # 直接获取
        r = request.POST.get("role")                            #r  字符串
        print(r ,"这是角色-------------------------")
        # 非临时工注册 为null
        reporttime = ""
        manager = ""
        howyear = ""

        if r:
            Rrole = Role.objects.get(rrole=r)
            print(Rrole ,"Rrole,这是角色实例，必须得有")
            role = Rrole.roleid
            print(type(Rrole.roleid) ,"Rrole.roleid---------------的类型")

            # 技术等级等于1，默认等于1  技术等级：12345
            technicalgrade = 1
            ulasttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            print(ulasttime ,"当前时间，就是修改时间--------------------" ,type(ulasttime))
            # 是否在职
            isDelect = True
            # utoken
            token = time.time() + random.randrange(1 ,100000)
            utoken = str(token)
            #上传图片
            uupoto = request.FILES["uupoto"]
            print(type(uupoto) ,"照片是什么类型-------------------------")
            print(uname,upasswd,ugender,uCreatedate,uupoto,uworkid,uidcard,ubirthday ,uphone,uemail,ufirstcontact,uconphone
                   ,uaddress,ueduschool,ueducation,uorigin,udepname,unit,role,jobgrade,technicalgrade,ulasttime
                   ,isDelect,utoken ,reporttime ,manager ,howyear)
            user = User.createUser(uname,upasswd,ugender,uCreatedate,uupoto,uworkid,uidcard,ubirthday ,uphone,uemail,ufirstcontact,uconphone
                   ,uaddress,ueduschool,ueducation,uorigin,udepname,unit,role,jobgrade,technicalgrade,ulasttime
                   ,isDelect,utoken ,reporttime ,manager ,howyear)

            user.save()
            user.uCreatedate = uCreatedate
            user.ubirthday = ubirthday
            user.save()
            if uupoto:
                fname = settings.MEDIA_ROOT + "/noticeImg/" + uupoto.name
                with open(fname ,"wb") as pic:
                    for item in uupoto.chunks():
                        pic.write(item)

            return redirect('/register/')




def temporaryuser(request):

    return render(request ,"login/temporaryuser.html")

def addtemporaryuser(request):
    print("我需要确定你来到了--------------addtemporaryuser------------")
    if request.method == "POST":
        uname = request.POST.get("uname")
        upasswd = request.POST.get("upasswd")
        uphone = request.POST.get("uphone")
        uaddress = request.POST.get("uaddress")
        ugender = request.POST.get("ugender")
        manager = request.POST.get("manager")
        ueducation = request.POST.get("ueducation")
        howyear = request.POST.get("howyear")
        uCreatedate = "1900-01-01"
        uupoto = ""
        uworkid = ""
        uidcard = ""
        ubirthday = "1900-01-01"
        uemail = ""
        ufirstcontact = ""
        uconphone = ""
        ueduschool = ""
        uorigin = ""
        udepname = ""
        unit = ""
        role = 0
        jobgrade = 0
        technicalgrade = 1
        ulasttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        reporttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        isDelect = False
        utoken = time.time() + random.randrange(1 ,100000)

        print(uname, upasswd, ugender, uCreatedate, uupoto, uworkid, uidcard, ubirthday, uphone,
                               uemail, ufirstcontact, uconphone
                               , uaddress, ueduschool, ueducation, uorigin, udepname, unit, role, jobgrade,
                               technicalgrade, ulasttime
                               , isDelect, utoken, reporttime, manager, howyear)

        user = User.createUser(uname, upasswd, ugender, uCreatedate, uupoto, uworkid, uidcard, ubirthday, uphone,
                               uemail, ufirstcontact, uconphone
                               , uaddress, ueduschool, ueducation, uorigin, udepname, unit, role, jobgrade,
                               technicalgrade, ulasttime
                               , isDelect, utoken, reporttime, manager, howyear)
        user.save()
        return redirect('/login/')





from django.core.paginator import Paginator
#人事停用账户
def logoutuser(request ,pageid):
    userList = User.objects.all().filter(isDelect=True)
    paginator = Paginator(userList ,5)
    page = paginator.page(pageid)

    return render(request ,"login/logoutuser.html" ,{"userList":page})

#重置密码操作
def resetpsswd(request ,pageid):
    path = request.path
    print(path ,"-------最原始的路由----------------------")#   /logoutuser/12345679/
    newpath = path[12:20]
    print(newpath ,"新的路由-----------------------------")
    user = User.objects.get(uworkid=newpath)
    user.upasswd = "123456"
    user.save()
    return redirect('/logoutuser/1')


# 离职操作（注销账户）
def subtractuser(request ,pageid):
    path = request.path
    print(path ,"-------最原始的路由----------------------")#   /logoutuser/12345679/
    newpath = path[12:20]
    print(newpath ,"新的路由-----------------------------")
    user = User.objects.get(uworkid=newpath)
    user.isDelect = False
    user.save()
    return redirect('/logoutuser/1')

#注销
def logout(request):
    del request.session['is_login']
    #del request.session['user_id']
    del request.session['username']
    return redirect("/login/")


# 主页，更多 more
def more(request):

    return render(request ,"login/more.html")
'''
    username = request.session["username"]
    user = User.objects.get(uname=username)
    # 采购 ，申请人为自己，并到了收货，你需要确认收货时间
    pafList = purchaseApplyFor.objects.filter(pname=username).filter(pcourse=3)
    dep = Departments.objects.get(depname=user.udepname)
    noticeList = Notice.objects.all().filter(audit=True).order_by("-issuetime")[:5]
    role3noticeList = Notice.objects.all().filter(audit=False).order_by("-issuetime")[:5]
    if user.role == 0 :
        lookOverList = Workflow.objects.filter(wname=username).order_by("wbegin")[:5]


        return render(request, "login/more.html", {"username": username ,"pafList":pafList ,"noticeList":noticeList ,"lookOverList":lookOverList })

    elif user.role == 1 :
        lookOverList = Workflow.objects.filter(wname=username)
        e2List = failureMessages.objects.filter(eventlevel=1)
        if username == "唐涛":
            pafList = purchaseApplyFor.objects.filter(pcourse=1)

            return render(request, "login/more.html",
                          {"username": username, "pafList": pafList, "noticeList": noticeList,
                           "lookOverList": lookOverList ,"e2List":e2List})


    elif user.role == 2 :
        lookOverList = Workflow.objects.filter(wname=username)
        approvalPending = Workflow.objects.filter(hierarchy0=dep.id)  # 只显示事件层级为本部门ID
        if username == "郑敏龙":
            print("这是维修审批----------------------------------------")
            e2List = failureMessages.objects.filter(eventlevel=2)

            print("这是采购审批----------------------------------------")
            pafList = purchaseApplyFor.objects.filter(pcourse=2)
            return render(request, "login/more.html",
                          {"username": username, "pafList": pafList, "noticeList": noticeList,
                           "lookOverList": lookOverList ,"e2List":e2List ,"approvalPending":approvalPending})

    elif user.role == 3 :
        lookOverList = Workflow.objects.filter(wname=username)
        approvalPending = Workflow.objects.all().filter(hierarchy0=dep.id)
        return render(request ,"login/more.html" ,{"username":username ,"role3noticeList":role3noticeList
            ,"lookOverList":lookOverList ,"approvalPending":approvalPending})
'''


