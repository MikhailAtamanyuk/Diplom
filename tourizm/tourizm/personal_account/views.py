from django.shortcuts import render, redirect
from .models import Db_user
from .forms import LkForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from crm.models import Order
from crm.forms import OrderForm
from bot.sendmessage import send_telegram
import requests

def lk(request):
    person = request.user.id
    ch = 0


    for i in Db_user.objects.all():
        ch += 1


    if person > ch:
        element = Db_user(first_name='4', second_name='4', email_user='4', phone_user='4', user=request.user)
        element.save()
        form = LkForm()
        db_lk = Db_user.objects.get(id=person)
        return render(request, 'blog/lk.html', {'form': form,
                                            'db_lk': db_lk})
    else:
        db_lk = Db_user.objects.get(id=person)
        form = LkForm()
        return render(request, 'blog/lk.html', {'form': form,
                                            'db_lk': db_lk})


def lk_edit(request):
    form = LkForm()
    person_id = request.user.id
    person = Db_user.objects.get(id=person_id)
    if request.POST:
        person.first_name = request.POST.get('name')
        person.second_name = request.POST.get('surname')
        person.email_user = request.POST.get('email')
        person.phone_user = request.POST.get('phone')
        person.user = request.user
        person.save()
        return render(request, 'blog/edit.html', {'form': form})
    else:
        return render(request, 'blog/edit.html', {'form': form})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'blog/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'first/signupuser.html', {'form': UserCreationForm(),
                                                                 'error': 'Имя уже существует'})
        else:
            return render(request, 'first/signupuser.html', {'form': UserCreationForm(),
                                                             'error': 'Пароли не совпадают'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'blog/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'blog/loginuser.html', {'form': AuthenticationForm(),
                                                            'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('index')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def crm(request):
    form_crm = OrderForm()
    return render(request, 'blog/crm.html', {'form_crm': form_crm})


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        country = request.POST['country']
        city = request.POST['city']
        element = Order(order_name=name, order_phone=phone, order_country=country, order_city=city)
        element.save()
        send_telegram(tg_name=name, tg_phone=phone, tg_country=country, tg_city=city)
        return render(request, 'blog/thanks_page.html')
    else:
        return render(request, 'blog/thanks_page.html')


def weather(request):
    app_id = 'c41091fb908d42b1944203931222808'

    if request.method == 'GET':
        return render(request, template_name='blog/weather.html')

    if request.method == 'POST':
        city = request.POST.get('city')
        if city == '':
            return render(request, template_name='blog/weather.html')
        url = f'http://api.weatherapi.com/v1/current.json?key={app_id}&q={city}&aqi=no'
        res = requests.get(url).json()
        res_curr = res['current']
        res_city = res_curr['temp_c']
        context = {
            'res_city': res_city,
            'city': city
        }
        return render(request, template_name='blog/weather.html', context=context)