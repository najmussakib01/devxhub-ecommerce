from django.shortcuts import resolve_url, render
from django.http import Http404
from django.views import View, generic
from .models import UserProfile

# Create your views here.
class UserProfileUpdateView(generic.UpdateView):
    model = UserProfile
    form_class = UserProfile
    template_name = 'user_profile/form.html'
    success_message = "User Updated Success."
    title = "User Profile Update Form"
    