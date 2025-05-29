from django.db import models
from django.contrib.auth.models import User

class WasteListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waste_type = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50, blank=True, help_text="e.g., 2 heaps, 5 sacks, 3 bags")
    description = models.CharField(max_length=100, blank=True, help_text="Additional details about the waste (optional)")
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='waste_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.waste_type} - {self.user.username}"