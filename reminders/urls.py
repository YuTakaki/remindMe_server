from django.urls import path
from .views import ReminderView


urlpatterns = [
    path('', ReminderView.as_view()),
    path('<str:pk>', ReminderView.as_view()),
]
