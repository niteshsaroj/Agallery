from django.shortcuts import render, get_object_or_404
from .models import Gallery

def gallery_list(request):
    galleries = Gallery.objects.all().order_by('-created_at')
    return render(request, 'gallery_list.html', {'galleries': galleries})

def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    media = gallery.media.all().order_by('-created_at')
    return render(request, 'gallery_detail.html', {'gallery': gallery, 'media': media})
