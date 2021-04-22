from django.core.validators import (EmailValidator, MinLengthValidator)
from django.contrib.auth.models import AbstractUser 
from django.db import models
import uuid


class Usuario(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length = 200, blank=False)
    last_name = models.CharField(max_length = 200, blank=False)
    email = models.CharField(max_length = 200, unique=True, blank=False)
    username = models.CharField(max_length = 200, unique=True, default='')
    password = models.CharField(max_length = 200, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username