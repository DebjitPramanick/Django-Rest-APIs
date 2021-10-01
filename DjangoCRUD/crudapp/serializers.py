from django.db.models import fields
from rest_framework import serializers
from crudapp.models import Batch, Student

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ('BatchId', 'BatchName')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('StudentId', 'StudentName', 'Age', 'JoiningDate')