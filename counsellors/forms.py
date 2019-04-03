from django import forms
from users.models import User, Counsellor
from counsellia.models import Appointment


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
		help_texts = {
			'username': None,
		}

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Counsellor
		fields = ['specialties', 'quote', 'image', 'dob', 'gender', 'website', 'address', 'phone_number', 'bio', 'qualification', 'available']
		widgets = {
			'specialties': forms.SelectMultiple(attrs={'size':12}),
			'dob': forms.TextInput(attrs={'type': 'date'}),
			'bio': forms.Textarea(attrs={'rows':3}),
			'qualification': forms.Textarea(attrs={'rows':3}),
		}


class AppointmentCreateForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ['description', 'remarks', 'time', 'appointment_type']
		widgets = {
			'time': forms.DateInput(attrs={'type': 'date'}),
			'remarks': forms.Textarea(attrs={'rows':4}),
		}


class AppointmentEditForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ['description', 'remarks', 'recommendations', 'fixed', 'held', 'time', 'counsellor_archived']
		widgets = {
			'time': forms.DateInput(attrs={'type': 'date'}),
			'recommendations': forms.Textarea(attrs={'rows':3}),
			'remarks': forms.Textarea(attrs={'rows':4}),
		}