from django.db import models

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('recycling', 'Recycling'),
        ('composting', 'Composting'),
        ('disposal', 'Disposal'),
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
    title = models.CharField(max_length=500)
    waste_type = models.CharField(max_length=50, choices=WASTE_TYPE_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    recycling_process = models.TextField()
    products_made = models.TextField()
    making_process = models.TextField()
    tutorial_link = models.URLField(max_length=500, blank=True, null=True, help_text="YouTube link for complex processes")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title