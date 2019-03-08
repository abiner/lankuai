from django.shortcuts import render
from website.models import Departments

from login.models import User
from django.core.paginator import Paginator
import time ,random




def workfolw(request):
    username = request.session['username']
    user = User.objects.get(uname=username)

    depar = user.udepname
    print(depar ,'depar---------------------------------------------')
    #%Y-%m-%d %H:%M:%S"当前时间作为流水号
    wid = str(time.strftime("%Y%m%d%H%M%S"))
    dep = Departments.objects.get(depname=user.udepname)
    if user.role == 0:
        print(user.role,"role=======================================================================================")
        print("我的身份是0 或 1========================================================================================")
        #hierarchy0 = dep.id 是员工的身份是为了让他提交给部门经理
        hierarchy0 = dep.id  #等于部门ID
        return render(request, 'workfolw/hrworkfolw.html', {"depar":depar , "username":username , 'wid':wid , 'hierarchy0':hierarchy0})

    if user.role == 1:
        print(user.role,"role=======================================================================================")
        print("我的身份是0 或 1========================================================================================")
        #hierarchy0 = dep.id 是员工的身份是为了让他提交给部门经理
        hierarchy0 = dep.id  #等于部门ID
        return render(request, 'workfolw/hrworkfolw.html', {"depar":depar , "username":username , 'wid':wid , 'hierarchy0':hierarchy0})


    #已经是部门经理的身份了，是手动提交了--------------------------------------------------------------------------------------
    elif user.role == 2:
        print("我的身份是2 或 3========================================================================================")
        dempList = Departments.objects.all()
        for item in dempList:
            print(item.dname ,"=====================================================================================")

        return render(request, 'workfolw/mrworkfolw.html', {"depar":depar , "username":username , 'wid':wid , "dempList":dempList})


    elif user.role == 3:
        print("我的身份是2 或 3========================================================================================")

        dempList = Departments.objects.all()
        for item in dempList:
            print(item.dname ,"=====================================================================================")

        return render(request, 'workfolw/mrworkfolw.html', {"depar":depar , "username":username , 'wid':wid , "dempList":dempList})


from django.shortcuts import redirect
from .models import Workflow ,managerApproval
#增加工作流申请表
def addworkfolw(request):
    if request.method == 'POST':
        wid = request.POST.get('wid')
        print(wid ,'wid')
        wname = request.POST.get('firstName')
        wdepname = request.POST.get('wdepname')
        wapplytype = request.POST.get('country')
        wbegin = request.POST.get('wbegin')
        wfinish = request.POST.get('wfinish')
        wreasons = request.POST.get('wreasons')
        print(wreasons ,'wreasons')

        username = request.session['username']
        user = User.objects.get(uname=username)
        #此用户必然是工程师
        #通过工程师的领导找到自己的部门ID
        demp = Departments.objects.get(depname=user.udepname)


        hierarchy0 = demp.id
        print(hierarchy0,'hierarchy0')

        addwf = Workflow.createWorkflow(wid ,wname ,wdepname ,wapplytype ,wbegin ,wfinish ,wreasons ,hierarchy0)
        print(wname ,wdepname ,wapplytype ,wbegin ,wfinish ,wreasons ,hierarchy0)

        addwf.save()
        return redirect('/hrworkfolw/')

#我的流程
def myfolw(request ,pageid):
    #获取本人所有的工作流显示在html
    username = request.session['username']
    print(username,'def myflow..........')
    #我的全部申请信息
    myflowList = Workflow.objects.filter(wname = username)

    print(type(myflowList) ,"看看myflowList是什么类型")

    paginator = Paginator(myflowList, 3)
    page = paginator.page(pageid)
    return render(request ,'workfolw/myflow.html' ,{"title":"我的流程" ,"myflowList":page})


#我审批过的流程
def IAppro(request ,pageid):
    #我是谁
    username = request.session['username']
    print(username ,"w sh i 谁，我审批过谁")


    #作为部门经理，这个功能是我独有的，我需要查看我审批过的申请表的 进度
    #managerApproval 有我的记录 ，根据我的名字取出
    #iappList = managerApproval.objects.filter(approvaler = username)                  取出我审批过的所有单
    iappList = managerApproval.objects.filter(approvaler=username)
    print(iappList)

    myflowList = []
    for item in iappList:
        print(item.maid ,"suoyou流水号")
        wf = Workflow.objects.get(wid=item.maid)
        myflowList.append(wf)

    paginator = Paginator(myflowList, 6)
    page = paginator.page(pageid)
    return render(request, "workfolw/IAppro.html", {"title": "有经过我手的审批表单", "myflowList": page})

#我的申请表单的现况
def onefolw(request ,wid):
    print("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    path = request.path
    print(path ,'path------------------------------')
    newpath = path[19:33]
    print(newpath ,"newpath000000000000000000000000")

    username = request.session['username']
    user = User.objects.get(uname=username)
    print(user.role ,'user.role=======================================')

    #workflow 申请信息
    workflow = Workflow.objects.get(wid=newpath)
    #审批状态
    if workflow.hierarchy0 == 0:
        result = "驳回"

    elif workflow.hierarchy0 == 100:
        result = "成功"

    else:
        result = "审批中"

    #判断当前用户的岗位级别：工程师
    if user.role == 0 :
        #取出部门经理审批意见，按时间排序
        managerAList = managerApproval.objects.filter(maid=newpath).order_by("approvaltime")
        # 刚申请还没有审批：
        if not managerAList :
            print("这里是还没有审批信息====================================================")
            return render(request, "workfolw/onefolw.html", {"title": "申请信息", "workflow": workflow ,"result": result})

        else:

            for item in managerAList:
                print(item ,"===============================================================")

                return render(request, "workfolw/onefolw.html" ,{"title": "申请信息", "workflow": workflow
                    , "managerAList": managerAList ,"result": result})


    #判断当前用户的岗位级别：部门主管
    if user.role == 1 :
        print("1111111111111111111111111111111111111111111111111111111")
        #那他肯定有部门经理user.manager
        managerA = managerApproval.objects.get(maid=newpath)

        return render(request, "workfolw/onefolw.html", {"title": "申请信息", "workflow": workflow, "managerA": managerA ,"result": result})

    #判断当前用户的岗位级别：部门经理
    if user.role == 2 :
        managerAList = managerApproval.objects.filter(maid=newpath).order_by("approvaltime")
        # 刚申请还没有审批：
        if not managerAList :
            print("not managerAList====================================================")
            return render(request, "workfolw/onefolw.html", {"title": "申请信息", "workflow": workflow ,"result": result})

        else:

            for item in managerAList:
                print(item ,"===============================================================")

            return render(request, "workfolw/onefolw.html", {"title": "申请信息", "workflow": workflow, "managerAList": managerAList ,"result": result})



    return render(request ,"workfolw/onefolw.html" ,{"title":"申请信息" ,"workflow":workflow ,"result": result})

from .models import Notice ,Classify
#公告填写
def notice(request):
    username = request.session["username"]
    cfyList = Classify.objects.all()
    print(cfyList ,"所有-----------------------------------------")
    #for cfy in cfyList:
        #print(cfy.classify)

    return render(request ,"workfolw/notice.html" ,{"username":username} )

from project import settings

#新增公告
def addnotice(request):
    print("到底来了没有，这他妈的！！！！！！！！！！！！！！！！！！！！！！！！！！")
    moticeid = str(time.strftime("%m%d%H%M%S")+str(random.randrange(1 ,1000)))
    print(moticeid)
    nname = request.session["username"]

    issuetime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    audit = False
    if request.method == "POST":
        headline = request.POST.get("headline")
        nclassify = request.POST.get("nclassify")
        picture = request.FILES.get('picture')


        print(picture ,"这里肯定需要数据，不可以没有数据=============================")
        article = request.POST.get("article")

        notic = Notice.createnotice(moticeid ,nname ,headline ,issuetime ,nclassify ,audit ,picture ,article)
        notic.save()
        if picture:
            fname = settings.MEDIA_ROOT + "/noticeImg/" + picture.name
            with open(fname ,"wb") as pic:
                for item in picture.chunks():
                    pic.write(item)
        return redirect('/notice')

#展示
def inform(request ,pageid):

    path = request.path
    print(path) # /0222145148668

    newpath = path[1:]
    print(newpath ,"newpath=======================")

    notice = Notice.objects.get(moticeid=newpath)
    #如果用户角色为3 ，且audit=False   则display = black
    #如果用户角色不为3 ，则display = none
    username = request.session["username"]
    user = User.objects.get(uname=username)
    if user.role == 3 and notice.audit == False:
        display = "block"
        return render(request, "workfolw/show.html", {"notice": notice, "display": display ,"username":username})
    else:
        display = "none"

        return render(request ,"workfolw/show.html" ,{"notice":notice ,"display":display ,"username":username})

#总经理同意
def addyes(request):
    if request.method == "POST":
        moticeid = request.POST.get("moticeid")

        notice = Notice.objects.get(moticeid=moticeid)
        notice.audit = True                                 #改成同意
        notice.save()

        return redirect('/index')

# 我发布的公告
def mynotice(request ,pageid):
    username = request.session["username"]
    noticeList = Notice.objects.filter(nname=username)
    paginator = Paginator(noticeList, 5)
    page = paginator.page(pageid)
    return render(request, "workfolw/mynotice.html" ,{"noticeList":page ,"username":username})

# 所有公告
def alnotice(request ,pageid):
    username = request.session["username"]
    noticeList = Notice.objects.all()
    paginator = Paginator(noticeList, 5)
    page = paginator.page(pageid)
    return render(request, "workfolw/alnotice.html" ,{"noticeList":page ,"username":username})




