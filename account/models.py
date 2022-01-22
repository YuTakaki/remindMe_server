
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  first_name =  models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  username = models.CharField(max_length=200, unique=True)
  email = models.EmailField(unique=True)
  date_joined = models.DateTimeField(auto_now=True)
  password = models.CharField(max_length=1000)

  def __str__(self):
    return self.username