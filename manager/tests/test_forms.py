from django.test import TestCase
from django.forms import DateTimeInput

from manager.forms import TaskForm, WorkerForm


class TestForms(TestCase):
    def setUp(self):
        self.task_form = TaskForm()
        self.worker_form = WorkerForm()

    def test_task_form_contain_fields(self):
        expected_fields = [
            "name",
            "description",
            "deadline",
            "is_completed",
            "priority",
            "task_type",
            "assignees",
        ]
        for field in expected_fields:
            self.assertIn(field, self.task_form.fields)

    def test_task_form_deadline_widget(self):
        widget = self.task_form.fields["deadline"].widget
        self.assertIsInstance(widget, DateTimeInput)
        self.assertEqual(widget.input_type, "datetime-local")

    def test_worker_form_contain_fields(self):
        expected_fields = ["username", "first_name", "last_name", "email", "position"]
        for field in expected_fields:
            self.assertIn(field, self.worker_form.fields)
