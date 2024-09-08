from django.contrib import admin
from .models import User, Car, Service, Insurance

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Insurance)
