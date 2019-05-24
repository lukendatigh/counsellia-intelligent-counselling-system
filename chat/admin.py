from django.contrib import admin
from . models import Conversation, Message

# Register your models here.

class ConversationAdmin(admin.ModelAdmin):
	list_display = ['counsellor', 'counsellee']
	list_filter = ['counsellor', 'counsellee']

class MessageAdmin(admin.ModelAdmin):
	list_display = ['text', 'time']
	list_filter = ['time']
		

admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, MessageAdmin)