from django.db import models

# Create your models here.
class CreatorUserModel(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username