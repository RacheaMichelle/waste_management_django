from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_waste, name='waste_list'),
]