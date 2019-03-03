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
from counsellia.models import Appointment
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

class AppointmentCreateView(LoginRequiredMixin, CreateView):
	model = Appointment
	template_name = 'counsellees/appointment_create.html'
	fields = ['description', 'time', 'counsellor']

	def form_valid(self, form):
		form.instance.counsellee = self.request.user.counselle
		return super().form_valid(form)

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
	paginate_by = 5

	def get_queryset(self):
		user = self.request.user
		return Counsellor.objects.filter(specialties__in=user.counsellee.categories.all()).distinct() 

class CounsellorProfileView(DetailView):
	model = Counsellor
	template_name = 'counsellees/counsellor_profile.html'
	context_object_name = 'counsellor'


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
