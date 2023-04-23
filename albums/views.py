import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from albums.models import Album, Photo
from .services import create_album


class AlbumsList(ListView):
    model = Album
    paginate_by = 20
    template_name = 'albums/albums_list.html'
    context_object_name = 'albums'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AlbumDetail(DetailView):
    model = Album
    template_name = 'albums/album_detail.html'
    context_object_name = 'album'


class CreateAlbumView(View):
    def post(self, request):
        try:
            album = create_album(request.POST.get('title'))
        except ValueError:
            return HttpResponse('<h1>Ошибка 500</h1>', status=500)
        return HttpResponseRedirect(reverse('album_detail', args=[album.id, album.slug]))


class AlbumPhotoUpdateView(View, LoginRequiredMixin):
    # POST to add an image
    def get(self, request, pk, slug):
        return JsonResponse({'post': 'false'})

    def post(self, request, pk, slug):
        try:
            album = Album.objects.get(pk=pk, slug=slug)
            photo_file = request.FILES.get('file')
            if photo_file:
                photo_file.name = f'photo_{album.slug}.{photo_file.name.split(".")[-1]}'
                Photo.objects.create(album=album, photo=photo_file)
                return HttpResponse('')
        except ObjectDoesNotExist:
            return HttpResponse(status=404)
        return HttpResponse(
            '<h1>500 Internal Server Error (Внутренняя ошибка сервера)</h1>',
            status=500)


class AlbumUpdateCoverView(View, LoginRequiredMixin):
    # POST to add an image
    def get(self, request, pk, slug):
        return JsonResponse({'post': 'false'})

    def post(self, request, pk, slug):
        try:
            album = Album.objects.get(pk=pk, slug=slug)
            photo_file = request.FILES.get('file')
            if photo_file:
                album.delete_cover()
                photo_file.name = f'cover_{album.slug}.{photo_file.name.split(".")[-1]}'
                album.cover = photo_file
                album.save()
                return HttpResponse('')
        except ObjectDoesNotExist:
            return HttpResponse(status=404)
        return HttpResponse(
            '<h1>500 Internal Server Error (Внутренняя ошибка сервера)</h1>',
            status=500)
