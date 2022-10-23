from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from datetime import date
from bmstu_lab.models import *

"""
контроллер для лабы 2
отправляет клиенту созданные шаблонизатором html страницы
это можно использовать только для просмотра информации из браузера человеком
а компьютеру будет неудобно читать информацию в виде html страниц
таким способом будет тяжело сделать, например, мобильное приложение, подключающееся к данному серверу 
"""

def home(request):
    return redirect('doctors')


def doctors(request):
    return render(request, 'doctors.html', {
        'current_date': date.today().strftime('%d.%m.%y'),
        'doctors': Doctor.objects.all()
    })


def patients(request):
    return render(request, 'patients.html', {
        'current_date': date.today().strftime('%d.%m.%y'),
        'patients': Patient.objects.all()
    })


def wards(request):
    return render(request, 'wards.html', {
        'current_date': date.today().strftime('%d.%m.%y'),
        'wards': Ward.objects.all()
    })


def cases(request):
    return render(request, 'cases.html', {
        'current_date': date.today().strftime('%d.%m.%y'),
        'cases': Case.objects.all()
    })


def make_appointment(request, id):
    doctor = Doctor.objects.filter(id=id).first()
    if doctor:
        return render(request, 'make_appointment.html', {
            'current_date': date.today().strftime('%d.%m.%y'),
            'doctor': doctor
        })
    else:
        return HttpResponseNotFound(f'Doctor with id {id} not found')
