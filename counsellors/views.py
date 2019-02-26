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
	template_name = 'counsellors/appointment_list.html'
	context_object_name = 'appointments'
	ordering = ['-time']
	paginate_by = 5


class AppointmentDetailView(DetailView):
	model = Appointment
	template_name = 'counsellors/appointment_detail.html'


class AppointmentCreateView(CreateView):
	model = Appointment
	template_name = 'counsellors/appointment_create.html'
	fields = ['title', 'time', 'counsellor']


class AppointmentUpdateView(UpdateView):
	model = Appointment
	field = ['title', 'time']
	template_name = 'counsellors/appointment_update.html'


class AppointmentDeleteView(DeleteView):
	model = Appointment
	context_object_name = 'appointment'
	template_name = 'counsellors/appointment_delete.html'


class ReportCreateView(CreateView):
	model = Report
	template_name = 'counsellors/report_create.html'


class ReportDetail(DetailView):
	model = Report
	template_name = 'counsellors/report_detail.html'

class ReportDeleteView(DeleteView):
	model = Report
	template_name = 'counsellors/report_delete.html'


class CounselleeListView(ListView):
	model = Counsellee
	template_name = 'counsellors/counsellee_list.html'	
	context_object_name = 'counsellees'
	paginate_by = 5	


class CounselleeProfileView(DetailView):
	model = Counsellee
	context_object_name = 'counsellee'
	template_name = 'counsellors/counsellee_profile.html'
		


@login_required
def profile_update(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.counsellor)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your profile has been updated!')
			return redirect('counsellor-schedule')
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.counsellor)

	context = {'u_form': u_form, 'p_form': p_form}
	return render(request, 'counsellors/profile.html', context)