from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . forms import UserForm
# Create your views here.
class SignUp(generic.CreateView):
	template_name= 'Account/SignUp.html'
	form_class=UserForm
	success_url=reverse_lazy('account:login')