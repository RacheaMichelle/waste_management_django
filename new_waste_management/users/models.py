from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Profile(models.Model):
    
    USER_TYPE_CHOICES = [
        ('household', 'Household'),
        ('business', 'Business'),
        ('collector', 'Collector'),
        ('recycler', 'Recycler'),
        ('quick_access', 'Quick Access'),
    ]

    WASTE_TYPE_CHOICES = [
        ('plastic', 'Plastic'),
        ('paper', 'Paper'),
        ('glass', 'Glass'),
        ('organic', 'Organic'),
        ('metal', 'Metal'),
        ('e-waste', 'E-Waste'),
        ('clothing', 'Clothing'),
        ('hazardous', 'Hazardous'),
        ('construction', 'Construction'),
        ('medical', 'Medical'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=20, 
        choices=USER_TYPE_CHOICES, 
        blank=True, 
        null=True
    )
    location = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
    )
    contact = models.CharField(
        max_length=15, 
        blank=True, 
        null=True,
        help_text="Phone number in format: +256XXXXXXXXX"
    )
    accepted_waste_types = models.CharField(
        max_length=200, 
        blank=True,
        help_text="Comma-separated list of accepted waste types"
    )

    def clean(self):
        if self.user_type in ['collector', 'recycler']:
            if not self.contact:
                raise ValidationError("Contact information is required for collectors/recyclers")
            if not self.accepted_waste_types:
                raise ValidationError("At least one waste type must be selected")

    def save(self, *args, **kwargs):
        self.full_clean()  # Runs clean() validation
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} ({self.get_user_type_display() if self.user_type else 'No Type'})"
