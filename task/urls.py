from django.urls import path

from . import views
from .views import IndexView

app_name = 'task'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('create/<int:id>', views.create, name='create'),
    path('create', views.create, name='create'),
]