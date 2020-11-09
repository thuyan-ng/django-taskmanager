from django.shortcuts import render, reverse
from django.views.generic import ListView
from .models import Task
from django.http import HttpResponseRedirect
from task.forms import AddTaskForm, TaskForm
from developer.models import Developer
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Task
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    permission_required = 'task.task_management'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = TaskForm
        return context


def delete(request, id):
    Task.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('task:index'))


def create(request, id=None):
    if id is None:
        form = TaskForm(request.POST)
    else:
        form = AddTaskForm(request.POST)
    if form.is_valid():
        task = Task.objects.create(title=form.cleaned_data['title'],description=form.cleaned_data['description'])
        if id is None:
            task.assignee = form.cleaned_data['assignee']
        else:
            task.assignee=Developer.objects.get(pk=id)
        task.save()
    return HttpResponseRedirect(reverse('developer:index'))
