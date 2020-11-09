from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Developer
from .forms import ShortDeveloperForm
from django.views.generic import DetailView, ListView
from task.forms import AddTaskForm

class IndexView(LoginRequiredMixin, ListView):
    model = Developer
    template_name = 'developer/index.html'
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = ShortDeveloperForm
        return context

# index(request):
    # return HttpResponse("Hello, world. You're at the developers index.") // old
    #context = {
        #'developers': Developer.objects.all(),
        #'form': DeveloperForm,
    #}
    #return render(request, 'developer/index.html', context)

class DevDetailView(LoginRequiredMixin, DetailView):
    model = Developer
    template_name = 'developer/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DevDetailView, self).get_context_data(**kwargs)
        context['form'] = AddTaskForm
        return context

#def detail(request, developer_id):
    # developer = Developer.objects.get(pk=developer_id)
    #developer = get_object_or_404(Developer, pk=developer_id)
    #return render(request, 'developer/detail.html', {'developer': developer})

def create(request):
    form = ShortDeveloperForm(request.POST)
    if form.is_valid():
        Developer.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            username=form.cleaned_data['username'],
            )
    return HttpResponseRedirect(reverse('developer:index'))

def delete(request, pk):
    Developer.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('developer:index'))

