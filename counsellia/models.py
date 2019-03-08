from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import Counsellor, Counsellee


class Appointment(models.Model):
	TYPE = (
		('first', 'First appointment'),
		('follow-up', 'Follow-up appointment'),
		('final', 'Final appointment'),
	)
	description = models.CharField('Short Description', max_length=256, null=True, blank=True)
	counsellee = models.ForeignKey(Counsellee, on_delete=models.CASCADE, null=True)
	counsellor = models.ForeignKey(Counsellor, on_delete=models.CASCADE, null=True)
	time = models.DateField('Appointment Date')
	appointment_type = models.CharField('Appointment Type', max_length=20, choices=TYPE, null=True)
	requested = models.BooleanField(default=True, null=True)
	fixed = models.BooleanField(default=False, null=True)
	held = models.BooleanField(default=False, null=True)
	remarks = models.TextField(null=True, blank=True)
	recommendations = models.TextField(null=True, blank=True)
	counsellee_archived = models.BooleanField(default=False)
	counsellor_archived = models.BooleanField(default=False)
	
	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('counsellee-appointment-detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['time',]


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
	archived = models.BooleanField(default=False, null=True)

	def __str__(self):
		return self.description

	class Meta:
		ordering = ['counsellee', '-time',]