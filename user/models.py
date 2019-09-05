from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from db.basemodel import BaseModel


class User(AbstractUser, BaseModel):
    class Meta:
        db_table = 'db_user'
