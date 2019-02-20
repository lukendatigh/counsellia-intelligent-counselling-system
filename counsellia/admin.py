from django.contrib import admin
from . models import (Appointment, Report)
from users.models import Category

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Report)