# 工单系统，流转人 = 当前登录用户.运维组所有成员


from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django import forms
from django.db import models

import time
from .models import UnitName ,Departments ,china_regionalTablet
import json
from datetime import datetime
from workfolw.models import Workflow ,managerApproval
from login.models import User
from repairANDbuyer.models import failureMessages

#上级处理工作流
def mdispose(request ,wid):
    path = request.path
    print(path)
    newpath = path[1:15]
    print(newpath)
    workflow = Workflow.objects.get(wid=newpath)
    #所有部门信息
    dempList = Departments.objects.all()
    #取出当前登录用户部门的dname 使它隐藏
    username = request.session['username']
    demp = Departments.objects.get(manager=username)
    print(demp ,"demp=================================")
    dn = demp.dname
    print(dn ,"dn=====================================")

    # 取出部门经理审批意见，按时间排序
    managerAList = managerApproval.objects.filter(maid=newpath).order_by("approvaltime")
    if not managerAList:
        print("这里是还没有审批信息====================================================")
        return render(request, "workfolw/mdispose.html",
                      {"title": "处理工作流", "workflow": workflow, "dempList": dempList, "dn": dn})
    else:
        for item in managerAList:
            return render(request, "workfolw/mdispose.html",
                          {"title": "处理工作流", "workflow": workflow, "dempList": dempList, "dn": dn ,"managerAList":managerAList})


#上级工作流保存与走向
def addmdispose(request):
    if "tijiao" in request.POST:
        print("yes-----------------------tijiao提交-------------------yes")


    #当前登录用户，审批人
    username = request.session['username']
    print(username, 'username-----------------------')
    #审批人意见
    mopinion = request.POST.get('mopinion')
    print(mopinion ,"-----------------------------")

    #申请人流水号：
    wid = request.POST.get('wid')
    print(wid ,"wid================================")

    #审批时间
    approvaltime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print(approvaltime ,"审批时间-----------------------")

    #保存工作流
    ma = managerApproval.createmanagerApproval(wid ,username ,mopinion ,approvaltime)
    ma.save()


    # 通过流水号取得申请人：因为是通用的，所以放出来
    wuser = Workflow.objects.get(wid=wid)
    #驳回申请，0是驳回
    if "bohui" in request.POST:
        print("bohui0000000000000000000000bohui驳回00000000000000000000000000")
        # 修改层级
        wuser.hierarchy0 = 0
        wuser.save()
        return redirect('/index')

    #从前台取出name属性，告诉每个button分别做什么事
    #流转是通过部门ID来决定的，部门不能超过批准数值
    demp = Departments.objects.all()
    for index in demp:
        if index.dname in request.POST:
            dep = Departments.objects.get(depname=index.depname)
            wuser.hierarchy0 = dep.id
            wuser.save()
            return redirect('/index')

        #批准审批，100是批准
    if "pizhun" in request.POST:
        print("bohui0000000000000000000000bohui批准00000000000000000000000000")
        # 修改层级
        wuser.hierarchy0 = 100
        wuser.save()
        return redirect('/index')


#我创办的工单
def Iestablishpage(request ,pageid):
    #等钱登录人名字所有工单
    username = request.session['username']
    iestablish = WorkList.objects.all().filter(creator = username)[0:3]

    paginator = Paginator(iestablish, 6)
    page = paginator.page(pageid)

    return render(request, 'website/Iestablish.html', {'title': '我创办的工单' ,"username":username , 'iestablish':page})

#我的待办
def delaypage(request ,pageid):
    #当前登录用户姓名
    username = request.session['username']
    delay = WorkList.objects.all().filter(creator = username).filter(workState = '跟进')

    paginator = Paginator(delay, 10)
    page = paginator.page(pageid)

    return render(request, 'website/delay.html', {'title': '我的待办' ,"username":username ,'delay':page})
#---继续处理工单
def goon(request):
    # ---使用session取到当前登录用户
    username = request.session['username']
    # user:当前登录用户
    user = User.objects.get(uname=username)

    # 当前时间
    finalTime = str(time.strftime("%m-%d/%H:%M"))
    # 流转人allUser,默认开单人，同组人全显示
    # 登录用户所在的组
    print(user.unit ,"登录用户所在的组")
    allUser = User.objects.all().values("uname").filter(unit=user.unit)


    gongdanhao = str(request.path)

    if gongdanhao[0:7] == '/delay/':#我的代办
        newpath = gongdanhao[7:]  # /delay/1sj20190104183422    /allWorkOrder/1sj20190104183422
        what = ''
        thisON = Process.objects.all().filter(wOrderNo = newpath)

        sel = WorkList.objects.get(workOrderNo=newpath)
        print(sel)

        return render(request, 'website/goon.html', {'sel':sel , 'finalTime':finalTime , 'username':username , 'allUser':allUser , 'thisON':thisON , 'what':what})


    elif gongdanhao[0:14] == '/allWorkOrder/':#全部工单
        newpath = gongdanhao[14:]
        what = 'none'
        thisON = Process.objects.all().filter(wOrderNo = newpath)

        sel = WorkList.objects.get(workOrderNo=newpath)
        print(sel)

        return render(request, 'website/goon.html', {'sel':sel , 'finalTime':finalTime , 'username':username , 'allUser':allUser , 'thisON':thisON , 'what':what})


    elif gongdanhao[0:12] == '/Iestablish/':#我的工单
        newpath = gongdanhao[12:]
        what = 'none'

        sel = WorkList.objects.get(workOrderNo=newpath)
        print(sel)

        thisON = Process.objects.all().filter(wOrderNo = newpath)

        return render(request, 'website/goon.html', {'sel':sel , 'finalTime':finalTime , 'username':username , 'allUser':allUser , 'thisON':thisON , 'what':what})


from .models import Process
#添加工单数据addProcess
def addProcess(request):
    if request.method == 'POST':
        finalTime = request.POST.get('finalTime')
        print(finalTime ,'====================finalTime：最后时间====================')
        gongdanhao = request.POST.get('gongdanhao')
        print(gongdanhao ,'gongdanhao-------------------------------------------')

        process = request.POST.get('manageCourse')
        print(process,"处理过程")

        workStateList = request.POST.get('workStateList')
        print(workStateList,'--------workStateList--------workStateList-------------workStateList--------')

        if workStateList == '关闭':
            WorkList.objects.filter(workOrderNo = gongdanhao).update(workState = '关闭')
            print(workStateList, '--------workStateList--------workStateList-------------workStateList--------')
        else:
            print('还是跟进还是跟进还是跟进还是跟进还是跟进还是跟进还是跟进还是跟进')

        flowHandler = request.POST.get('flowHandler')
        print(flowHandler ,'flowHandler：流转处理人')
        addp = Process.createProcess(finalTime ,gongdanhao ,process ,workStateList ,flowHandler)
        print(finalTime ,gongdanhao ,process ,workStateList ,flowHandler)
        addp.save()

        return redirect('/delay/1')




from django.core.paginator import Paginator
from django.http import HttpResponse ,JsonResponse
#所有工单
def allpage(request ,pageid):
    username = request.session["username"]

    search = request.POST.get("search")
    error_msg = "没有相关工单"
    if not search:
        error_msg = "请输入搜索关键字"
        allWList = WorkList.objects.all()
        paginator = Paginator(allWList, 10)
        page = paginator.page(pageid)
        return render(request, 'website/allWorkOrder.html', {'title': '全部工单信息' ,"username":username , "allworkorder":page})
    else:
        allWList = WorkList.objects.filter(workState__icontains=search)
        paginator = Paginator(allWList, 10)
        page = paginator.page(pageid)
        return render(request, 'website/allWorkOrder.html',
                      {'title': '全部工单信息', "username": username, "allworkorder": page})


import random
#工单系统
def writeWorkList(request):
    if request.method == 'POST':
        # 从前端取parent
        parent = request.POST.get('parent')
        # 从前端取level
        level = request.POST.get('level')
        # parent,level相等的数据全部取出存为citys,可是没有
        citys = china_regionalTablet.objects.filter(parent=parent, level=level).all()
        dict_city = []
        # citys是一组数据，每个city的ID，name ，取出来存为一组temp，一组temp存到字典
        for city in citys:
            temp = []
            temp.append(city.id)
            temp.append((city.name))
            dict_city.append(temp)
        # dict_city是获取到了，把dict_city传到前端
        return HttpResponse(json.dumps({"dict_city": dict_city}))
    # ---使用session取到当前登录用户
    username = request.session['username']
    nowTime = str(time.strftime("%m-%d/%H:%M"))
    print(nowTime, 'nowTime:当前时间')

    # user:当前登录用户
    user = User.objects.get(uname=username)
    print(user, '当前登录用户')

    # 当前时间：
    nowtime = str(time.strftime("%m%d%H%M"))+str(random.randrange(1 ,1000))
    print(user.unit ,"当前用户所在单位-------------------  -----------------")

    #当前单位 的简称                                                               你告诉我你取当前单位干哈？
    unit = UnitName.objects.get(unitName=user.unit)
    print(unit.uname)

    #当前单位简称
    print(unit.uname ,'当前单位简称------------------------------------------')
    workOrderNo = unit.uname + nowtime

    # 单位名称
    unitName = user.unit
    print(unitName ,'单位名称------------------')

    # 流转人allUser,默认开单人，同组人全显示
    allUser = User.objects.all().filter(unit=user.unit)
    print(allUser[0] ,'有哪些可流转人')


    return render(request, 'website/writeWorkList.html', {'nowTime': nowTime, 'unitName': unitName
            , 'username': username, 'workOrderNo': workOrderNo ,'allUser':allUser})


from .models import WorkList
from django.contrib import messages
def addWriteWorkList(request):
    if request.method == 'POST':
        billingTime = request.POST.get('billingTime')
        gongdanhao = request.POST.get('gongdanhao')
        unitName = request.POST.get('unitName')
        clientName = request.POST.get('clientName')
        clientPho = request.POST.get('clientPho')
        clientAddress = request.POST.get('clientAddress')
        faultClassList = request.POST.get('faultClassList')
        faultClasssList = request.POST.get('faultClasssList')
        faultDetailList = request.POST.get('faultDetailList')
        incidentClaList = request.POST.get('incidentClaList')
        incidentRankList = request.POST.get('incidentRankList')
        incidentStateList = request.POST.get('incidentStateList')
        incidentTheme = request.POST.get('incidentTheme')
        incidentDescribe = request.POST.get('incidentDescribe')
        manageCourse = request.POST.get('manageCourse')
        creator = request.POST.get('creator')
        print(creator ,'===============================creatorcreatorcreatorcreator=================================')
        workStateList = request.POST.get('workStateList')
        flowHandler = request.POST.get('flowHandler')
        workWM = WorkList.createWorkList(billingTime, gongdanhao, unitName, clientName, clientPho,
                        clientAddress ,faultClassList, faultClasssList, faultDetailList, incidentClaList,
                        incidentRankList , incidentStateList, incidentTheme, incidentDescribe, manageCourse,
                        creator ,workStateList, flowHandler)
        print(billingTime, gongdanhao, unitName, clientName, clientPho,
                        clientAddress ,faultClassList, faultClasssList, faultDetailList, incidentClaList,
                        incidentRankList , incidentStateList, incidentTheme, incidentDescribe, manageCourse,
                        creator ,workStateList, flowHandler)
        workWM.save()
        messages.add_message(request, messages.SUCCESS, 'Hello world.')
        return redirect('/writeWorkList')




# 注销系统
from django.contrib import auth


def logout(request):
    del request.session['is_login']
    #del request.session['user_id']
    del request.session['username']

    return redirect("/login")


@login_required
def nav(request):
    return render(request, 'nav.html')
    # return HttpResponse("Sunck is a good man")



def form(request):
    return render(request, 'forms.html')


@login_required
def main(request):
    return render_to_response(request, 'main.html')


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def table(request):
    return render(request, 'table.html')


def hrwfolw(request):
    # return HttpResponse("Sunck is a good man")
    return render(request, 'workfolw/hrworkfolw.html')


def hrms(request):
    # return HttpResponse("Sunck is a good man")
    return render(request, 'hrms.html')


54


def media(request):
    # return HttpResponse("Sunck is a good man")
    return render(request, 'media/../templates/media.html')


def testyem(request):
    # 业务逻辑代码
    return HttpResponse("OK")



def ithelpdesk(request):
    # 业务逻辑代码
    return render(request, 'helpdesk.html')
    # return HttpResponse("Sunck is a good man")
    # return redirect("https://blog.csdn.net/miaoqinian")


def test(request):
    # 业务逻辑代码
    return render(request, 'test.html')
    # return redirect("https://blog.csdn.net/miaoqinian")
