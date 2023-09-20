from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request):
    return HttpResponse("logged into dashboard.")

def logout(request):
    return HttpResponse("logged out of dashboard.")


