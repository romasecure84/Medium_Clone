from django.shortcuts import render

def login_view(request):
    # login olan istifadeci birbasa ana sehifeye getsin
    context = dict()
    return render(request, 'user_profile/login.html', context)
