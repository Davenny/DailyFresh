# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.from hashlib import sha1
from django.shortcuts import render,redirect
from models import *
def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    if upwd!=upwd2:
        return redirect('/user/register/')

    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    user = UserInfo()
    user.uname = uname
    user.upwd =upwd3
    user.uemail =uemail

