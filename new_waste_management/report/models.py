from django.db import models
from django.contrib.auth.models import User

UGANDA_DISTRICTS = [
    ('Kampala', 'Kampala'),
    ('Wakiso', 'Wakiso'),
    ('Masindi', 'Masindi'),
    ('Kasese', 'Kasese'),
    ('Iganga', 'Iganga'),
    ('Bushenyi', 'Bushenyi'),
    ('Gulu', 'Gulu'),
    ('Lira', 'Lira'),
    ('Mbarara', 'Mbarara'),
    ('Jinja', 'Jinja'),
    ('Mbale', 'Mbale'),
    ('Arua', 'Arua'),
    ('Soroti', 'Soroti'),
    ('Fort Portal', 'Fort Portal'),
    ('Hoima', 'Hoima'),
    ('Masaka', 'Masaka'),
    ('Mukono', 'Mukono'),
    ('Nebbi', 'Nebbi'),
    ('Tororo', 'Tororo'),
    ('Kabale', 'Kabale'),
    ('Mityana', 'Mityana'),
    ('Adjumani', 'Adjumani'),
    ('Pallisa', 'Pallisa'),
    ('Kumi', 'Kumi'),
    ('Bundibugyo', 'Bundibugyo')
]

class DumpingReport(models.Model):
    WASTE_TYPES = [
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
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='reports/')
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPES)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    district = models.CharField(
        max_length=50,
        choices=UGANDA_DISTRICTS,
        default='Kampala'  # ✅ Default value for existing data
    )
    
    def __str__(self):
        return f"Report #{self.id} - {self.get_district_display()}"

    def save(self, *args, **kwargs):
        if not self.district:
            self.district = self.guess_district()
        super().save(*args, **kwargs)
    
    def guess_district(self):
        """Simple district guessing for student project"""
        return 'Kampala'  # Default guess for now
