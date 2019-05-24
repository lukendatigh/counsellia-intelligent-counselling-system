from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)

from . models import Conversation, Message
from users.models import Counsellor, Counsellee



class CounsellorConversationsView(ListView):
    model = Conversation
    template_name = 'counsellor_conversations.html'
    context_object_name = 'conversations'


class CounsellorDialogueView(ListView, CreateView):
    model = Conversation
    template_name = "counsellor_dialogue.html"
    context_object_name = 'messages'
    # form_class = 


class CounselleeConversationsView(ListView):
    model = Conversation
    template_name = 'counsellee_conversations.html'
    context_object_name = 'conversations'

    def get_queryset(self):
        pass


class CounselleeDialogueView(ListView, CreateView):
    model = Conversation
    template_name = 'counsellee_dialogue.html'
    context_object_name = 'messages'

