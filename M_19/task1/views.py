from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import Buyer, Game
from django.http import HttpResponse

class Task4(TemplateView):

    def main_page(request):
        return render(request, 'main_page.html')

    def shop_page(request):
        title_shop = 'Игры'
        games = Game.objects.all()
        buy = 'Купить'
        context = {'title': title_shop,
                   'games': games,
                   'buy': buy}

        return render(request, 'shop_page.html', context)

    def basket_page(request):
        title_basket = 'Корзина'
        string1 = 'Пока не робит, приходите завтра!'
        string2 = 'Что ж вы всё время сегодня приходите :)'
        context = {'title': title_basket,
                   'message1': string1,
                   'message2': string2}

        return render(request, 'basket_page.html', context)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':

        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            subscribe = form.cleaned_data['subscribe']

            check_user = Buyer.objects.filter(name=username)

            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif check_user.exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                info['message'] = f'Приветствуем, {username}!'

    else:
        form = UserRegister()
    return render(request, 'registration_page.html', info)

#
# def sign_up_by_html(request):
#     info = {}
#
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = request.POST.get('age')
#         subscribe = request.POST.get('subscribe')
#
#         if int(age) < 18:
#             info['error'] = 'Вы должны быть старше 18'
#         elif password != repeat_password:
#             info['error'] = 'Пароли не совпадают'
#         elif username in users:
#             info['error'] = 'Пользователь уже существует'
#         else:
#             users.append(username)
#             info['message'] = f'Приветствуем, {username}!'
#
#     return render(request, 'registration_page.html', info)

# python manage.py startapp
# django-admin startproject
# python manage.py runserver
