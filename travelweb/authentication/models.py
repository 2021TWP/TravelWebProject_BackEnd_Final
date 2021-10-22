from django.db import models
from django.contrib.auth.models import AbstractUser
from schedule.models import Schedule


class UserGroup(models.Model):
    group_name = models.CharField(max_length=20, blank=False, unique=True)
    pin = models.CharField(max_length=8, blank=False)
    schedules = models.ManyToManyField(Schedule, blank=True)

    def __str__(self):
        return self.group_name


class UserInfo(AbstractUser):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True, blank=False)
    g_id = models.ManyToManyField(UserGroup, blank=True)

    def __str__(self):
        return self.username

