from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'apphome.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': '',
        'Показать содержимое рабочей директории': ''
    }
    
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time =  datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    wordir = os.listdir(path='.')
    context = {'list': wordir}
    return render(request, 'appworkdir.html', context)
    raise NotImplemented
