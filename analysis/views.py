from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse

from django.views.generic import (
	ListView, 
	DetailView,
	UpdateView,
	DeleteView,
	View,
	)

from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User, Counsellor, Counsellee
from .models import Report

from . forms import TwitterHandleForm

from . wordfrequency import  word_frequency as run_word_frequency
from . sentiment import sentiment as run_sentiment_analysis
from . lda import lda as run_lda



# Report list views (past, archived)
class ReportsPastView(ListView):
	model = Report
	context_object_name = 'reports'
	template_name = 'analysis/reports_past.html'
	
	def get_queryset(self):
		counsellor = self.request.user.counsellor
		return Report.objects.filter(
			counsellor=counsellor,
			archived=False
		)



class ReportsArchivedView(ListView):
	model = Report
	context_object_name = 'reports'
	template_name = 'analysis/reports_archived.html'

	def get_queryset(self):
		counsellor = self.request.user.counsellor
		return Report.objects.filter(
			counsellor=counsellor,
			archived=True
		)




# function view to display charts
def display_charts(request, *args, **kwargs):

	if request.method == "POST":
		form = TwitterHandleForm(request.POST)
		if form.is_valid():
			twitter_handle = request.POST.get('twitter_handle')

			from . fetch_tweets import fetch as fetch_from
			fetched_tweets = fetch_from(twitter_handle)
			mode_frequency = run_word_frequency(fetched_tweets)
			sentiment_percentages = run_sentiment_analysis(fetched_tweets)
			topic_models = run_lda(fetched_tweets)

			word_text = []
			word_frequency = []
			for key, value in mode_frequency.items():
				word_text.append(key)
				word_frequency.append(value)

			sentiment_names = []
			sentiment_amount = []
			for key, value in sentiment_percentages.items():
				sentiment_names.append(key)
				sentiment_amount.append(value)


	else:
		form = TwitterHandleForm()
		twitter_handle = None
		word_text = []
		word_frequency = []
		sentiment_names = []
		sentiment_amount = []
		topic_models = []

	# sentiment_names = ['Positive', 'Negatiive', 'Neutral']
	# sentiment_amount = [55, 5, 40]
	# word_text = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy',
	# 'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy',
	# 'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy',
	# 'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy',]
	# word_frequency = [12, 34, 9, 26, 5, 4, 8, 45,
	# 12, 34, 9, 26, 5, 4, 8, 45,
	# 12, 34, 9, 26, 5, 4, 8, 45,
	# 12, 34, 9, 26, 5, 4, 8, 45]

	context = {
		'handle_form': form,
		'twitter_handle': twitter_handle,
		'sentiment_names': sentiment_names,
		'sentiment_amount': sentiment_amount,
		'word_text': word_text,
		'word_frequency': word_frequency,
		'topic_models': topic_models
	}

	return render(request, 'analysis/charts.html', context)
