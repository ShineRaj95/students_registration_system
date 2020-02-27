from django.db import models

# Create your models here.


"""Class represents a student. An object of this model represents a row
in the db table. Each property in the class represents a column in the
table
"""
class Students(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250,unique=True)
    age = models.CharField(max_length=10)
    phone = models.CharField(max_length=15,unique=True)
    address = models.TextField()
    gender = models.CharField(max_length=15)
    course = models.CharField(max_length=15)