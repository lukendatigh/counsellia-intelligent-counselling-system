from django import forms
from users.models import ( User, Counsellee )

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Counsellee
		fields = ['categories', 'twitter_handle', 'dob', 'gender', 'address', 'phone_number', 'bio', 'interests', 'active', 'image']
		widgets = {
			# 'categories': Select2Widget,
			'categories': forms.SelectMultiple(attrs={'size':10}),
			'dob': forms.TextInput(attrs={'type': 'date'}),
			'bio': forms.Textarea(attrs={'rows':3}),
			'interests': forms.Textarea(attrs={'rows':3}),
		}