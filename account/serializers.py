from rest_framework.serializers import ModelSerializer

from .models import User

class RegisterSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password', 'id')
    extra_kwargs = {
      "id" : {
        "read_only": True
      }
    }

class LoginSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'password')