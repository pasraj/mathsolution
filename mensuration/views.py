from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def circle(request):
    return HttpResponse("<h1> Circle function</h1>")
