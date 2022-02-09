from rest_framework.serializers import ModelSerializer
from .models import Reminder

class ReminderSerializer(ModelSerializer):
  class Meta:
    model = Reminder
    fields = '__all__'
    extra_kwargs = {
      'id' : {
        'read_only' : True
      },
      'favorite' : {
        'read_only' : True
      },
      'user' : {
        'read_only' : True
      }
    }