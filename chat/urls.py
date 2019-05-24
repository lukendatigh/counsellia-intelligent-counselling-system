from django.urls import path, include
from . views import (
	CounsellorConversationsView,
	CounsellorDialogueView,
	CounselleeConversationsView,
	CounselleeDialogueView,
	)


urlpatterns = [
	path('counsellees/',
		CounsellorConversationsView.as_view(),
		name = 'counsellor-conversations'),
	path('counsellee/<int:pk>/',
		CounsellorDialogueView.as_view(),
		name = 'counsellor-select-conversation'),
	path('counsellors/',
		CounselleeConversationsView.as_view(),
		name = 'counsellee-conversations',),
	path('counsellor/<int:pk>/',
		CounselleeDialogueView.as_view(),
		name = 'counsellee-select-conversation'),
]