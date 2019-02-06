from django.db import models
from django.contrib.auth.models import User
from users.models import Counsellor, Counsellee


class Appointment(models.Model):
	title = models.CharField(max_length=128, null=True)
	counsellee = models.ForeignKey(Counsellee, on_delete=models.CASCADE, null=True)
	counsellor = models.ForeignKey(Counsellor, on_delete=models.CASCADE, null=True)
	time = models.DateTimeField()
	fixed = models.BooleanField(default=False, null=True)
	held = models.BooleanField(default=False, null=True)
	remarks = models.TextField(null=True)
	recommendations = models.TextField(null=True)
	
	def __str__(self):
		return title


# class Report(models.Model):
#	counsellee = models.ForeignKey(Counsellee, on_delete=models.CASCADE, null=True)
#	counsellor = models.ForeignKey(Counsellor, on_delete=models.CASCADE, null=True)
#	title = models.CharField(max_length=256, null=True)
#	time = models.DateTimeField(default=timezone.now, blank=True, null=True)
#	text = models.TextField(null=True)
#	word_cloud = models.TextField(null=True)
#	handle = models.CharField(max_length=128, null=True)
#	remarks = models.TextField(null=True)

#	def __str__(self):
#		return title
