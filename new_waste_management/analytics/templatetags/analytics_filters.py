# analytics/templatetags/analytics_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)