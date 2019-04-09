#自定义表单

from django import forms

class LoginForm(forms.Form):
    #required=True:不能为空,必须得填
    #widget=forms.PasswordInput:形成密文
    username = forms.CharField(max_length=12 ,min_length=6 ,required=True
                               ,error_messages={'required':'用户账号不能为空' ,'invalid':'格式错误'}
                               ,widget=forms.TextInput(attrs={'class':'c'}))
    passwd   = forms.CharField(max_length=16 ,min_length=6 ,widget=forms.PasswordInput)










