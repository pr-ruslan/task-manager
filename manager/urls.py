from django.urls import path, include
from .views import (
    index,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
)


app_name = "manager"


worker_patterns = [
    path('', WorkerListView.as_view(), name="workers-list"),
    path('<int:pk>/', WorkerDetailView.as_view(), name="worker-detail"),
    path('create/', WorkerCreateView.as_view(), name="worker-create"),
    path('<int:pk>/update/', WorkerUpdateView.as_view(), name="worker-update"),
    path('<int:pk>/delete/', WorkerDeleteView.as_view(), name="worker-delete"),
]


urlpatterns = [
    path("", index, name="index"),
    path("workers/", include(worker_patterns)),
]

