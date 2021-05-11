from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from main.models import ListModel


class CustomUserCreationForm(UserCreationForm):
    """
    Форма регистрации нового пользователя.
    С обязательными полями: ['username', 'password', 'email']
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        error_messages = {
            'username': {
                'unique': "Имя другое введи..."
            },
            'password2': {
                'password_mismatch': "Пароль не одинаков!",
            }
        }


class LoginForm(forms.Form):

    login = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.TextInput(attrs={'id': 'input_field_email-id'}),
    )
    password = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.PasswordInput()
    )

    class Meta:
        error_messages = {
            'login': {
                'user_not_found': 'Нет такого пользователя!!!!'
            },
            'password': {
                'wrong_password': 'Пароль кривой'
            }
        }

    def clean_login(self):
        login = self.cleaned_data.get("login")

        if not User.objects.filter(username=login).exists():
            raise ValidationError(
                self.Meta.error_messages['login']['user_not_found'],
                code='user_not_found',
            )
        return login


