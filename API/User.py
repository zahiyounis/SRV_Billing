from rest_framework import serializers
from django.contrib.auth.models import Group, Permission, AbstractUser
from django.db import models



class User(AbstractUser):
    Extension = models.IntegerField(null=True)

    class Meta:
        verbose_name = "User"
        db_table = "api_user"


