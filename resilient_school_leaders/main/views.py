# Import modules
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about_index(request):
    return render(request, 'main/about_index.html')

def faqs_index(request):
    return render(request, 'main/faqs_index.html')

def coming_soon(request):
    return render(request, 'main/coming_soon.html')