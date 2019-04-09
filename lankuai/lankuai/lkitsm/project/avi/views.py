
from django.shortcuts import render , redirect
from django.core.paginator import Paginator
from django import forms
from .models import Video
from django.http import HttpResponse, HttpResponseRedirect


class videoForm(forms.Form):
    uploader = forms.CharField()
    imgpath = forms.ImageField()
    uppath = forms.FileField()
    describe = forms.CharField()
    uploaddate = forms.DateField()
    kind = forms.CharField()
    score = forms.IntegerField()
    haveseen = forms.CharField()

#form表单
def form(request):

    if request.method == 'POST':

        vf = videoForm(request.POST ,request.FILES)
        if vf.is_valid():

            uploader = vf.cleaned_data['uploader']
            imgpath = vf.cleaned_data['imgpath']
            print(uploader)
            uppath = vf.cleaned_data['uppath']
            print(uppath ,"+++++++++++++++++++++++++++++++++++++++++++++++++")
            describe = vf.cleaned_data['describe']
            print(describe)
            uploaddate = vf.cleaned_data['uploaddate']
            print(uploaddate)
            kind = vf.cleaned_data['kind']
            print(kind)
            score = vf.cleaned_data['score']
            print(score,'5555555555555555555555555555555555555555555555')
            haveseen = vf.cleaned_data['haveseen']


            vid = Video()
            vid.uploader = uploader
            vid.imgpath = imgpath
            vid.uppath = uppath
            vid.describe = describe
            vid.uploaddate = uploaddate
            vid.kind = kind
            vid.score = score
            vid.haveseen = haveseen

            print(type(vid.uppath), '---' ,vid.uppath ,"11111111111111111111111111111111111111111111111111111111111111111111111111111111")
            vid.save()
            print("2222222222222222")
            print("来到这里会重定向-----------------")
        return redirect('/media/upload')
    else:
        vf = videoForm

    haveseen = "已看过"
    print("怎么没到这历来。。。。。。。。。。。。。。。。。。。。。。。。。")

    return render(request, 'avi/uploading.html', locals() ,{"title":"上传视频","haveseen":haveseen})




from project.settings import MEDIA_URL
#蓝快课堂
def media(request ,pageid):

    username = request.session['username']
    print(username ,'======当前登录用户名username========================')
    vidList = Video.objects.all()
    paginator = Paginator(vidList, 3)
    page = paginator.page(pageid)
    print(page ,'页数')
    #搜索
    search = request.POST.get("search")
    error_msg = "查无此视频"

    #我的总分
    #我看过的视频ID，所有ID的分数和
    iseeList = Isee.objects.filter(iname=username)
    count = 0
    score = 0
    for isee in iseeList:

        v = Video.objects.get(id=isee.igid)#取出我看过的视频
        print(v.score ,"单条视频的分数")
        count += 1
        score += v.score
        print(score ,"所有视频的分数和")

    if not search:
        error_msg="请输入关键字"
        return render(request, 'avi/media.html', {'title': '蓝快课堂', 'username': username, 'video': page, 'vidList': vidList, 'error_msg': error_msg , "count":count , "score":score})
    else:

        vidList1 = Video.objects.filter(describe__icontains = search)
        return render(request, 'avi/media.html', {'title': '蓝快课堂', 'username': username, 'video': page, 'vidList': vidList1, 'error_msg': error_msg , "count":count , "score":score})


def avi(request ,id):

    video = Video.objects.get(id = id)

    return render(request ,'avi/avi.html' ,{"video":video})

import time
from .models import Isee
def addIsee(request ,pid):
    #当前用户
    username = request.session['username']
    print(username)
    #视频ID
    newpath = request.path[10:]#media/add1
    video = Video.objects.get(id=newpath)
    print(request.path ,"----------------------url----------------------")
    print(newpath ,"新dizhi --------------------------------------------")
    seetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print(seetime ,"")
    #如果该用户看过该视频，则直接重定向
    if Isee.objects.filter(iname=username ,igid=newpath):
        return redirect('/media/avi' + newpath)
    else:
        #否则先存进去再重定向
        isee = Isee.createisee(username, newpath, seetime)
        isee.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/media/avi' + newpath)


def addok(request):
    return redirect('/addok')











