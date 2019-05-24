from django.urls import path, include
from . import views as users_views
from counsellees import views as counsellee_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', users_views.index, name = 'index-page'),
	path('counsellee/', include('counsellees.urls')),
	path('counsellor/', include('counsellors.urls')),
	
	# Login view
	path('counsellee-login/', auth_views.LoginView.as_view(template_name = 'users/counsellee_login.html'), 
		name = 'counsellee-login'),
	path('counsellee-register/', users_views.counsellee_register, 
		name='counsellee-register'),


	path('counsellor-login/', auth_views.LoginView.as_view(template_name = 'users/counsellor_login.html'), 
			name = 'counsellor-login'),
	path('counsellor-register/', users_views.counsellor_register, 
		name='counsellor-register'),

	path('counsellee-logout/', auth_views.LogoutView.as_view(template_name = 'users/counsellee_logout.html'), 
		name = 'counsellee-logout'),
	path('counsellor-logout/', auth_views.LogoutView.as_view(template_name = 'users/counsellor_logout.html'), 
		name = 'counsellor-logout'),
]