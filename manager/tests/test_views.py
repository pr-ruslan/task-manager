from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.timezone import now

from manager.models import Position, Task, TaskType


GROUP_URL_NAMES = [
    "workers-list",
    "worker-create",
    "task-list",
    "index",
    "task-create",
]

DETAILED_URL_VIEWS = [
    "worker-detail",
    "worker-update",
    "worker-delete",
    "task-detail",
    "task-update",
    "task-delete",
]


APP_NAME = "manager"


class PublicViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_views_unauthorized(self):
        for url_name in DETAILED_URL_VIEWS:
            url = reverse(f"{APP_NAME}:{url_name}", args=[1, ])
            response = self.client.get(url)
            self.assertNotEquals(response.status_code, 200)

        for url_name in GROUP_URL_NAMES:
            url = reverse(f"{APP_NAME}:{url_name}")
            response = self.client.get(url)
            self.assertNotEquals(response.status_code, 200)


class PrivateViewTest(TestCase):
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

        self.client.force_login(self.user)

    def test_uses_correct_template(self):
        response = self.client.get(reverse(f"{APP_NAME}:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/index.html")

    def test_worker_list_view(self):
        res = self.client.get(reverse("manager:workers-list"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "manager/worker_list.html")
        self.assertEqual(list(res.context["worker_list"]), [self.user])

    def test_worker_create_view(self):
        res = self.client.post(reverse("manager:worker-create"), {
            "username": "newworker",
            "password": "password123",
            "first_name": "New",
            "last_name": "Worker",
            "position": self.position.pk, # Add this line
        })
        self.assertRedirects(res, reverse("manager:workers-list"))
        self.assertTrue(get_user_model().objects.filter(username="newworker").exists())

    def test_worker_list_view_search(self):
        res = self.client.get(reverse("manager:workers-list") + "?q=alic")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["worker_list"]), 1)
        self.assertEqual(res.context["worker_list"][0].username, "alice")