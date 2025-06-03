# frontend/auth_views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Şifreler uyuşmuyor.')
            return render(request, 'frontend/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu kullanıcı adı zaten mevcut.')
            return render(request, 'frontend/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Bu e-posta zaten kayıtlı.')
            return render(request, 'frontend/register.html')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, 'Kayıt başarılı! Giriş yapabilirsiniz.')
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'frontend/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre.')

    return render(request, 'frontend/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
