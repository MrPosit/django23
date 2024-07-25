from .models import CustomUser
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from .forms import SignUpForm
from django.views.generic import CreateView

def home(request):
    return render(request, 'home.html')

class SignUp(CreateView):
    model = CustomUser
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
