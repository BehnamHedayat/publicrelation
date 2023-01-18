from django.shortcuts import render
from django.http import JsonResponse

from .models import User, Skills

# Create your views here.

def home(request):
    return render(request,'regster/index.html')
