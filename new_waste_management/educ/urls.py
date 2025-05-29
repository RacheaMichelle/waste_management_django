from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.waste_quiz, name='waste_quiz'),
  
]
