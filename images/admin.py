from django.contrib import admin
from .models import Gallery, Media

class MediaInline(admin.TabularInline):
    model = Media
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    inlines = [MediaInline]
    fields = ['title', 'description', 'cover_image']


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Media)
