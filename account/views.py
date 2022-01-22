from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import User
from .serializers import LoginSerializer, RegisterSerializer

# Create your views here.
class RegisterView(GenericAPIView):

  serializer_class = RegisterSerializer
  queryset = User.objects.all()
    
  def post(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print(serializer)

    return Response(serializer.data)


class LoginView(GenericAPIView):

  serializer_class = LoginSerializer

  def get_queryset(self):
    print(self)
    return User.objects.filter()
  
    
  def post(self, request):
    print(request.data['username'])
    # serializer = self.get_serializer(request.data)
    # serializer.is_valid(raise_exception=True)
    # serializer.save()
    # print(serializer)
    return Response([])