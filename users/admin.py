from django.contrib import admin
from . models import (User, Counsellee, Counsellor)

# Register your models here.
admin.site.register(User)
admin.site.register(Counsellee)
admin.site.register(Counsellor)