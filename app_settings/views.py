from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError

# Create your views here.
def main(request):
    return render(request,'app_settings/main.html')
def Registration(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        login = request.POST.get('login')
        password = request.POST.get('password')
        print(login + password)
        # confirm_password = request.POST.get('confirm_password')
        # checkbox = request.POST.get('checkbox')
        # context['email'] = email
        # context['login'] = login
        # context['password']  = password
        # context['confirm_password'] = confirm_password
        if login and password and email:
            if len(password) >= 8:
                if password:
                    try:
                        User.objects.create_user(username = login, email = email, password = password)
                        context['email'] = ''
                        context['login'] = ''
                        context['password']  = ''
                    except IntegrityError:
                        context['error'] = 'Такий користувач вже існує!'
                else:
                    context['error'] = 'Паролі не співпадають!'
            else:
                context['error'] = 'Пароль повинен бути більше ніж 7 символів!'
        else:
            context['error'] = 'Ви не заповнили усі поля(галочку)!'
    return render(request, 'app_settings/registration.html', context)

def Authorization(request):
    context = {}
    if request.user.is_authenticated:
        context['error'] = 'Ти вже авторизувався'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context['username'] = username
        context['password'] = password
        if username and password:
            user = authenticate(username = username, password = password)
            print(user)
            if user:
                print('login succes')
                login(request, user)
                # return redirect('Authorization')
            else:
                context['error'] = 'Логін aбо пароль невірний'
        else:
            context['error'] = 'Заповніть всі поля'
    return render(request, 'app_settings/authorization.html', context)

def log_out(request):
    logout(request)
    return redirect('Main_page')