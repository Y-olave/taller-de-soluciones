# Path: seccion243-backend\sistemabackend\productos\urls.py
# Compare this snippet from seccion243-backend\sistemabackend\productos\views.py:
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'inicio.html')

def login(request):
    return render(request, 'login.html')

