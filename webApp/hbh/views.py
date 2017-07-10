#coding:utf-8
import json
import re

from django.http import HttpResponse

# 数据库接口导入
from hbh import models as hbh_models

info = {
        'fail': '失败',
        'error': '错误',
        'Success': '成功'
    }

# 注册用户
def addUser(request):
    if request.method == "POST":
        data = request.POST
        if hbh_models.User.objects.filter(UserName = data['UserName']):
            return HttpResponse(u'数据已存在')
        elif not re.match('^1(3|4|5|7|8)[0-9]\d{8}$', data['PhoneNumber']):
            return HttpResponse(info['fail'])
        elif data['UserName'] and data['UserPassword']:
            hbh_models.User(UserName=data['UserName'], UserPassword=data['UserPassword'], PhoneNumber=data['PhoneNumber']).save()
            return HttpResponse(info['Success'])
    else:
        return HttpResponse(u'接口调用方式出错！')

# 用户登录
def isLogin(request):
    if request.method == "GET":
        UserName = request.GET.get('UserName', False)
        UserPassword = request.GET.get('UserPassword', False)
        if UserName and UserPassword:
            userInfo = hbh_models.User.objects.filter(UserName=UserName).values()
            if userInfo[0]['UserPassword'] == UserPassword:
                return HttpResponse(u'登陆成功!')
        else:
            return HttpResponse(u'UserName不能为空！')
    else:
        return HttpResponse(u'接口调用方式出错！')

#删除用户
# def deleteUser(request):
#     if request.method == "GET":
#         UserName = request.GET.get('UserName')
#         UserPassword = request.GET.get('UserPassword')
#         if UserName and UserPassword: