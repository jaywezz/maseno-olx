from .models import DaemonStar_User

from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):

		model = DaemonStar_User
		fields = ('username', 'email')


class LoginForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput)

	class Meta:
		model = DaemonStar_User
		fields = ['username', 'password']

class ProfileEditForm(forms.ModelForm):

	class Meta:
		model = DaemonStar_User
		fields = ('user_avatar', 'username', 'email', 'phone_number', 'location')




