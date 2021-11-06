from django.db.models import fields
from rest_framework import serializers
from TodoApp.models import TaskList, Task

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields=('listID', 'listName')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields=('taskID', 'taskName', 'taskStatus', 'listId')