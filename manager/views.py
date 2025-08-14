from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from manager.models import (
    Worker
)

def index(request):
    return HttpResponse("Some test text")


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