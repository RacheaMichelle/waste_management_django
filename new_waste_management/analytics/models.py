from django.db import models
from django.contrib.auth.models import User
from education.models import Resource  # Import the Resource model from education

class ResourceView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)  # Correct reference
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'resource')

    def __str__(self):
        return f"{self.user.username} viewed {self.resource.title}"