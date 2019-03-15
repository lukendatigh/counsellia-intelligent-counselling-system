from django.db import models

from django.utils import timezone

from users.models import Counsellor, Counsellee

# Create your models here.
class Report(models.Model):
	counsellee = models.ForeignKey(Counsellee, on_delete=models.CASCADE, null=True)
	counsellor = models.ForeignKey(Counsellor, on_delete=models.CASCADE, null=True)
	description = models.CharField('short description', max_length=256, null=True)
	time = models.DateTimeField(default=timezone.now, blank=True, null=True)
	text = models.TextField(blank=True, null=True)
	topic = models.TextField(blank=True, null=True)
	word_count = models.TextField(blank=True, null=True)
	sentiment = models.TextField('sentiment analysis', null=True)
	remarks = models.TextField(blank=True, null=True)
	archived = models.BooleanField(default=False)

	def __str__(self):
		return self.description

	class Meta:
		ordering = ['counsellee', '-time',]