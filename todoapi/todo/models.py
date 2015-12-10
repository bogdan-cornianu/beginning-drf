from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=200)
    completed = models.BooleanField()
