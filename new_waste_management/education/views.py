# education/views.py
from django.shortcuts import render
from .models import Resource  # Changed from EducationalResource to Resource

def resources(request):
    resources = Resource.objects.all()  # Changed model name here
    
    # Pre-process tutorial links by splitting them
    for resource in resources:
        if resource.tutorial_link:
            resource.tutorial_links = [link.strip() for link in resource.tutorial_link.split(',') if link.strip()]
        else:
            resource.tutorial_links = []
    
    context = {
        'resources': resources
    }
    return render(request, 'education/resources.html', context)