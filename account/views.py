from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
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
    username = request.data['username']
    password = request.data['password']
    user = User.objects.filter(username=username).first()
    if user is None:
      raise AuthenticationFailed({"error" : "No user exist"})
    if not user.check_password(password):
      raise AuthenticationFailed({"error" : "Wrong password"})
    refresh = RefreshToken.for_user(user)
    serializer = RegisterSerializer(user)
    return Response({
      'user': serializer.data,
      'token': str(refresh.access_token),
    })


class UserView(GenericAPIView):
  serializer_class = RegisterSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = self.get_serializer(request.user)
    return Response(user.data)