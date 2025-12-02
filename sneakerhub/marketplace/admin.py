from django.contrib import admin
from .models import Sneaker


@admin.register(Sneaker)
class SneakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'size', 'price', 'owner', 'created_at')
    search_fields = ('name', 'brand', 'owner__username')
