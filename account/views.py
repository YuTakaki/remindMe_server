from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
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
    usernameOrEmail = request.data['usernameOrEmail']
    password = request.data['password']
    user = User.objects.filter(Q(username=usernameOrEmail) | Q(email=usernameOrEmail)).first()
    if user is None:
      raise AuthenticationFailed({"error" : {"usernameOrEmail" : "username/email does not exist"}})
    if not user.check_password(password):
      raise AuthenticationFailed({"error" : {"password" : "Wrong password"}})
    refresh = RefreshToken.for_user(user)
    serializer = RegisterSerializer(user)
    return Response({
      'user': serializer.data,
      'token': str(refresh.access_token),
    })


class UserCheckView(GenericAPIView):
  serializer_class = RegisterSerializer

  def get(self, request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    user = User.objects.filter(Q(username = username) | Q(email = email)).first()
    return Response(True) if user is None else Response(False)

class UserView(GenericAPIView):
  serializer_class = RegisterSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    print(request)
    serializer = self.serializer_class(request.user)
    return Response(serializer.data)