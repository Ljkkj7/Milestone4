from django.db import models

# Create your models here.
class CreatorAccountModel(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CreatorAccount for {self.user.username}"
    
class WishlistItem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='wishlist_items')
    sneaker = models.ForeignKey('marketplace.Sneaker', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'sneaker')

    def __str__(self):
        return f"{self.sneaker} in {self.user.username}'s Wishlist"