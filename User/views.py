from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def login(request):
    return render(request,'login.html')

def Is_logged_in(request):
    return render(request,'home.html')
    
def registration(request):
    return render(request,'registration.html')