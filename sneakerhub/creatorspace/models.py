from django.db import models

# Create your models here.
class Brand(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    brand_bio = models.TextField()
    brand_banner = models.ImageField(upload_to='brand_banners/', null=True, blank=True)

    def __str__(self):
        return self.brand_name
    
class BrandCollaborators(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='collaborators')
    collaborator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product_edit_permission = models.BooleanField(default=False)
    product_upload_permission = models.BooleanField(default=False)
    product_delete_permission = models.BooleanField(default=False)
    profile_edit_permission = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.collaborator.username} - {self.brand.brand_name}"
    
class BrandProducts(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='brand_products/', null=True, blank=True)
    product_sizes = models.JSONField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    release_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name