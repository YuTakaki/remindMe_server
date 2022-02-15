from django.urls import path
from .views import CalendarTaskView, ReminderView


urlpatterns = [
    path('', ReminderView.as_view()),
    path('month', CalendarTaskView.as_view()),
    path('<str:pk>', ReminderView.as_view()),
    path('<int:pk>', ReminderView.as_view()),
]
