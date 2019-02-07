from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views as counsellee_views

from . views import (
	AppointmentListView,
	AppointmentDetailView,
	AppointmentCreateView,
	AppointmentUpdateView,
	AppointmentDeleteView,
	AppointmentCounsellorProfileView,
	CounsellorListView,
	CounsellorProfileView
	)

urlpatterns = [
	
	# home page(appointment list) and user's profile
	path('', AppointmentListView.as_view(), name = 'counsellee-home'),
	path('profile/', counsellee_views.profile_update, name = 'counsellee-profile'),

	path('appointment/<int:pk>/', 
		AppointmentDetailView.as_view(),
		name = 'counsellee-appointment-detail'),
	path('appointment/new/', 
		AppointmentCreateView.as_view(), 
		name = 'counsellee-appointment-create'),
	path('appointment/<int:pk>/update/', 
		AppointmentUpdateView.as_view(), 
		name = 'counsellee-appointment-update'),
	path('appointment/<int:pk>/delete/', 
		AppointmentDeleteView.as_view(),
		name = 'counsellee-appointment-delete'),
	path('appointment/<int:pk>/counsellor/', 
		AppointmentCounsellorProfileView.as_view(),
		name = 'appointment-counsellor'),

	path('counsellors/', CounsellorListView.as_view(),
		name = 'available-counsellors'),

	path('counsellor/<int:pk>/', CounsellorProfileView.as_view(),
		name = 'selected-counsellor-profile'),
	# path('counsellor/<str:username>/profile/', CounsellorProfileView.as_view(),
	# 	name = 'selected-counsellor-profile'),

]