from django.db import models


# Create your models here.

class Student(models.Model):
    StudentId = models.AutoField(primary_key=True)
    BatchName = models.CharField(max_length=500, default="Math")
    StudentName = models.CharField(max_length=500)
    Age = models.IntegerField()
    JoiningDate = models.DateField()

class Batch(models.Model):
    BatchId = models.AutoField(primary_key=True)
    BatchName = models.CharField(max_length=500)
