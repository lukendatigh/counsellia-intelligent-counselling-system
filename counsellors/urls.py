from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views as counsellor_views

from . views import (
		AppointmentListView,
		AppointmentDetailView,
		AppointmentCreateView,
		AppointmentUpdateView,
		AppointmentDeleteView,
		CounselleeListView,
		CounselleeProfileView,
	)

urlpatterns = [
	path('profile/', counsellor_views.profile_update, name = 'counsellor-profile'),
	
	path('counsellee/<int:pk>', CounselleeProfileView.as_view(), name = 'selected-counsellee-profile'),
	path('', AppointmentListView.as_view(), name = 'counsellor-schedule'),	
	path('counsellees', CounselleeListView.as_view(), name = 'counsellor-counsellee-list'),

]