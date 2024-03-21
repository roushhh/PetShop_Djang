from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterFrom(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","first_name","last_name"]
        labels={"username":"Enter username","email":"Email"}
        #fields="__all__"
