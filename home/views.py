from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import Template

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to Jaykay Website Home Page<h1>")
