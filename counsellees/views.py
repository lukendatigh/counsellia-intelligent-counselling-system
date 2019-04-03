from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)

from users.models import User, Counsellor, Counsellee, Counselling
from counsellia.models import Appointment
from .forms import UserUpdateForm, ProfileUpdateForm, AppointmentCreateForm, AppointmentEditForm



# Counsellor Views 
# (list of available counsellors, contacted counsellors, and counsellor profile)
class CounsellorListView(ListView):
	model = Counsellor
	template_name = 'counsellees/counsellor_list.html'
	context_object_name = 'counsellors'
	# ordering = ['rating']
	paginate_by = 5

	def get_queryset(self):
		counsellee = self.request.user.counsellee
		return Counsellor.objects.filter(specialties__in=counsellee.categories.all()).distinct() 


class ContactedCounsellorListView(ListView):
	model = Counsellor
	template_name = 'counsellees/counsellor_contacted_list.html'
	context_object_name = 'counsellors'

	def get_queryset(self):
		counsellee = self.request.user.counsellee
		return Counsellor.objects.filter(counsellees=counsellee).distinct()
	

def counsellor_profile(request, pk):
	counsellee = request.user.counsellee
	counsellor = Counsellor.objects.get(pk=pk)
	appointments = Appointment.objects.filter(
		counsellor=counsellor).filter(
		counsellee=counsellee
		)
	context = {'counsellor': counsellor, 'appointments': appointments}
	return render(request, 'counsellees/counsellor_profile.html', context)



		

# Appointment Lists (upcoming, requested, held, archived)
class AppointmentsUpcomingView(ListView):
	model = Appointment
	template_name = 'counsellees/appointments_upcoming.html'
	context_object_name = 'appointments'
	paginate_by = 5 

	def get_queryset(self):
		counsellee = self.request.user.counsellee
		return Appointment.objects.filter(
			counsellee=counsellee).filter(
			requested=True).filter(
			fixed=True).filter(
			held=False).filter(
			counsellee_archived=False)


class AppointmentsRequestedView(ListView):
	model = Appointment
	template_name = 'counsellees/appointments_requested.html'
	context_object_name = 'appointments'
	paginate_by = 5 

	def get_queryset(self):
		counsellee = self.request.user.counsellee
		return Appointment.objects.filter(
			counsellee=counsellee).filter(
			requested=True).filter(
			fixed=False).filter(
			held=False).filter(
			counsellee_archived=False)


class AppointmentsHeldView(ListView):
	model = Appointment
	template_name = 'counsellees/appointments_held.html'
	context_object_name = 'appointments'
	paginate_by = 5 

	def get_queryset(self):
		counsellee = self.request.user.counsellee
		return Appointment.objects.filter(
			counsellee=counsellee).filter(
			requested=True).filter(
			held=True).filter(
			counsellee_archived=False)


class AppointmentsArchivedView(ListView):
	model = Appointment
	template_name = 'counsellees/appointments_archived.html'
	context_object_name = 'appointments'
	paginate_by = 5 

	def get_queryset(self):
		counsellee = self.request.user.counsellee
		return Appointment.objects.filter(
			counsellee=counsellee).filter(
			counsellee_archived=True)





# General Appointment Views (create, detail, edit, delete)
def appointment_create(request, pk):
	counsellee = request.user.counsellee
	counsellor = Counsellor.objects.get(pk=pk)
	if request.method == 'POST':
		form = AppointmentCreateForm(request.POST)
		if form.is_valid():			
			appointment = form.save(commit=False)
			appointment.counsellee = counsellee
			appointment.counsellor = counsellor
			appointment.save()
			# record contacted status
			if not Counselling.objects.filter(counsellor=counsellor, counsellee=counsellee).exists():
				new_record = Counselling(counsellor = counsellor, counsellee = counsellee) 
				new_record.save()
			
			messages.success(request, f'Appointment requested successfully!')
			return redirect('counsellee-appointments-requested')
	else:
		form = AppointmentCreateForm()
	context = {'form': form}
	return render(request, 'counsellees/appointment_create.html', context)


class AppointmentDetailView(DetailView):
	model = Appointment
	context_object_name = 'appointment'
	template_name = 'counsellees/appointment_detail.html'


class AppointmentEditView(SuccessMessageMixin, UpdateView):
	model = Appointment
	form_class = AppointmentEditForm
	template_name = 'counsellees/appointment_edit.html'
	success_message = "Appointment edited successfully!"


class AppointmentDeleteView(SuccessMessageMixin, DeleteView):
	model = Appointment
	template_name = 'counsellees/appointment_confirm_delete.html'
	context_object_name = 'appointment'
	success_url = '/counsellee/appointments/upcoming/'
	success_message = "Appointment Deleted!"




@login_required
def profile_update(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.counsellee)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your profile has been updated!')
			return redirect('counsellee-appointments-upcoming')
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.counsellee)

	context = {'u_form': u_form, 'p_form': p_form}
	return render(request, 'counsellees/profile.html', context)



def counsellee_notifications(request):
	counsellee = request.user.counsellee 
	upcoming_appointments = Appointment.objects.filter(
			counsellee=counsellee).filter(
			requested=True).filter(
			fixed=True).filter(
			held=False).filter(
			counsellee_archived=False)
	#filter(fixed=True).filter(held=False).filter(counsellee_archived=False)
	appointments_count = upcoming_appointments.count()
	context = {'appointments_count': appointments_count, 'upcoming_appointments': upcoming_appointments}
	return render(request, 'counsellia/counsellee_subbbase.html', context)
