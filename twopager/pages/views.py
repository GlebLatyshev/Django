from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello Word")

def poka(request):
    return HttpResponse("Poka Word")