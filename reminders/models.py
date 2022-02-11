from django.db.models.deletion import CASCADE
from django.db import models

from account.models import User

# Create your models here.
class Reminder(models.Model):
  title = models.CharField(max_length=100)
  start_time = models.TimeField()
  end_time = models.TimeField(null=True)
  date = models.DateField()
  favorite = models.BooleanField(default=False)
  note = models.TextField()
  user = models.ForeignKey(User, related_name='reminders', on_delete=CASCADE)

  def __str__(self):
      return self.title