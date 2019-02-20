from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)

from users.models import ( User, Counsellor, Counsellee )
from counsellia.models import (Appointment, Report)
from .forms import ( UserUpdateForm, ProfileUpdateForm )



class AppointmentListView(ListView):
	model = Appointment
	template_name = 'counsellees/appointment_list.html'
	context_object_name = 'appointments'
	ordering = ['-time']
	paginate_by = 5 


class AppointmentDetailView(DetailView):
	model = Appointment
	context_object_name = 'appointments'
	template_name = 'counsellees/appointment_detail.html'


class AppointmentCreateView(CreateView):
	model = Appointment
	template_name = 'counsellees/appointment_create.html'
	fields = ['title', 'time', 'counsellor']


class AppointmentUpdateView(UpdateView):
	model = Appointment
	field = ['title', 'time']
	template_name = 'counsellees/appointment_update.html'


class AppointmentDeleteView(DeleteView):
	model = Appointment
	template_name = 'counsellees/appointment_delete.html'
	context_object_name = 'appointment'

class CounsellorListView(ListView):
	model = Counsellor
	template_name = 'counsellees/counsellor_list.html'
	context_object_name = 'counsellors'
	# ordering = ['rating']
	paginate_by = 6


class CounsellorProfileView(DetailView):
	model = Counsellor
	template_name = 'counsellees/counsellor_profile.html'
	context_object_name = 'counsellor'


class CounselleeProfileView(DetailView):
	model = Counsellee
	template_name = 'counsellees/counsellee_profile_view.html'
	context_object_name = 'counsellee'

# class CounselleeMessages(ListView):
# 	model = Conversation

# class CounselleeConversation():



@login_required
def profile_update(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.counsellee)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your profile has been updated!')
			return redirect('counsellee-home')
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.counsellee)

	context = {'u_form': u_form, 'p_form': p_form}
	return render(request, 'counsellees/profile.html', context)
