from django.contrib import admin
from . models import (User, Counsellee, Counsellor, Counselling, Category)

# Register your models here.
class CounsellingAdmin(admin.ModelAdmin):
	list_display = ['counsellor', 'counsellee', 'date_contacted']
	list_filter = ['date_contacted'] 

class CounselleeAdmin(admin.ModelAdmin):
	list_display = ['user', 'twitter_handle', 'active']
	list_filter = ['gender', 'active']
		
class CounsellorAdmin(admin.ModelAdmin):
	list_display = ['user', 'qualification', 'available']
	list_filter = ['gender', 'available']

admin.site.register(User)
admin.site.register(Counsellee, CounselleeAdmin)
admin.site.register(Counsellor, CounsellorAdmin)
admin.site.register(Counselling, CounsellingAdmin)
admin.site.register(Category)