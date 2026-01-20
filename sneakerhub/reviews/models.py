from django.db import models

# Create your models here.
class Review(models.Model):
    reviewed_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    reviewer_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviews_made')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.reviewer_id.username} for {self.reviewed_user.username}'
