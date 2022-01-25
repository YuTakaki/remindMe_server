from rest_framework.serializers import ModelSerializer

from .models import User

class RegisterSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password', 'id')
    extra_kwargs = {
      "id" : {
        "read_only": True
      },
      "password" : {
        "write_only": True
      }
    }

  def create(self, data):
    password = data.pop('password', None)
    instance = self.Meta.model(**data)
    if password is not None:
      instance.set_password(password)
      instance.save()
    return instance

class LoginSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'password')