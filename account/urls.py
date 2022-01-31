from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('check', views.UserCheckView.as_view()),
    path('verify', views.UserView.as_view())
]
