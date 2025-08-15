from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.models import (
    Worker,
    Task,
    Position,
    TaskType,
)

def index(request):
    return render(request, "adminlte/index.html")



class WorkerListView(generic.ListView):
    model = Worker

    class Meta:
        ordering = ['username']


class WorkerDetailView(generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    fields = '__all__'


class WorkerUpdateView(generic.UpdateView):
    model = Worker


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:workers-list")


class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    model = Task


class TaskDeleteView(generic.DeleteView):
    model = Task