from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views as counsellor_views

from . views import (
		AppointmentListView,
		AppointmentDetailView,
		AppointmentCreateView,
		AppointmentUpdateView,
		AppointmentDeleteView,
		CounselleeProfileView,
	)

urlpatterns = [

	# home page(appointment list) and user's profile
	path('', AppointmentListView.as_view(), name = 'counsellor-home'),
	path('profile/', counsellor_views.profile_update, name = 'counsellor-profile'),

]