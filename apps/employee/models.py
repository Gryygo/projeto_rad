from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="employee")
    can_create = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    can_create_user = models.BooleanField(default=False)
    can_edit_user = models.BooleanField(default=False)
    can_delete_user = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='created_employee', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user)