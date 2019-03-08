from django.contrib import admin
from . models import (Appointment, Report)
from users.models import Category

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
	list_display = ['description', 'counsellor', 'counsellee', 'time']
	list_filter = ['time', 'counsellor', 'counsellee']


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Report)