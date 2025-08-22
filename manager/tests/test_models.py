from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from manager.models import (Position,
                            Task,
                            TaskType)

class ModelTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="TestPosition")

        self.user = get_user_model().objects.create_user(
            password="pbkdf",
            username="alice",
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com",
            is_staff=False,
            is_active=True,
            date_joined="2025-08-13T12:00:00Z",
            position=self.position,
        )
        self.user.save()

        self.task_type = TaskType.objects.create(
            name="TestTaskType",
        )

        self.task = Task.objects.create(
            name="TestTask",
            description="TestTask Description",
            deadline=now(),
            is_completed=False,
            priority="UG",
            task_type=self.task_type,
        )
        self.task.assignees.set([self.user])

    def test_worker_string(self):
        self.assertEqual(str(self.user), f"{self.user.username} ({self.user.position.name})")

    def test_task_string(self):
        self.assertEqual(
            str(self.task), (
                f"{self.task.name}, priority: {self.task.get_priority_display()} "
                f"[{'Done' if self.task.is_completed else 'In progress'}]"
            )
        )

    def test_password_is_correct(self):
        self.assertTrue(self.user.check_password("pbkdf"))

    def test_invalid_priority(self):
        with self.assertRaises(ValidationError):
            self.task.priority = "AB"
            self.task.full_clean()

    def test_correct_assignees_label(self):
        assignees_label = self.task._meta.get_field("assignees").verbose_name
        self.assertEqual("assignees", assignees_label)