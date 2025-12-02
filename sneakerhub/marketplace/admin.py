from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Sneaker)

class SneakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'size', 'price', 'owner', 'created_at')
    search_fields = ('name', 'brand', 'owner__username')