from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated:
        # qaqas :), sen artiq login olmusan!
        messages.warning(request, f'{request.user.username} Daha evvel login olmusunuz!')
        return redirect('home_view')
    context = dict()
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if len(username) < 6 or len(password) < 6:
            messages.warning(request, 'Zehmet olmasa istifadece adini ve ya sifresinin uygun giriniz!')
            return redirect('user_profile:login_view')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} Sessiyaniz Basladi!')
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)

def logout_view(request):
    messages.warning(request, f'{request.user.username} Sessiyaniz Bitdi!')
    logout(request)
    return redirect('home_view')


def register_view(request):
    context = dict()
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'user_profile/register.html', context)