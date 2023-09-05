from django import forms
from django.forms import ModelForm

from main.models import List

class TaskEditForm(ModelForm):
    class Meta:
        model = List
        fields = ('title', 'author', 'description', 'date')