from django.contrib import admin
from . models import (User, Counsellee, Counsellor, Counselling, Category)

# Register your models here.
admin.site.register(User)
admin.site.register(Counsellee)
admin.site.register(Counsellor)
admin.site.register(Counselling)
admin.site.register(Category)