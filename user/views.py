
from django.shortcuts import render, redirect, HttpResponseRedirect
from . import models
from .forms import UserForm,RegisterForm


def login(request):
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(user_name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['nickname'] = user.nickname
                    request.session['user_name'] = user.user_name
                    return redirect(request.session['login_from'])
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'user/login.html', locals())
    if request.META.get('HTTP_REFERER', '/') == 'http://127.0.0.1:8000/user/register/':
        pass
    else:
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    login_form = UserForm()
    return render(request, 'user/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            nickname = register_form.cleaned_data['nickname']
            mobile = register_form.cleaned_data['mobile']
            sex = register_form.cleaned_data['sex']

            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'user/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(user_name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'user/register.html', locals())
                same_nickname_user = models.User.objects.filter(nickname=nickname)
                if same_nickname_user:  # 用户名唯一
                    message = '昵称已存在，请重新选择昵称！'
                    return render(request, 'user/register.html', locals())
                same_mobile_user = models.User.objects.filter(mobile=mobile)
                if same_mobile_user:  # 手机唯一唯一
                    message = '该手机号已被注册，请使用别的手机号！'
                    return render(request, 'user/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.user_name = username
                new_user.password = password1
                new_user.mobile = mobile
                new_user.sex = sex
                new_user.save()
                return HttpResponseRedirect('/user/login/')  # 自动跳转到登录页面
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    register_form = RegisterForm()
    return render(request, 'user/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect(request.META.get('HTTP_REFERER', '/'))
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect(request.META.get('HTTP_REFERER', '/'))
