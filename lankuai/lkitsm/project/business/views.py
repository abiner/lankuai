

from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect
from .models import Business ,files
from website.models import Departments
from django.core.paginator import Paginator
from login .models import User
import os
from django.contrib import messages

def busines(request):
    username = request.session['username']
    print(username ,"当前登录用户")

    user = User.objects.get(uname=username)
    print(user.role ,"当前登录这点role是什么？？？")
    if user.role == 2 or user.role == 3:
        print("我们职位比较高")
        return render(request, 'business/business.html', {"title": "商务合同" , "username":username})

    else:
        print("我们职位比较低")
        messages.add_message(request ,messages.DEBUG ,'权限不足')
        return redirect('/index')


from django.shortcuts import render,HttpResponse,HttpResponseRedirect

def addbusiness(request):

    pactNo = request.POST.get("pactNo")
    print(pactNo ,"-----------------------------------")
    projectname = request.POST.get("projectname")
    print(projectname ,"-----------------------------------")
    signedname = request.POST.get("signedname")
    signedsubject = request.POST.get("signedsubject")
    billingunit = request.POST.get("billingunit")
    executedate = request.POST.get("executedate")
    print(executedate ,"-----------------executedate------------------")
    begindate = request.POST.get("begindate")
    overdate = request.POST.get("overdate")
    pacttotalsum = request.POST.get("pacttotalsum")
    monthlyfee = request.POST.get("monthlyfee")
    Agreedpaymenttime = request.POST.get("Agreedpaymenttime")
    knotrate = request.POST.get("knotrate")
    accountmanager = request.POST.get("accountmanager")
    projectaddress = request.POST.get("projectaddress")
    followuppeople = request.POST.get("followuppeople")
    servertype = request.POST.get("servertype")
    servicemode = request.POST.get("servicemode")
    print("-------------------所有数据均获取到了----------------------")
    filess = request.FILES.getlist("addfile")


    print(pactNo, projectname, signedname, signedsubject, billingunit, executedate, begindate
                                  ,overdate, pacttotalsum, monthlyfee, Agreedpaymenttime, knotrate, accountmanager
                                  ,projectaddress , followuppeople, servertype, servicemode)
    bus = Business.createbusiness(pactNo, projectname, signedname, signedsubject, billingunit, executedate, begindate
                                  ,overdate, pacttotalsum, monthlyfee, Agreedpaymenttime, knotrate, accountmanager
                                  ,projectaddress , followuppeople, servertype, servicemode)
    print(bus)
    bus.save()
    for file in filess:
        print(file ,"-----------------------是否有文件路径------------------------------")
        f = files.createfiles(pactNo ,file)
        print(f)
        f.save()
    return redirect('/business/')

#所有合同
def allcontract(request ,pageid):
    allconList = Business.objects.all()
    paginator = Paginator(allconList, 2)
    page = paginator.page(pageid)
    return render(request ,"business/allcontract.html" ,{"title":"所有合同" ,"myconList":page})


#我的合同
def mycontract(request ,pageid):
    username = request.session['username']
    #所有跟进人是我的合同
    myconList = Business.objects.all().filter(followuppeople=username)
    paginator = Paginator(myconList, 2)
    page = paginator.page(pageid)
    return render(request ,"business/mycontract.html" ,{"title":"我的合同" ,"myconList":page})

#合同详情
def contractdetails(request ,pid):
    path = request.path
    print(path ,"当前路径------------大家好，才是真的好啊--------------")
    #/business/alcontract/fds4321
    newpath = path[10:]
    print(newpath ,"新的路径-------------------------")
    bus = Business.objects.get(pactNo=newpath)
    filess = files.objects.filter(pactNo=newpath)
    print(len(filess) ,filess ,"----------------------")
    return render(request ,"business/contractdetails.html" ,{"business":bus ,"filess":filess})






