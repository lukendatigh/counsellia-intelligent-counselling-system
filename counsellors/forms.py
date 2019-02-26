from django import forms
from users.models import ( User, Counsellor )

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']
		help_texts = {
			'username': None,
		}

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Counsellor
		fields = ['specialties', 'quote', 'image', 'dob', 'gender', 'website', 'address', 'phone_number', 'bio', 'qualification', 'available']
		widgets = {
			'specialties': forms.SelectMultiple(attrs={'size':9}),
			'dob': forms.TextInput(attrs={'type': 'date'}),
			'bio': forms.Textarea(attrs={'rows':3}),
			'qualification': forms.Textarea(attrs={'rows':3}),
		}