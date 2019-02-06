from django import forms
from users.models import ( User, Counsellee )

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Counsellee
		fields = ['image', 'dob', 'gender', 'address', 'phone_number', 'bio', 'interests']
		widgets = {
			'bio': forms.Textarea(attrs={'rows':3}),
			'interests': forms.Textarea(attrs={'rows':3}),
		}