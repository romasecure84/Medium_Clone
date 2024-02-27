from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
        post_info = request.POST
        email = post_info.get('email')
        email_confirm = post_info.get('email_confirm')
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_name')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        instagram = post_info.get('instagram')
        
        if len(first_name)<3 or len(last_name)<3 or len(email)<3 or len(password)<3:
            messages.warning(request, 'Zehmet olmasa yeterli uzunluqda melumatlar giriniz!')
            return redirect('user_profile:register_view')
        
        if email != email_confirm:
            messages.warning(request, 'Zehmet olmasa Email bilgisini duzgun giriniz!')
            return redirect('user_profile:register_view')
        
        if password != password_confirm:
            messages.warning(request, 'Zehmet olmasa Sifre bilgisini duzgun giriniz!')
            return redirect('user_profile:register_view')
        
        user, created = User.objects.get_or_create(username=email)
        # Eger istifadeci created deyilse daha evvel qeydiyyatdan kecib
        if not created:
            user = authenticate(request, username=email, password=password)            
            if user is not None:
                login(request, user)
                messages.success(request, 'Daha Evvel Uzv Olmusunuz.. Ana Sehifeye Yonlendirildiniz!')                
                return redirect('home_view')
            messages.warning(request, f'{email} adresi sistemde movcuddur, amma login olmadiniz.. Login Sehifesine Yonlendirildiniz..')
            return redirect('user_profile:login_view')

    return render(request, 'user_profile/register.html', context)