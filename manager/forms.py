from django import forms

from .models import Task, Worker


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "deadline",
            "is_completed",
            "priority",
            "task_type",
            "assignees"
        ]
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
        }


class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "position"
        ]

