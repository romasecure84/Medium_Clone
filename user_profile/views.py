from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    # login olan istifadeci birbasa ana sehifeye getsin
    if request.user.is_authenticated:
        # qaqas :), sen artiq login olmusan!
        messages.warning(request, f'{request.user.username} Daha evvel login olmusunuz!')
        return redirect('home_view')
    context = dict()
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # Bu bilgilerin dogru alinib alinmadigini kontrol edelim
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} Login Oldunuz!')
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)
