from django.db import models

from django.utils import timezone

from users import (Counsellor, Counsellee)

# Create your models here.
class Conversation(models.Model):
	counsellee = models.ForeignKey(Counsellee, on_delete=models.CASCADE, null=True)
	counsellor = models.ForeignKey(Counsellor, on_delete=models.CASCADE, null=True)
	requested = models.BooleanField(default=True, null=True)
	ongoing = models.BooleanField(default=False, null=True)
	archived = models.BooleanField(default=False, null=True)

	def __str__(self):
		return f"{self.counsellee.user.username} and {self.counsellee.user.username}'s Conversation"


class Message(models.Model):
	conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True)
	text = models.TextField(null=True)
	time = models.DateTimeField(default=timezone.now, null=True)