from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from main.models import List, Users
from main.validators.password_validators import validate_password_strength


class TaskEditForm(ModelForm):
    class Meta:
        model = List
        fields = ('title', 'author', 'description', 'date', 'user_id')

class RegistrationForm(ModelForm):
    email    = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        validate_password_strength(password)
        return password

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Users
        fields = ('id', 'name', 'surname', 'email', 'password', 'phone')


class LoginForm(forms.Form):
    email    = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)