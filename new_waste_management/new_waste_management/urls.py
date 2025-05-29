from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('waste/', include('waste.urls')),
    path('matching/', include('matching.urls')),
    path('analytics/', include('analytics.urls')),
    path('education/', include('education.urls')),
    path('educ/', include('educ.urls')),
    path('report/', include('report.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)