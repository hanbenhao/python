from django.http import HttpResponse
import json

# 数据库接口导入
from hbh import models as hbh_models

# 注册用户
def addUserInfo(request):
    info = {
        'fail': '失败',
        'error': '错误',
        'Success': '成功'
    }
    if request.method == "GET":
        name = request.GET.get('name', False)
        age = request.GET.get('age', False)
        if name and age:
            hbh_models.Person(name=name, age=age).save()
            print(request, 111111)
            return HttpResponse(json.dumps(info['Success'], ensure_ascii=False))
        else:
            return HttpResponse(json.dumps(info['fail'], ensure_ascii=False))
    else:
        return HttpResponse(json.dumps(info, ensure_ascii=False))

# 用户登录
def isLogin(request):
    info = {
        'fail': '失败',
        'error': '错误',
        'Success': '成功'
    }
    if request.method == "POST":
        print(request.POST)
        return HttpResponse(json.dumps(info, ensure_ascii=False))
    else:
        return HttpResponse(json.dumps(info, ensure_ascii=False))