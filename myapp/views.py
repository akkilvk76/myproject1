from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def bca(request):
    return render(request,'abc.html')

def cba1(request):
    return render(request,'cba1.html')