from django.urls import path
from . import views



urlpatterns = [
    path('report/', views.report_dumping, name='report_dumping'),
    path('success/<int:report_id>/', views.report_success, name='report_success'),
]
