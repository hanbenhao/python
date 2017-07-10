#coding:utf-8
import json
import re

from django.http import HttpResponse

# Create your views here.

# 注册用户
def addUser(request):
    return HttpResponse(u'成功')
