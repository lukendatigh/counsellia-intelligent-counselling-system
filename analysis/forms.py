from django import forms 
from users.models import Counsellee, Counsellor
from . models import Report



class TwitterHandleForm(forms.Form):
    twitter_handle = forms.CharField(help_text="Enter a handle you wish to analyze.",
    	label = '',)

    def clean_twitter_handle(self):
    	data = self.cleaned_data['twitter_handle']
    	return data