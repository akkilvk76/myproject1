from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
    return render(request,'home.html')

def bca(request):
    return render(request,'abc.html')

def cba1(request):
    return render(request,'cba1.html')

def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['pswd']
        age=request.POST['age']
        address=request.POST['adrs']
        userdata=User(username=username,password=password,age=age,address=address)  
        userdata.save()
        return render(request,'signup.html')
    else:
        return render(request,'signup.html')