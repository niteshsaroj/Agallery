from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='gallery_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Media(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='gallery_media/')
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media in {self.gallery.title}"

    def is_video(self):
        ext = self.file.name.split('.')[-1].lower()
        return ext in ['mp4', 'mov', 'avi', 'webm', 'mkv']

    def is_image(self):
        ext = self.file.name.split('.')[-1].lower()
        return ext in ['jpg', 'jpeg', 'png', 'gif', 'webp']
