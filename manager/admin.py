from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Worker, Position, TaskType, Task


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Additional Info", {"fields": ("position",)}),)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "position",
        "is_staff",
        "is_superuser",
    )


admin.site.register(Position)
admin.site.register(TaskType)
admin.site.register(Task)
