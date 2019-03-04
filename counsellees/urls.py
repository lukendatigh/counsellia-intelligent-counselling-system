from django.urls import path, include

from . import views as counsellee_views
from . views import (
	AppointmentDetailView,
	AppointmentUpdateView,
	AppointmentDeleteView,
	CounsellorListView,
	CounsellorProfileView,
	AppointmentPendingView,
	AppointmentUpcomingView,
	AppointmentHeldView,
	AppointmentArchivedView,
	)


urlpatterns = [
	
	# user's profile
	path('profile/', counsellee_views.profile_update, name = 'counsellee-profile'),


	# appointment create, update, delete and view details
	path('counsellor/<int:pk>/appointment/', 
		counsellee_views.appointment_create, 
		name = 'counsellee-appointment-create'),
	path('appointment/<int:pk>/update/', 
		AppointmentUpdateView.as_view(), 
		name = 'counsellee-appointment-update'),
	path('appointment/<int:pk>/delete/',
		AppointmentDeleteView.as_view(),
		name = 'counsellee-appointment-delete'),
	path('appointment/<int:pk>/', 
		AppointmentDetailView.as_view(),
		name = 'counsellee-appointment-detail'),


	# apoointment lists (pending, upcoming, held, archived)
	path('appointments/pending/',
		AppointmentPendingView.as_view(),
		name = 'counsellee-appointments-pending'),
	path('appointments/upcoming/',
		AppointmentUpcomingView.as_view(),
		name = 'counsellee-appointments-upcoming'),
	path('appointments/held/',
		AppointmentHeldView.as_view(),
		name = 'counsellee-appointments-held'),
	path('appointments/archived/',
		AppointmentArchivedView.as_view(),
		name = 'counsellee-appointments-archived'),


	# Viewing list of counsellors and their profiles
	path('counsellors/', CounsellorListView.as_view(),
		name = 'available-counsellors'),
	path('counsellor/<int:pk>/', CounsellorProfileView.as_view(),
		name = 'selected-counsellor-profile'),
	# path('counsellor/<str:username>/profile/', CounsellorProfileView.as_view(),
	# 	name = 'selected-counsellor-profile'),

]