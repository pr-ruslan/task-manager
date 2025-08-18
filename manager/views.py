from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from manager.forms import WorkerForm, TaskForm
from manager.models import (
    Worker,
    Task,
    Position,
    TaskType,
)

def index(request):
    tasks_count = Task.objects.count()
    tasks_incomplete_count = Task.objects.filter(is_completed=False).count()
    workers_count = Worker.objects.count()

    return render(request, "manager/index.html", {
        "tasks_count": tasks_count,
        "tasks_incomplete_count": tasks_incomplete_count,
        "workers_count": workers_count,
    })




class WorkerListView(generic.ListView):
    model = Worker

    class Meta:
        ordering = ['username']


class WorkerDetailView(generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy("manager:workers-list")


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy("manager:workers-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:workers-list")


class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:tasks-list")

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:tasks-list")

class TaskDeleteView(generic.DeleteView):
    model = Task