from django import forms
from django.db import transaction
from . models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Counsellee, Counsellor



class CounselleeRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	# @transaction.atomic
	# def save(self):
	# 	user = super().save(commit=False)
	# 	user.save()
	# 	counsellee = Counsellee.objects.create(user=user)
	# 	counsellee.save()
	# 	return user


class CounsellorRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	# @transaction.atomic
	# def save(self):
	# 	user = super().save(commit=False)
	# 	user.save()
	# 	counsellor = Counsellor.objects.create(user=user)
	# 	counsellor.save()
	# 	return user