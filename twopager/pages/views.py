from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello Word")

def poka(request):
    return HttpResponse("Poka Word")

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ResumePageView(TemplateView):
    template_name = "resume.html"