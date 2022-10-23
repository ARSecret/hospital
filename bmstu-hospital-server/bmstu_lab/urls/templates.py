from django.urls import path
from bmstu_lab.views import templates

urlpatterns = [
    path('', templates.home),
    path('doctors/', templates.doctors, name='doctors'),
    path('patients/', templates.patients, name='patients'),
    path('wards/', templates.wards, name='wards'),
    path('cases/', templates.cases, name='cases'),
    path('make_appointment/<int:id>', templates.make_appointment, name='make_appointment')
]
