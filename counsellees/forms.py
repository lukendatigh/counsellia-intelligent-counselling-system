from django import forms
from users.models import User, Counsellee, Counsellor
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
		model = Counsellee
		fields = ['categories', 'twitter_handle', 'dob', 'gender', 'address', 'phone_number', 'bio', 'interests', 'active', 'image']
		widgets = {
			'categories': forms.SelectMultiple(attrs={'size':16}),
			'dob': forms.TextInput(attrs={'type': 'date'}),
			'bio': forms.Textarea(attrs={'rows':3}),
			'interests': forms.Textarea(attrs={'rows':3}),
		}


class AppointmentCreateForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ['description', 'time', 'appointment_type']
		widgets = {
			'time': forms.DateInput(attrs={'type': 'date'}),
		}


class AppointmentEditForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ['description', 'remarks', 'time', 'counsellee_archived']
		widgets = {
		'time': forms.DateInput(attrs={'type': 'date'}),
		}