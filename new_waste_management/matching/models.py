from django.db import models
from django.contrib.auth.models import User
from waste.models import WasteListing
from django.utils import timezone

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(WasteListing, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.message[:50]}"