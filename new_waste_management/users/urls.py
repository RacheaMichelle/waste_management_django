
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('quick-dashboard/', views.quick_dashboard, name='quick_dashboard'),

    path('quick-register/', views.quick_register, name='quick_register'),
    
]
