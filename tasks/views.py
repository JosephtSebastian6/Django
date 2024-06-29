#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import task
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializar_class =TaskSerializer
    queryset = task.objects.all()