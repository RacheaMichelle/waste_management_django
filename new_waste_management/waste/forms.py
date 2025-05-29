from django import forms
from .models import WasteListing

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

class WasteListingForm(forms.ModelForm):
    class Meta:
        model = WasteListing
        fields = ['waste_type', 'quantity', 'description', 'location', 'image']
        widgets = {
            'waste_type': forms.Select(choices=WASTE_TYPE_CHOICES),
            'quantity': forms.TextInput(attrs={'placeholder': 'e.g., 2 heaps, 5 sacks'}),
            'description': forms.TextInput(attrs={'placeholder': 'Additional details (e.g., color, condition)'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g., Kampala'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity', '').strip()
        if quantity:
            parts = quantity.split()
            if len(parts) < 2 or not parts[0].replace('.', '').isdigit():
                raise forms.ValidationError("Please enter a quantity with a unit (e.g., '2 heaps', '5 sacks').")
        return quantity