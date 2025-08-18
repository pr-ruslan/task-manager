from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
        position = models.ForeignKey("Position",
                                     on_delete=models.CASCADE,
                                     related_name="workers",)

        class Meta:
            ordering = ["username"]

        def __str__(self):
            return f"{self.username} ({self.position.name})"


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("UG", "Urgent"),
        ("HP", "High Priority"),
        ("RE", "Regular"),
        ("LO", "Forget About"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        default="RE",
    )
    task_type = models.ForeignKey("TaskType",
                                  on_delete=models.CASCADE,
                                  related_name="tasks",)
    assignees = models.ManyToManyField(
        Worker,
        related_name="tasks",
    )

    def __str__(self):
        return (
            f"{self.name}, priority: {self.get_priority_display()} "
            f"[{'Done' if self.is_completed else 'In progress'}]"
        )