from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    agreed_to_terms = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group,related_name='customuser_set',blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',related_query_name='user',)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True, help_text='Specific permissions for this user.',related_query_name='user',)
