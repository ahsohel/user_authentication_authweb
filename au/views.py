from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
# Create your views here.


def index(request):
    return render(request, 'index.html')

def func_login(request):
    if request.method=="POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        print(user_name)
        print("user_name")
        print(password)

        user_vari = authenticate(username=user_name, password=password)
        print("username is")
        print(user_vari.username)
        print("password is")
        print(user_vari.password)
        print("first_name is")
        print(user_vari.first_name)
        print("last_name is")
        print(user_vari.last_name)
        if user_vari is not None:
            login(request, user_vari)
            return redirect('index')

    return render(request, 'func_login.html')




def func_signup(request):
    if request.method == "POST":
        user_name=request.POST.get('user_name')
        f_name=request.POST.get('first_name')
        l_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(user_name)


        myusr_vari = User.objects.create_user(user_name, email, password)
        myusr_vari.first_name=f_name
        myusr_vari.last_name=l_name
        myusr_vari.save()

        return redirect('index')

    return render(request, 'func_signup.html')


def func_logout(request):
    logout(request)
    return redirect('index')