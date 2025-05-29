from django import template
from matching.models import Notification  # Adjust import based on your app structure

register = template.Library()

@register.filter
def unread_notifications_count(user):
    if user.is_authenticated:
        return Notification.objects.filter(recipient=user, is_read=False).count()
    return 0