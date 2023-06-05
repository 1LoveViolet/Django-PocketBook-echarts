# accounting_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from . import models
from .models import  UserInfo,Account
from .forms import UserRegistrationForm, UserLoginForm, AccountForm

import json

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html", {'msg': "注册成功哦", 'url': "/login"})

    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = UserLoginForm(data=request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            print(form.cleaned_data['username'], form.cleaned_data['password'])

            user=UserInfo.objects.filter(username=username,password=password)
            if user:
                return render(request, "success.html", {'msg': "登录成功哦", 'url': "/entry_list"})
            else:
                error = '用户名或密码不正确'
                return render(request, "error.html", {'msg': error, 'url': "/login"})
        else:
            error = '用户名或密码不正确'
            return render(request, "error.html", {'msg': error, 'url': "/login"})
def user_loginout(request):
    logout(request)
    return render(request, "success.html", {'msg': "退出成功哦", 'url': "/login"})

def entry_list(request):
    entries = models.Account.objects.all()
    return render(request, 'entry_list.html', {'entries': entries})

def create_list(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('entry_list')
    else:
        form = AccountForm()
    return render(request, 'create_list.html', {'form': form})


def update_list(request, entry_id):
    entry = models.Account.objects.get(id=entry_id)
    print('method:  '+ request.method)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=entry)
        print(form)
        if form.is_valid():
            form.save()
            print('表单数据有效')
            return redirect('entry_list')
        else:
            # 输出验证错误信息
            print(form.errors)
    else:
        form = AccountForm(instance=entry)
        print('请求方法不是POST')
    print('表单数据无效')
    return render(request, 'update_list.html', {'form': form, 'entry': entry})


def delete_list(request, entry_id):
    entry = models.Account.objects.get(id=entry_id)
    entry.delete()
    return redirect('entry_list')

from django.shortcuts import render

def chart_view(request):
    records = Account.objects.order_by('time')
    data = list(records)
    times=[]
    accounts=[]
    for record in data:
        # 假设你的 Record 模型有 'timestamp', 'expense' 和 'income' 字段
        time = record.time.strftime('%Y-%m-%d')
        type = record.type
        if type==1:
            account=record.account
        else:
            account=-record.account
        times.append(time)
        accounts.append( account)

    return render(request, 'echarts.html', {'times': json.dumps(times), 'accounts': json.dumps(accounts)})
