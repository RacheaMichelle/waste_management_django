from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def home(request):
    context = {'message': 'Welcome to the NEMA Waste Management Platform'}
    rendered = render(request, 'home.html', context)
    logger.info("Rendered HTML: %s", rendered.content.decode('utf-8'))
    return rendered