from django.shortcuts import render
from django.http import HttpResponse
from .models import coffee


def home(request):
    coffeee = coffee.objects.all()
    return render(request,'home.html',{'coffeee':coffeee})

