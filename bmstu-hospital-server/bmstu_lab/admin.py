from django.contrib import admin

from .models import *

"""
конфигурация админ панели
"""

admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Ward)
admin.site.register(Case)
