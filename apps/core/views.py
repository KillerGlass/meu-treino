from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User,Group
from django.urls import reverse_lazy
#from .forms import UserCreationForm


def homeView(request):      
    return render(request,template_name='home.html')

def sobreView(request):      
    return render(request,template_name='about-us.html')

def contatoView(request):      
    return render(request,template_name='contact.html')
