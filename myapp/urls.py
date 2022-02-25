from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='index'),
    path('bca/',views.bca,name='home'),
    path('cba1/',views.cba1,name='cba1'),
]