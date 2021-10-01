from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from crudapp.models import Batch, Student
from crudapp.serializers import BatchSerializer, StudentSerializer

# Create your views here.

@csrf_exempt
def batchAPI(request, id=0):
    if request.method == 'GET':
        batch = Batch.objects.all()
        batch_sl = BatchSerializer(batch, many=True)
        return JsonResponse(batch_sl.data, safe=False)

    elif request.method == 'POST':
        batch_data = JSONParser().parse(request)
        batch_sl = BatchSerializer(data=batch_data)
        if batch_sl.is_valid():
            batch_sl.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)

    elif request.method == 'PUT':
        batch_data = JSONParser().parse(request)
        batch = Batch.objects.get(BatchId=batch_data['BatchId'])
        batch_sl = BatchSerializer(batch, data=batch_data)
        if batch_sl.is_valid():
            batch_sl.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE':
        batch = Batch.objects.get(BatchId=id)
        batch.delete()
        return JsonResponse("Deleted successfully", safe=False)



@csrf_exempt
def studentAPI(request, id=0):
    if request.method == 'GET':
        student = Student.objects.all()
        student_sl = StudentSerializer(student, many=True)
        return JsonResponse(student_sl.data, safe=False)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_sl = StudentSerializer(data=student_data)
        if student_sl.is_valid():
            student_sl.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)

    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = Student.objects.get(StudentId=student_data['StudentId'])
        student_sl = StudentSerializer(student, data=student_data)
        if student_sl.is_valid():
            student_sl.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE':
        student = Student.objects.get(StudentId=id)
        student.delete()
        return JsonResponse("Deleted successfully", safe=False)