from acount.models import CustomUser
from acount.forms import RegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm ##로그인, 회원가입 폼
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        auth_form = AuthenticationForm(request=request, data = request.POST)
        if auth_form.is_valid():
            v_username = auth_form.cleaned_data.get('username')
            v_password = auth_form.cleaned_data.get('password')
            user  = authenticate(request=request, username = v_username, password = v_password)           
            if user:
                login(request, user)
        return redirect('urlnamehome')
    else:
        auth_form = AuthenticationForm()
        return render (request, 'login.html', {'views_auth_form':auth_form})


def logout_view(request):
    logout(request)
    return redirect('urlnamewelcome')


def signup(request):
    if request.method == 'POST':
        cre_form = RegisterForm(request.POST)
        if cre_form.is_valid():
            user = cre_form.save()
            login(request, user)
            return redirect('urlnamehome')
        else:
            if CustomUser.objects.filter(username=request.POST['username']).exists(): # 아이디 중복 체크 
                return render(request, 'error.html', {'errorid':request.POST['username']})

            if request.POST['password1'] != request.POST['password2']: # 비밀번호와 비밀번호 확인이 다를 시
                return render(request, 'error.html', {'errorpw':request.POST['username']}) 

            if len(request.POST['password1']) < 8 or len(request.POST['password2']) < 8: # 비밀번호가 8자리 미만일 시
                return render(request, 'error.html', {'errorpw2':request.POST['username']})

            if request.POST['password1'].isdigit() or request.POST['password2'].isdigit():# 비밀번호가 숫자로만 이루어졌을 때
                return render(request, 'error.html', {'errorpw3':request.POST['username']})

            if CustomUser.objects.filter(nickname=request.POST['nickname']).exists(): # 닉네임 중복 체크 
                return render(request, 'error.html', {'errornn':request.POST['nickname']})

            return render(request, 'error.html', {'errorelse':request.POST['nickname']}) # 그 외의 에러       
    else: 
        cre_form = RegisterForm()
        return render(request, 'signup.html',{'views_cre_form':cre_form})

def error(request):
    return render(request,'error.html')


   
