# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2023/04/19
# @File : account.py

from django.shortcuts import render, redirect
from web import models

from utils.encrypt import md5

# 1.定义类
from django import forms


class LoginForm(forms.Form):
    role = forms.ChoiceField(
        required=True,
        choices=(("2", "客户"), ("1", "管理员")),
        widget=forms.Select(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}, render_value=True)
        # 保留密码 render_value=True
    )


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    # 1.接收并获取数据(数据格式或是否为空验证 - Form组件 & ModelForm组件）
    form = LoginForm(data=request.POST)
    if not form.is_valid():
        print("验证失败")
        return render(request, "login.html", {"form": form})

    # {'role': '1', 'username': 'asdfasdf', 'password': '123123'}
    # print(form.cleaned_data)  # {"username":'',"password":'xxx","role":xxx}
    role = form.cleaned_data.get("role")
    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password")
    password = md5(password)

    # 2.去数据库校验  1管理员  2客户
    mapping = {"1": "ADMIN", "2": "CUSTOMER"}
    if role not in mapping:
        return render(request, "login.html", {'form': form, 'error': "角色不存在"})

    if role == "1":
        user_object = models.Administrator.objects.filter(active=1, username=username, password=password).first()
    else:
        user_object = models.Customer.objects.filter(active=1, username=username, password=password).first()

    # 2.1 校验失败
    if not user_object:
        return render(request, "login.html", {'form': form, 'error': "用户名或密码错误"})

    # 2.2 校验成功，用户信息写入session+进入项目后台
    request.session['user_info'] = {'role': mapping[role], 'name': user_object.username, 'id': user_object.id}

    return redirect("/level/list/")


def sms_login(request):
    return render(request, "sms_login.html")


def test(request):
    return render(request, "test.html")
