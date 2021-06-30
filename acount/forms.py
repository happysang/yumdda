from django.contrib.auth.forms import UserCreationForm
from django.forms.models import fields_for_model
from .models import CustomUser

class RegisterForm (UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2','nickname']

        # labels = {
        #     'username': '아이디',
        #     'Password': '비밀번호',
        #     'nickname': '닉네임'
        # }