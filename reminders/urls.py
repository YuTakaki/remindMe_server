from django.urls import path
from .views import ReminderTodayView, ReminderView


urlpatterns = [
    path('', ReminderView.as_view()),
    path('today', ReminderTodayView.as_view())
]
