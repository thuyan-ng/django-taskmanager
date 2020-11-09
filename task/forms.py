from django import forms
from developer.models import Developer
from .models import Task

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    assignee = forms.ModelChoiceField(queryset=Developer.objects.all(), required=False)

class AddTaskForm(TaskForm):
    assignee = forms.ModelChoiceField(queryset=Developer.objects.all(), required=False, disabled=True)