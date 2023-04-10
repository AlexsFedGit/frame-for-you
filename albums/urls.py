from django.urls import path

from albums.views import AlbumsList, AlbumDetail, CreateAlbumView, AlbumPhotoUpdateView

urlpatterns = [
    path('', AlbumsList.as_view(), name='albums_list'),
    path('create/', CreateAlbumView.as_view(), name='album_create'),
    path('<int:pk>_<slug:slug>/update', AlbumPhotoUpdateView.as_view(), name='album_photo_update'),
    path('<int:pk>_<slug:slug>/', AlbumDetail.as_view(), name='album_detail'),
]
