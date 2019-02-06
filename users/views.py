from . models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from . forms import CounselleeRegisterForm, CounsellorRegisterForm
from . models import Counsellee, Counsellor

# Create your views here.
def index(request):
	return render(request, 'users/index.html')

def counsellee_register(request):
	if request.method == "POST":
		form = CounselleeRegisterForm(request.POST) # getting the form data and storing in variable
		if form.is_valid(): # checking if form is valid
			user = form.save(commit=False)
			user.is_counsellee = True
			user.save()	# saving form data to database

			# creating matching profile for new account
			counsellee = Counsellee()
			counsellee.user = form.instance
			counsellee.save()

			username = form.cleaned_data.get('username')
			messages.success(request, f'{username}, your account has been created. You are now able to login!')
			return redirect('counsellee-login')
	else:
		form = CounselleeRegisterForm()
	context = {'title': 'Counsellee Signup','form': form}
	return render(request, 'users/counsellee_register.html', context)


def counsellor_register(request):
	if request.method == "POST":
		form = CounsellorRegisterForm(request.POST) # getting the form data and storing in variable
		if form.is_valid(): # checking if form is valid
			user = form.save(commit=False)
			user.is_counsellor = True
			user.save()	# saving form data to database

			# creating matching profile for new account
			counsellor = Counsellor()
			counsellor.user = form.instance
			counsellor.save()

			username = form.cleaned_data.get('username')
			messages.success(request, f'{username}, your account has been created! You are now able to login!')
			return redirect('counsellor-login')
	else:
		form = CounsellorRegisterForm()
	context = {'title': 'Counsellor Signup', 'form': form}
	return render(request, 'users/counsellor_register.html', context)






