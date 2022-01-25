from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import LoginSerializer, RegisterSerializer

# Create your views here.
class RegisterView(GenericAPIView):

  serializer_class = RegisterSerializer
  queryset = User.objects.all()
    
  def post(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    return Response({
      'user': serializer.data,
      'token': str(refresh.access_token),
    })


class LoginView(GenericAPIView):

  serializer_class = LoginSerializer

  def get_queryset(self):
    return User.objects.filter()
    
  def post(self, request):
    print(request.data['username'])
    print()
    return Response([])

class UserView(GenericAPIView):
  serializer_class = RegisterSerializer

  def get(self, request):
    user = self.get_serializer(request.user)
    return Response(user.data)