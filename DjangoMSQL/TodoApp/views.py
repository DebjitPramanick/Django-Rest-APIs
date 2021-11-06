from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TodoApp.models import TaskList, Task
from TodoApp.serializers import ListSerializer, TaskSerializer

# Create your views here.


@csrf_exempt
def listAPI(req, id=0):
    if req.method == 'GET':
        lists = TaskList.objects.all()
        lists_sl = ListSerializer(lists, many = True)
        return JsonResponse(lists_sl.data, safe=False)

    elif req.method == 'POST':
        list_data = JSONParser().parse(req)
        list_sl = ListSerializer(data = list_data)
        if list_sl.is_valid():
            list_sl.save()
            return JsonResponse("Added.", safe=False)

    elif req.method == 'PUT':
        list_data = JSONParser().parse(req)
        list = TaskList.objects.get(listId = list_data['listId'])
        list_sl = ListSerializer(list, data = list_data)
        if list_sl.is_valid():
            list_sl.save()
            return JsonResponse("Updated.", safe=False)
        return JsonResponse("Failed to update.")

    elif req.method == 'DELETE':
        list = TaskList.objects.get(ListId = id)
        list.delete()
        return JsonResponse("Deleted", safe=False)


@csrf_exempt
def taskAPI(req, id=0):
    if req.method == 'GET':
        tasks = Task.objects.all()
        tasks_sl = TaskSerializer(tasks, many = True)
        return JsonResponse(tasks_sl.data, safe=False)

    elif req.method == 'POST':
        task_data = JSONParser().parse(req)
        task_sl = TaskSerializer(data = task_data)
        if task_sl.is_valid():
            task_sl.save()
            return JsonResponse("Added.", safe=False)

    elif req.method == 'PUT':
        task_data = JSONParser().parse(req)
        task = Task.objects.get(listId = task_data['taskId'])
        task_sl = TaskSerializer(task, data = task_data)
        if task_sl.is_valid():
            task_sl.save()
            return JsonResponse("Updated.", safe=False)
        return JsonResponse("Failed to update.")

    elif req.method == 'DELETE':
        task = Task.objects.get(ListId = id)
        task.delete()
        return JsonResponse("Deleted", safe=False)
