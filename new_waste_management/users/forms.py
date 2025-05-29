from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=Profile.USER_TYPE_CHOICES,
        widget=forms.RadioSelect
    )
    location = forms.CharField(max_length=100)
    contact = forms.CharField(
        max_length=15,
        required=False,
        help_text="Phone number in format: +256XXXXXXXXX"
    )
    accepted_waste_types = forms.MultipleChoiceField(
        choices=Profile.WASTE_TYPE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        
        if user_type in ['collector', 'recycler']:
            if not cleaned_data.get('contact'):
                self.add_error('contact', "Contact information is required for collectors/recyclers")
            if not cleaned_data.get('accepted_waste_types'):
                self.add_error('accepted_waste_types', "At least one waste type must be selected")
        
        return cleaned_data
    from django import forms

class QuickRegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=Profile.USER_TYPE_CHOICES,
        widget=forms.RadioSelect,
        required=False  # Now optional
    )
    location = forms.CharField(max_length=100, required=False)
    contact = forms.CharField(
        max_length=15,
        required=False,
        help_text="Phone number in format: +256XXXXXXXXX"
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_type', 'location', 'contact']

    def save(self, commit=True):
        user = super().save(commit)
        profile, created = Profile.objects.get_or_create(user=user)
        profile.user_type = self.cleaned_data.get('user_type') or None
        profile.location = self.cleaned_data.get('location') or None
        profile.contact = self.cleaned_data.get('contact') or None
        profile.save()
        return user