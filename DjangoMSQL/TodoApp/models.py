from django.db import models

# Create your models here.

class Task(models.Model):
    taskID = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=50)
    taskStatus = models.BooleanField(default=False)
    listId = models.IntegerField()

class List(models.Model):
    listID = models.AutoField(primary_key=True)
    listName = models.CharField(max_length=50)