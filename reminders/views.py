from datetime import datetime
from rest_framework.generics import GenericAPIView

from account.models import User
from .models import Reminder
from .serializers import ReminderSerializer
from rest_framework import permissions
from rest_framework.response import Response

# Create your views here.
class ReminderView(GenericAPIView):
  serializer_class = ReminderSerializer
  permission_classes = [permissions.IsAuthenticated]

  def post(self, request):

    serializer = self.get_serializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    reminder = serializer.save(user = request.user)
    serialize_data = self.get_serializer(reminder)
    return Response(serialize_data.data)

  def get(self, request):
    reminder = Reminder.objects.filter(date__gte = datetime.date.today())
    print(reminder)
    return Response(True)
