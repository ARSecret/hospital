from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# лаба 3
"""
создаём для нашего сервера API
API нужно, чтобы к серверу можно было подключаться с разных устройств
например, с приложения для телефона или из отдельного приложения на компьютере, а не только через браузер

веб сервис - программная служба со стандартизированным API
REST - стиль написания API, набор соглашений о том, как правильно создавать API

используем фреймворк Django REST Framework
в этом файле описаны сериализаторы данных, они преобразуют данные, взятые из модели, в формат JSON
"""


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username']


class SpecialitySerializer(serializers.HyperlinkedModelSerializer):
    doctors = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='doctor-detail'
    )

    class Meta:
        model = Speciality
        fields = ['id', 'url', 'name', 'doctors', 'description']


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    work_record = serializers.IntegerField(read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'url', 'user', 'speciality', 'last_name', 'first_name', 'patronymic', 'photo', 'work_record', 'gender']


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    age = serializers.IntegerField(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'url', 'user', 'first_name', 'last_name', 'patronymic', 'birth_date', 'gender', 'age']


class WardsSerializer(serializers.HyperlinkedModelSerializer):
    patients = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='patient-detail'
    )

    class Meta:
        model = Ward
        fields = ['id', 'url', 'number', 'capacity', 'patients']


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = ['patient', 'doctor', 'ward', 'start_date', 'end_date', 'active', 'description']