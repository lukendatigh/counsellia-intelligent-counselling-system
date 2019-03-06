from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)

from users.models import User, Counsellor, Counsellee
from counsellia.models import Appointment
from .forms import UserUpdateForm, ProfileUpdateForm, AppointmentCreateForm, AppointmentEditForm



# Counsellor Views (list, profile details)
class CounsellorListView(ListView):
	model = Counsellor
	template_name = 'counsellees/counsellor_list.html'
	context_object_name = 'counsellors'
	# ordering = ['rating']
	paginate_by = 5

	def get_queryset(self):
		user = self.request.user
		return Counsellor.objects.filter(specialties__in=user.counsellee.categories.all()).distinct() 


class CounsellorProfileView(DetailView):
	model = Counsellor
	template_name = 'counsellees/counsellor_profile.html'
	context_object_name = 'counsellor'



# Appointment Lists (upcoming, requested, held, archived)
class AppointmentsUpcomingView(ListView):
	model = Appointment
	template_name = 'counsellees/appointments_upcoming.html'
	context_object_name = 'appointments'
	paginate_by = 5 

	def get_queryset(self):
		user = self.request.user
		return Appointment.objects.filter(counsellee=user.counsellee).filter(requested=True).filter(fixed=True)


class AppointmentsRequestedView(ListView):
	model = Appointment
	template_name = 'counsellees/appointments_requested.html'
	context_object_name = 'appointments'
	paginate_by = 5 

	def get_queryset(self):
		user = self.request.user
		return Appointment.objects.filter(counsellee=user.counsellee).filter(requested=True).filter(counsellee_archived=False)


class AppointmentsHeldView(ListView):
	model = Appointment
	template_name = 'counsellees/appointments_held.html'
	context_object_name = 'appointments'
	paginate_by = 5 

	def get_queryset(self):
		user = self.request.user
		return Appointment.objects.filter(counsellee=user.counsellee).filter(held=True)


class AppointmentsArchivedView(ListView):
	model = Appointment
	template_name = 'counsellees/appointments_archived.html'
	context_object_name = 'appointments'
	paginate_by = 5 

	def get_queryset(self):
		user = self.request.user
		return Appointment.objects.filter(counsellee=user.counsellee).filter(counsellee_archived=True)


# General Appointment Views (create, detail, edit, delete)
def appointment_create(request, pk):
	counsellor = Counsellor.objects.get(pk=pk)
	if request.method == 'POST':
		form = AppointmentCreateForm(request.POST)
		if form.is_valid():			
			appointment = form.save(commit=False)
			# import pdb
			# pdb.set_trace()
			instance = request.user
			appointment.counsellor = counsellor
			appointment.counsellee = request.user.counsellee 
			appointment.save()
			messages.success(request, f'Appointment requested successfully!')
			return redirect('available-counsellors')
	else:
		form = AppointmentCreateForm()
	context = {'form': form}
	return render(request, 'counsellees/appointment_create.html', context)


class AppointmentDetailView(DetailView):
	model = Appointment
	context_object_name = 'appointment'
	template_name = 'counsellees/appointment_detail.html'


class AppointmentEditView(UpdateView):
	model = Appointment
	form_class = AppointmentEditForm
	template_name = 'counsellees/appointment_edit.html'


class AppointmentDeleteView(DeleteView):
	model = Appointment
	template_name = 'counsellees/appointment_delete.html'
	context_object_name = 'appointment'
	




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
