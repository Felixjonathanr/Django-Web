from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Bikin_akun
from django.contrib import messages


def index(request):
    return render(request, 'index.html')
def register (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        role = request.POST['role']
        if Bikin_akun.objects.filter(username=username).exists():
            messages.info(request,'Username sudah digunakan')
            return redirect (register)
        elif Bikin_akun.objects.filter(email=email).exists():
            messages.info(request,'Email sudah digunakan')
            return redirect(register)
        else:
            user = Bikin_akun.objects.create(username=username, password=password, email=email, role=role)
            return redirect(login)
    return render(request, 'register.html')
def login (request):
    if request.method =="POST":
        username2 = request.POST['username2']
        password2 = request.POST['password2']
        role2 = request.POST['role2']
        try :
            user = Bikin_akun.objects.get(username=username2, password=password2, role= role2)
            request.session['username3'] = user.username
            if role2 =="seller":
                return redirect(index)
            else:
                return redirect(users)
        except Bikin_akun.DoesNotExist:
            messages.info(request, 'Akun atau password atau role anda salah')
            return redirect(login)

    return render(request, 'login.html')
def users(request):
    username3 = request.session.get('username3')
    return render(request,'users.html', {'username': username3})
