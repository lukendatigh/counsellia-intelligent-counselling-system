from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)

from users.models import User, Counsellor, Counsellee
from counsellia.models import Appointment
from .forms import (
	UserUpdateForm,
	ProfileUpdateForm,
	AppointmentCreateForm,
	AppointmentEditForm,
	)



# Counsellee Views
class CounselleeListView(ListView):
	model = Counsellee
	template_name = 'counsellors/counsellee_list.html'	
	context_object_name = 'counsellees'
	paginate_by = 5	


def counsellee_profile(request, pk):
	counsellor = request.user.counsellor
	counsellee = Counsellee.objects.get(pk=pk)
	appointments = Appointment.objects.filter(
		counsellor=counsellor).filter(
		counsellee=counsellee
		)
	context = {'counsellee': counsellee, 'appointments': appointments}
	return render(request, 'counsellors/counsellee_profile.html', context)



# Appointment Lists (upcoming, requests, held, archived)
class AppointmentsUpcomingView(ListView):
	model = Appointment
	context_object_name = 'appointments'
	template_name = 'counsellors/appointments_upcoming.html'
	paginate_by = 5

	def get_queryset(self):
		counsellor = self.request.user.counsellor
		return Appointment.objects.filter(
			counsellor=counsellor).filter(
			requested=True).filter(
			fixed=True).filter(
			held=False).filter(
			counsellor_archived=False)


class AppointmentsRequestsView(ListView):
	model = Appointment
	context_object_name = 'appointments'
	template_name = 'counsellors/appointments_requests.html'
	paginate_by = 5

	def get_queryset(self):
		counsellor = self.request.user.counsellor
		return Appointment.objects.filter(
			counsellor=counsellor).filter(
			requested=True).filter(
			fixed=False).filter(
			held=False).filter(
			counsellor_archived=False)


class AppointmentsHeldView(ListView):
	model = Appointment
	context_object_name = 'appointments'
	template_name = 'counsellors/appointments_held.html'
	paginate_by = 5

	def get_queryset(self):
		counsellor = self.request.user.counsellor
		return Appointment.objects.filter(
			counsellor=counsellor).filter(
			requested=True).filter(
			held=True).filter(
			counsellor_archived=False)


class AppointmentsArchivedView(ListView):
	model = Appointment
	context_object_name = 'appointments'
	template_name = 'counsellors/appointments_archived.html'
	paginate_by = 5

	def get_queryset(self):
		counsellor = self.request.user.counsellor
		return Appointment.objects.filter(
			counsellor=counsellor).filter(
			counsellor_archived=True)
	




# General Appointment Views (create, detail, edit, delete)
def appointment_create(request, pk):
	counsellor = request.user.counsellor
	counsellee =  Counsellee.objects.get(pk=pk)
	if request.method == 'POST':
		form = AppointmentCreateForm(request.POST)
		if form.is_valid():			
			appointment = form.save(commit=False)
			appointment.counsellee = counsellee
			appointment.counsellor = counsellor
			appointment.fixed = True
			appointment.save()
			
			messages.success(request, f'Appointment created successfully!')
			return redirect('counsellor-appointments-upcoming')
	else:
		form = AppointmentCreateForm()
	context = {'form': form}
	return render(request, 'counsellors/appointment_create.html', context)


class AppointmentDetailView(DetailView):
	model = Appointment
	context_object_name = 'appointment'
	template_name = 'counsellors/appointment_detail.html'


class AppointmentEditView(UpdateView):
	model = Appointment
	form_class = AppointmentEditForm
	template_name = 'counsellors/appointment_edit.html'
	success_message = "Appointment edited successfully!"


class AppointmentDeleteView(DeleteView):
	model = Appointment
	context_object_name = 'appointment'
	template_name = 'counsellors/appointment_confirm_delete.html'
	success_url = '/counsellor/appointments/upcoming/'
	success_message = "Appointment Deleted!"


	


# Report Views

@login_required
def profile_update(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.counsellor)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your profile has been updated!')
			return redirect('counsellor-appointments-upcoming')
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.counsellor)

	context = {'u_form': u_form, 'p_form': p_form}
	return render(request, 'counsellors/profile.html', context)


@login_required
def counsellor_notifications(request):
	counsellor = request.user.counsellor
	upcoming_appointments = Appointments.objects.filter(
		counsellor=counsellor).filter(
		held=False).filter(
		counsellee_archived=False
	)
	#filter(fixed=True).filter(held=False).filter(counsellor_archived=False)
	appointments_count = upcoming_appointments.count()
	context = {'appointments_count': appointments_count}
	return render(request, 'counsellia/counsellor_subbbase.html', context)
