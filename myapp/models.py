from django.db import models

class User(models.Model):

    username=models.CharField(max_length=25)
    password=models.CharField(max_length=30)
    age=models.CharField(max_length=10)
    address=models.CharField(max_length=40)