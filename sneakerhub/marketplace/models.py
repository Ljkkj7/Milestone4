from django.db import models
from django.conf import settings


class Sneaker(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=4, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sneakers'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.name} (Size: {self.size})"
