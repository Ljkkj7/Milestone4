from datetime import datetime
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
    
class DateInput(forms.DateInput):
    input_type = 'date'
    
class BrandProductsForm(forms.ModelForm):
    class Meta:
        model = BrandProducts
        fields = ['product_name', 'product_description', 'product_image', 'product_sizes', 'product_price'
                  , 'quantity', 'release_date', 'is_active']
        widgets = {
            'release_date': DateInput(),
            'product_price': forms.NumberInput(attrs={'step': '1.00'}),
        }


    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if len(product_name) > 40:
            raise forms.ValidationError("Product cannot exceed 40 characters.")
        return product_name

    def clean_product_description(self):
        product_description = self.cleaned_data.get('product_description')
        if len(product_description) < 20:
            raise forms.ValidationError("Product description must be at least 20 characters long.")
        return product_description
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative.")
        return quantity
    
    def clean_product_price(self):
        product_price = self.cleaned_data.get('product_price')
        if product_price <= 0:
            raise forms.ValidationError("Price must be a positive value.")
        return product_price
    
    def clean_product_sizes(self):
        product_sizes = self.cleaned_data.get('product_sizes')
        if not product_sizes:
            raise forms.ValidationError("Please enter at least one size.")
        sizes_list = [size.strip() for size in product_sizes.split(',')]
        if not all(size.isdigit() and 1 <= int(size) <= 14 for size in sizes_list):
            raise forms.ValidationError("Sizes must be numbers between 1 and 14 [UK sizes], separated by commas.")
        return product_sizes
    
    def clean_product_image(self):
        product_image = self.cleaned_data.get('product_image')
        if product_image and product_image.size > 2 * 1024 * 1024:  # 2MB limit
            raise forms.ValidationError("Product image file size must be under 2MB.")
        return product_image
    
    def save(self, commit=True):
        product = super().save(commit=False)
        product_name = self.cleaned_data.get('product_name')
        product.product_name = product_name.title()  # Ensure product name is title cased
        if commit:
            product.save()
        return product