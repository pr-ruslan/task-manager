from django.db.models import Q
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

    return render(
        request,
        "manager/index.html",
        {
            "tasks_count": tasks_count,
            "tasks_incomplete_count": tasks_incomplete_count,
            "workers_count": workers_count,
        },
    )


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker

    def get_queryset(self):
        self.queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            self.queryset = self.queryset.filter(
                Q(first_name__icontains=q) | Q(username__icontains=q)
            )
        return self.queryset

    class Meta:
        ordering = ["username"]


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
        q = self.request.GET.get("q")

        if self.request.GET.get("status") == "incompleted":
            queryset = queryset.filter(is_completed=False)
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(description__icontains=q)
            )

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
    success_url = reverse_lazy("manager:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "manager/confirm_delete.html"
    success_url = reverse_lazy("manager:task-list")
