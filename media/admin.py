from django.contrib import admin

# Register your models here.from django.contrib import admin
from .models import MediaItem

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'uploaded_at')
    list_filter = ('media_type', 'uploaded_at')
    search_fields = ('title', 'description')
