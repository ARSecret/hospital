from rest_framework import routers
from ..views.api import *
from django.urls import path, include

"""
URLы для API, например, 127.0.0.1:8000/api/users - список пользователей системы
"""

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('specialities', SpecialityViewSet)
router.register('doctors', DoctorViewSet)
router.register('patients', PatientViewSet)
router.register('wards', WardViewSet)
router.register('cases', CaseViewSet)

urlpatterns = [
    path('', include(router.urls))
]