from django import forms
from django.contrib.auth.models import User
from .models import Brand 

class CreatorSpaceForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'logo']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Brand.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("A brand with this name already exists.")
        return name
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 20:
            raise forms.ValidationError("Description must be at least 20 characters long.")
        return description
    
    def clean_logo(self):
        logo = self.cleaned_data.get('logo')
        if logo.size > 2 * 1024 * 1024:  # 2MB limit
            raise forms.ValidationError("Logo file size must be under 2MB.")
        return logo
    
    def save(self, commit=True):
        brand = super().save(commit=False)
        name = self.cleaned_data.get('name')
        brand.name = name.title()  # Ensure brand name is title cased
        if commit:
            brand.save()
        return brand