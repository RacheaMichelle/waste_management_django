# report/forms.py
from django import forms
from .models import DumpingReport

class DumpingReportForm(forms.ModelForm):
    class Meta:
        model = DumpingReport
        fields = ['photo', 'waste_type', 'district', 'description', 'latitude', 'longitude']  # ✅ Add 'district'
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
