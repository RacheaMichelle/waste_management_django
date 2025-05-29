from django.urls import path
from . import views

urlpatterns = [
    path('', views.matches, name='matches'),
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/mark/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
    path('notifications/delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('notifications/clear/', views.clear_all_notifications, name='clear_all_notifications'),
]