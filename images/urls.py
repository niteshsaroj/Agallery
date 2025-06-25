from django.urls import path
from .views import gallery_list, gallery_detail

urlpatterns = [
    path('', gallery_list, name='gallery_list'),
    path('<int:pk>/', gallery_detail, name='gallery_detail'),
]
