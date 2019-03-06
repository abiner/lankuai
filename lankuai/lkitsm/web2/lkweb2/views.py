from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
from django import forms
from .models import User


#定义表单模型
class UserloginForm(forms.Form):
    username = forms.CharField(label = '用户名 :',max_length = 50)
    password = forms.CharField(label = '密码 :',widget = forms.PasswordInput())


def login(request):
    if request.method == 'POST':
        uf = UserloginForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(uname__exact = username,upasswd__exact = password)
            if user:
                return render_to_response('main.html',{'username':username})#成功后跳转的页面
            else:
                return render_to_response('login.html',{'uf':uf})#登录失败跳转回原来登录页面
                #return render(request,'login.html')
                #return HttpResponseRedirect('/login/')
    else:
        uf=UserloginForm() 
    return render_to_response('login.html',{'uf':uf})
    #return render(request,'login.html')
    #return HttpResponse("Sunck is a good man")



@login_required
def nav(request):
    
    return render(request,'nav.html')
    #return HttpResponse("Sunck is a good man")

@login_required
def form(request):
    return render(request,'form.html')


@login_required
def main(request):
    return render(request,'main.html')

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def table(request):
    return render(request,'table.html')

#@login_required
def home(request):
    return render(request,'home.html')