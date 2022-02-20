from datetime import date
from rest_framework.generics import GenericAPIView
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

  def get(self, request, pk):
    reminder = {
      'today' : Reminder.objects.filter(date = date.today(), user=request.user).order_by('start_time'),
      'upcomming-events': Reminder.objects.filter(date__gte = date.today(), user=request.user).order_by('date'),
      'important': Reminder.objects.filter(favorite = True, user=request.user).order_by('start_time')
    }
    serialize = self.get_serializer(reminder[pk], many=True)
    return Response(serialize.data)

  def delete(self, _, pk):
    reminder_to_delete = Reminder.objects.get(pk=pk)
    reminder_to_delete.delete()
    return Response(True)


  def put(self, _, pk):
    reminder = Reminder.objects.get(pk=pk)
    reminder.favorite = not reminder.favorite
    reminder.save()
    serializer = self.get_serializer(reminder)
    return Response(serializer.data)

class CalendarTaskView(GenericAPIView):
  serializer_class = ReminderSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    tasks = Reminder.objects.filter(date__month = int(month) + 1, date__year = year)
    serialize = self.get_serializer(tasks, many=True)
    return Response(serialize.data)

class SearchTaskView(GenericAPIView):
  serializer_class = ReminderSerializer
  permission_classes = [ permissions.IsAuthenticated ]

  def get(self, request):
    keyword = request.GET.get('keyword')
    reminder = Reminder.objects.filter(title__icontains = keyword)
    serializer = self.serializer_class(reminder, many=True)
    return Response(serializer.data)