from django.urls import path, include

from . import views as counsellor_views
from . views import (
		AppointmentDetailView,
		AppointmentEditView,
		AppointmentDeleteView,
		CounselleeListView,
		AppointmentsUpcomingView,
		AppointmentsRequestsView,
		AppointmentsHeldView,
		AppointmentsArchivedView,
	)



urlpatterns = [

	# access analysis urls
	path('report/', include('analysis.urls')),

	# user's profile
	path('profile/', counsellor_views.profile_update, name = 'counsellor-profile'),
	

	# appointment create, update, delete and view details
	path('counsellor/<int:pk>/appointment/', 
		counsellor_views.appointment_create, 
		name = 'counsellor-appointment-create'),
	path('appointment/<int:pk>/', 
		AppointmentDetailView.as_view(),
		name = 'counsellor-appointment-detail'),
	path('appointment/<int:pk>/edit/',
		AppointmentEditView.as_view(success_url = "/counsellor/appointments/requested/"),
		name = 'counsellor-appointment-edit'),
	path('appointment/<int:pk>/delete/',
		AppointmentDeleteView.as_view(),
		name = 'counsellor-appointment-delete'),



	# apoointment lists (pending, upcoming, held, archived)
	path('appointments/upcoming/',
		AppointmentsUpcomingView.as_view(),
		name = 'counsellor-appointments-upcoming'),
	path('appointments/requested/',
		AppointmentsRequestsView.as_view(),
		name = 'counsellor-appointments-requests'),
	path('appointments/held/',
		AppointmentsHeldView.as_view(),
		name = 'counsellor-appointments-held'),
	path('appointments/archived/',
		AppointmentsArchivedView.as_view(),
		name = 'counsellor-appointments-archived'),



	# counsellee list and profile
	path('counsellee/<int:pk>', 
		counsellor_views.counsellee_profile, 
		name = 'selected-counsellee-profile'),
	path('counsellees/', 
		CounselleeListView.as_view(), 
		name = 'counsellor-counsellee-list'),

]