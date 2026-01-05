from django import forms
from marketplace.models import Sneaker


class ListingCreationForm(forms.ModelForm):
    class Meta:
        model = Sneaker
        fields = ['name', 'brand', 'size', 'price', 'description', 'image']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters long.")
        return description
