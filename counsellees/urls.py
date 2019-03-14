from django.urls import path, include

from . import views as counsellee_views
from . views import (
	AppointmentDetailView,
	AppointmentEditView,
	AppointmentDeleteView,
	CounsellorListView,
	ContactedCounsellorListView,
	CounsellorProfileView,
	AppointmentsUpcomingView,
	AppointmentsRequestedView,
	AppointmentsHeldView,
	AppointmentsArchivedView,
	)


urlpatterns = [
	
	# user's profile
	path('profile/', counsellee_views.profile_update, name = 'counsellee-profile'),


	# notifications
	path('', counsellee_views.counsellee_notifications, name = 'counsellee-notifications'),

	# appointment create, update, delete and view details
	path('counsellor/<int:pk>/appointment/', 
		counsellee_views.appointment_create, 
		name = 'counsellee-appointment-create'),
	path('appointment/<int:pk>/', 
		AppointmentDetailView.as_view(),
		name = 'counsellee-appointment-detail'),
	path('appointment/<int:pk>/edit/',
		AppointmentEditView.as_view(success_url="/counsellee/appointments/upcoming/"), 
		name = 'counsellee-appointment-edit'),
	path('appointment/<int:pk>/delete/',
		AppointmentDeleteView.as_view(),
		name = 'counsellee-appointment-delete'),



	# apoointment lists (pending, upcoming, held, archived)
	path('appointments/upcoming/',
		AppointmentsUpcomingView.as_view(),
		name = 'counsellee-appointments-upcoming'),
	path('appointments/requested/',
		AppointmentsRequestedView.as_view(),
		name = 'counsellee-appointments-requested'),
	path('appointments/held/',
		AppointmentsHeldView.as_view(),
		name = 'counsellee-appointments-held'),
	path('appointments/archived/',
		AppointmentsArchivedView.as_view(),
		name = 'counsellee-appointments-archived'),


	# counsellor list and profile
	path('counsellors/available/', CounsellorListView.as_view(),
		name = 'available-counsellors'),
	path('counsellors/contacted/', ContactedCounsellorListView.as_view(),
		name = 'contacted-counsellors'),
	path('counsellor/<int:pk>/', CounsellorProfileView.as_view(),
		name = 'selected-counsellor-profile'),
	# path('counsellor/<str:username>/profile/', CounsellorProfileView.as_view(),
	# 	name = 'selected-counsellor-profile'),

]