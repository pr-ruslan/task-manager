from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from manager.forms import WorkerForm, TaskForm
from manager.models import (
    Worker,
    Task,
)


@login_required
def index(request):
    tasks_count = Task.objects.count()
    tasks_incomplete_count = Task.objects.filter(is_completed=False).count()
    workers_count = Worker.objects.count()

    return render(request, "manager/index.html", {
        "tasks_count": tasks_count,
        "tasks_incomplete_count": tasks_incomplete_count,
        "workers_count": workers_count,
    })



class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker

    class Meta:
        ordering = ['username']


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy("manager:workers-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy("manager:workers-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    template_name = "manager/confirm_delete.html"
    success_url = reverse_lazy("manager:workers-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get("uncompleted"):
            queryset = queryset.filter(is_completed=False)
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")

class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:tasks-list")

class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "manager/confirm_delete.html"
    success_url = reverse_lazy("manager:task-list")
