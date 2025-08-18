from django.urls import path, include
from .views import (
    index,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)


app_name = "manager"


workers_patterns = [
    path("", WorkerListView.as_view(), name="workers-list"),
    path('<int:pk>/', WorkerDetailView.as_view(), name="worker-detail"),
    path('create/', WorkerCreateView.as_view(), name="worker-create"),
    path('<int:pk>/update/', WorkerUpdateView.as_view(), name="worker-update"),
    path('<int:pk>/delete/', WorkerDeleteView.as_view(), name="worker-delete"),
]

tasks_patterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path('<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
    path('create/', TaskCreateView.as_view(), name="task-create"),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name="task-update"),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name="task-delete"),
]


urlpatterns = [
    path("", index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("workers/", include(workers_patterns)),
    path("tasks/", include(tasks_patterns)),
]

