from django.shortcuts import render
from login.models import User
from website.models import Departments
from .models import failureMessages ,faultType ,theDoorOf,cost ,quote
import random
import time
from django.shortcuts import redirect

#维修申请页面
def repair(request):
    username = request.session['username']
    user = User.objects.get(uname=username)
    dep = user.udepname
    depList = Departments.objects.all()
    ftList = faultType.objects.all()
    return render(request ,'repairANDbuyer/repair.html' ,{"username":username ,"dep":dep ,"depList":depList ,"ftList":ftList })



from .models import State
#增  维修表，刚提交上来，是为给检测技术人员的
def addrepair(request):
    if request.method == "POST":
        #faultID,fname,inunits,phone,faultclass,brandtype,equipmentID,faultdescribe,subtime,eventlevel
        #faultID
        faultID = str(int(time.strftime("%Y%m%d%H%M%S"))+int(random.randrange(1 ,1000)))
        fname = request.POST.get("fname")
        inunits = request.POST.get("inunits")
        phone = request.POST.get("phone")
        faultclass = request.POST.get("faultclass")
        brandtype = request.POST.get("brandtype")
        equipmentID = request.POST.get("equipmentID")
        faultdescribe = request.POST.get("faultdescribe")
        #subtime 时间
        subtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print(subtime ,"---------------------------subtime------------------------------")
        subtime = request.POST.get("subtime")

        #让事件等于什么呢？
        eventlevel = 1
        print(faultID,fname,inunits,phone,faultclass,brandtype,equipmentID,faultdescribe,subtime,eventlevel)
        fm = failureMessages.createfailureMessages(faultID,fname,inunits,phone,faultclass,brandtype,equipmentID,faultdescribe,subtime,eventlevel)
        fm.save()
        return redirect('/repairANDbuyer/addrepairok/')


def addrepairok(request):
    redirect = "/repairANDbuyer/repair"
    return render(request, 'addok.html', {"redirect": redirect})

#维修
#检测人员  提交表
def verif(request ,pid):
    username = request.session['username']
    print(username ,"当前登录人")
    path = request.path
    print(path ,"path------------------------------------------------------------------------------------------------")
    #/repairANDbuyer/20190131204044/
    newpath = path[16:30]
    print(newpath ,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaanewpathaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    #维修表信息
    fm = failureMessages.objects.get(faultID=newpath)
    ft = faultType.objects.all()
    dempList = Departments.objects.all()
    #co = cost.objects.get(faultID=newpath)
    print(dempList ,"---------------------------dempList-----------------------------")
    user = User.objects.get(uname=username)

    #当前登录人角色为1，显示维修表，及输入成本价信息
    if user.role == 1:
        return render(request, "repairANDbuyer/inspectorrole1.html", {"title": "技术检测及报成本价", "fm": fm, "ft": ft
            , "dempList": dempList, "username": username})

    #当前登录人角色为2，显示维修表和成本价表，及输入报价信息
    elif user.role == 2 :
        #成本价表
        cos = cost.objects.get(faultID=newpath)
        return render(request, "repairANDbuyer/inspectorrole2.html", {"title": "部门经理报价", "fm": fm, "ft": ft
            , "dempList": dempList, "username": username ,"cos":cos})


    #当前登录人角色为3
    elif user.role == 3 :
        return render(request, "repairANDbuyer/inspectorrole3.html", {"title": "技术检测人员", "fm": fm, "ft": ft
            , "dempList": dempList, "username": username})

    else:
        print("-------------------------------------else-----------------------------------")
        print(path[-1])
        print("-------------------------------------else-----------------------------------")
        return render(request, "ok.html", {"title": "技术检测及报成本价", "fm": fm, "ft": ft
            , "dempList": dempList, "username": username})


#添加 唐黄 成本价
def addCostPrice(request):
    if request.method == "POST":
        faultID = request.POST.get("faultID")
        cname = request.POST.get("cname")
        cause = request.POST.get("cause")
        supplies = request.POST.get("supplies")
        costprice = request.POST.get("costprice")
        subtime = request.POST.get("subtime")
        #当前 时间
        subtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print(faultID,cname,cause,supplies,costprice,subtime)
        co = cost.createcost(faultID,cname,cause,supplies,costprice,subtime)
        co.save()

        fm = failureMessages.objects.get(faultID=faultID)
        #可维修则为2
        if "pizhun" in request.POST:
            fm.eventlevel = 2
        #不可维修则为0
        elif "bohui" in request.POST:
            fm.eventlevel = 0
        fm.save()
        return redirect('/addCostPriceok/')

def addCostPriceok(request):
    redirect = "/index"
    return render(request, 'addok.html', {"redirect": redirect})

from django.core.paginator import Paginator
#添加部门经理报价   addcostPrice
def addquote(request):
    print("i live you hahaahahahahahahahahahah")
    if request.method == "POST":
        username = request.session["username"]
        faultID = request.POST.get("faultID")
        quo = request.POST.get("quo")
        comment = request.POST.get("comment")
        subtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print(faultID ,username ,quo ,comment ,subtime ,"-------------------------")
        quot = quote.createquote(faultID ,username ,quo ,comment ,subtime)
        quot.save()
        fm = failureMessages.objects.get(faultID=faultID)
        if "pizhun" in request.POST:
            fm.eventlevel = 100
        elif "bohui" in request.POST:
            fm.eventlevel = 0
        fm.save()
        return redirect('/index')

# 维修 发起人查看自己的进程
def myrepair(request ,pageid):
    username = request.session["username"]
    myrepairList = failureMessages.objects.filter(fname=username)
    paginator = Paginator(myrepairList ,6)
    page = paginator.page(pageid)

    return render(request ,"repairANDbuyer/myrepair.html" ,{"myrepairList":page})

#维修 ，特定的某一条进程
def onerepair(request ,pageid):
    path = request.path
    print(path ,'整个路径------------------------------')
    newpath = path[25:39]#19,33
    print(newpath ,"截取后的路径newpath000000000000000000000000")

    #这里肯定要改的

    failureM = failureMessages.objects.get(faultID=newpath)
    print(failureM.eventlevel ,"--------------------------------目前该维修单  状态是啥")

    if failureM.eventlevel == 1:
        #提交成本价
        result = "等待技术人员检测"
        return render(request ,"repairANDbuyer/onerepair.html" ,{"title":"维修申请结果" ,"failureM":failureM ,"result":result})

    elif failureM.eventlevel == 2:
        #技术检测已完成，需要显示技术人员检测
        result = "等待部门经理报价"
        co = cost.objects.filter(faultID=newpath)
        return render(request ,"repairANDbuyer/onerepair.html" ,{"title":"维修申请结果" ,"failureM":failureM ,"result":result ,"co":co})

    elif failureM.eventlevel == 0 :
        #终止进程,就算终止进程，你也得显示在那一步终止的
        result = "已终止进程"
        co = cost.objects.filter(faultID=newpath)
        quot = quote.objects.filter(faultID=newpath)
        #如果没有技术人员检测表
        if not co:
            return render(request ,"repairANDbuyer/onerepair.html" ,{"title":"维修申请结果" ,"failureM":failureM ,"result":result})
        else:
            if not quot:
                return render(request ,"repairANDbuyer/onerepair.html" ,{"title":"维修申请结果" ,"failureM":failureM ,"result":result ,"co":co})
            else:
                return render(request, "repairANDbuyer/onerepair.html",
                              {"title": "维修申请结果", "failureM": failureM, "result": result, "co": co ,"quot":quot})


    elif failureM.eventlevel == 100 :
        #维修成功，显示技术人员检测，显示部门经理报价
        result = "维修成功"
        co = cost.objects.filter(faultID=newpath)
        quot = quote.objects.filter(faultID=newpath)

        return render(request ,"repairANDbuyer/onerepair.html" ,{"title":"维修申请结果" ,"failureM":failureM ,"result":result ,"co":co ,"quot":quot})


from .models import Goods ,purchaseApplyFor ,goodsCost ,managerConsent ,Consignee
#采购
def buyer(request):
    #设置默认
    purchaseID= str(int(time.strftime("%m%d%H%M%S"))+int(random.randrange(1 ,1000)))
    #str(time.strftime("%m%d%H%M%S") + random.randrange(1, 1000))
    print(purchaseID ,"==========================purchaseID")
    username = request.session["username"]
    print("当前登录人：" ,username ,"----------------")
    user = User.objects.get(uname=username)
    depname = user.udepname
    print("当前登录人所属部门：" ,depname ,"----------------")



    return render(request ,'repairANDbuyer/buyer.html' ,{"title":"采购申请页面" ,"purchaseID":purchaseID ,"pdemp":depname ,"username":username})

#采购 ，发起采购单
def addpurchase(request):
    if request.method == "POST":
        #获取商品信息
        purchaseID = request.POST.get("purchaseID")


        #获取申请信息
        pdemp = request.POST.get("pdemp")
        pname = request.POST.get("pname")
        pdate = request.POST.get("pdate")
        pcomment = request.POST.get("pcomment")
        # pcourse 状态
        pcourse = 1

        # gnameList 多个物品名称 ， gamountList 多个物品数量
        gnameList = request.POST.getlist("name1", [])
        gamountList = request.POST.getlist("name2", [])

        count = len(gnameList)
        print(len(gnameList), "多个物品名称是多少个呢？？？？？？？？？？？？")
        for item in range(count):
            goods = Goods.creategoods(purchaseID, gnameList[item], gamountList[item])
            goods.save()

        # goods = Goods.creategoods(purchaseID ,gname ,gamount)
        # goods.save()
        paf = purchaseApplyFor.createpurchaseApplyFor(purchaseID ,pdemp ,pname ,pdate ,pcomment ,pcourse)
        paf.save()
        return redirect('/repairANDbuyer/addpurchaseok/')

def addpurchaseok(request):
    redirect = "/repairANDbuyer/buyer"
    return render(request, 'addok.html', {"redirect": redirect})


#采购 ，采购部唐涛提交成本价 ,role 为1，   部门经理通过并修改报价role 为2
def costprice(request ,pig):
    username = request.session["username"]
    user = User.objects.get(uname=username)


    #首先展示申请页面
    print(request.path ,"这是路径，需要剪切-----------------")
    #/repairANDbuyer/2201246091
    path = request.path
    newpath = path[16:25]
    print(newpath ,"这是剪切后的网址-----------------------")
    paf = purchaseApplyFor.objects.get(purchaseID=newpath)
    goods = Goods.objects.get(purchaseID=newpath)

    #当前登录人role 为1 ，显示采购申请，采购部提交成本
    if user.role == 1 :
        return render(request, 'repairANDbuyer/costprice1.html', {"paf":paf , "goods":goods})

    #当前登录人role 为2 ，显示采购申请 ，成本，提交同意
    if user.role == 2 :
        gc = goodsCost.objects.get(purchaseID=newpath)

        return render(request, 'repairANDbuyer/costprice2.html', {"paf": paf, "goods": goods ,"gc":gc})
    #当前登录人role为0，显示采购申请，成本，同意，提交收货时间
    if user.role == 0 :
        paf = purchaseApplyFor.objects.get(purchaseID=newpath)
        gc = goodsCost.objects.get(purchaseID=newpath)
        mc = managerConsent.objects.get(purchaseID=newpath)

        cgdate = time.strftime("%Y-%m-%d/%H:%M", time.localtime(time.time()))
        print(cgdate ,"========================cgdate===============================")

        return render(request, 'repairANDbuyer/costprice3.html', {"paf": paf, "goods": goods, "gc": gc ,"mc":mc ,"cgdate":cgdate})

#采购 ，增加成本
def addgoodscost(request):
    if request.method == "POST":
        purchaseID = request.POST.get("purchaseID")
        gcgprice = request.POST.get("cnt4")
        suggestprice = request.POST.get("cnt5")

        goodsprofit = int(suggestprice) - int(gcgprice)

        gcdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print(gcdate ,"当前时间，格式是否咩问题呢")
        pcomment = request.POST.get("pcomment")

        print(purchaseID , gcgprice, suggestprice ,goodsprofit ,gcdate ,pcomment)
        gc = goodsCost.creategoodsCost(purchaseID , gcgprice, suggestprice ,goodsprofit ,gcdate ,pcomment)
        gc.save()
        #保存进去了，就修改采购层级 ，自己再也看不到了，给部门经理看
        paf = purchaseApplyFor.objects.get(purchaseID=purchaseID)
        paf.pcourse = 2
        paf.save()
        return redirect('/index')

#采购 ，增加部门经理同意
def addmanageryes(request):
    if request.method == "POST":
        purchaseID = request.POST.get("purchaseID")
        affirmprice = request.POST.get("affirmprice")
        mcdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        pcomment = request.POST.get("pcomment")
        print(purchaseID ,affirmprice ,mcdate ,pcomment)
        mc = managerConsent.createmanagerConsent(purchaseID ,affirmprice ,mcdate ,pcomment)
        mc.save()
        #保存好了，修改采购层级，
        paf = purchaseApplyFor.objects.get(purchaseID=purchaseID)
        paf.pcourse = 3
        paf.save()
        return redirect('/index')

#采购 ，增加发起人收货时间
def addconsignee(request):
    if request.method == "POST":
        purchaseID = request.POST.get("purchaseID")
        cgdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        pcomment = request.POST.get("pcomment")
        cg = Consignee.createconsignee(purchaseID ,cgdate ,pcomment)
        cg.save()
        paf = purchaseApplyFor.objects.get(purchaseID=purchaseID)
        paf.pcourse = 100 #表示成功
        paf.save()
        return redirect('/index')

#采购 ，发起人查看进程
def mypurchase(request ,pageid):
    username = request.session["username"]
    print(username ,"当前登录用户------------")
    user = User.objects.get(uname=username)
    pafList = purchaseApplyFor.objects.filter(pname=username) #取出所有我申请的采购单

    paginator = Paginator(pafList ,5)
    page = paginator.page(pageid)

    return render(request ,"repairANDbuyer/mypurchase.html" ,{"title":"我的采购申请" ,"pafList":page})


def onepurchase(request ,pageid):
    print(request.path ,"-------------------------------------")#/repairANDbuyer/mypurchase/220161824/
    path = request.path
    newpath = path[27:36]   #id
    print(newpath ,"-------------------------------------")

    paf = purchaseApplyFor.objects.get(purchaseID=newpath)
    goodsList = Goods.objects.filter(purchaseID=newpath)
    if paf.pcourse == 1:#只有申请表，和商品信息
        return render(request, "repairANDbuyer/onepurchase.html" ,{"title":"具体进程" ,"paf":paf ,"goodsList":goodsList})
    elif paf.pcourse == 2:#成本信息
        gc = goodsCost.objects.get(purchaseID=newpath)
        return render(request, "repairANDbuyer/onepurchase.html" ,{"title":"具体进程" ,"paf":paf ,"goodsList":goodsList ,"gc":gc})
    elif paf.pcourse == 3:#部门经理同意
        gc = goodsCost.objects.get(purchaseID=newpath)
        mc = managerConsent.objects.get(purchaseID=newpath)
        return render(request, "repairANDbuyer/onepurchase.html",
                      {"title": "具体进程", "paf": paf, "goodsList": goodsList, "gc": gc ,"mc":mc})
    elif paf.pcourse == 100:
        gc = goodsCost.objects.get(purchaseID=newpath)
        mc = managerConsent.objects.get(purchaseID=newpath)
        cg = Consignee.objects.get(purchaseID=newpath)
        return render(request ,"repairANDbuyer/onepurchase.html" ,{"title":"具体进程" ,"paf":paf ,"goodsList":goodsList
            ,"gc":gc ,"mc":mc ,"cg":cg})






