from django import forms
from django.contrib.auth.models import User
from .models import Brand, BrandProducts 

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name', 'brand_bio', 'brand_banner', 'brand_logo']

    def clean_brand_name(self):
        brand_name = self.cleaned_data.get('brand_name')
        if Brand.objects.filter(brand_name=brand_name).exists():
            raise forms.ValidationError("A brand with this name already exists.")
        return brand_name
    
    def clean_brand_bio(self):
        brand_bio = self.cleaned_data.get('brand_bio')
        if len(brand_bio) < 20:
            raise forms.ValidationError("Description must be at least 20 characters long.")
        return brand_bio
    
    def clean_brand_banner(self):
        brand_banner = self.cleaned_data.get('brand_banner')
        if brand_banner.size > 2 * 1024 * 1024:  # 2MB limit
            raise forms.ValidationError("Banner file size must be under 2MB.")
        return brand_banner
    
    def clean_brand_logo(self):
        brand_logo = self.cleaned_data.get('brand_logo')
        if brand_logo.size > 2 * 1024 * 1024:  # 2MB limit
            raise forms.ValidationError("Logo file size must be under 2MB.")
        return brand_logo
    
    def save(self, commit=True):
        brand = super().save(commit=False)
        brand_name = self.cleaned_data.get('brand_name')
        brand.brand_name = brand_name.title()  # Ensure brand name is title cased
        if commit:
            brand.save()
        return brand
    
class BrandProductsForm(forms.ModelForm):
    class Meta:
        model = BrandProducts
        fields = ['product_name', 'product_description', 'product_image', 'product_sizes', 'product_price'
                  , 'quantity', 'release_date', 'is_active']


    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if len(product_name) < 5:
            raise forms.ValidationError("Product name must be at least 5 characters long.")
        return product_name

    def clean_product_description(self):
        product_description = self.cleaned_data.get('product_description')
        if len(product_description) < 20:
            raise forms.ValidationError("Product description must be at least 20 characters long.")
        return product_description