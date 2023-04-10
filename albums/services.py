from .models import Album


def create_album(title: str):
    if not title:
        raise ValueError
    album = Album.objects.create(title=title)
    return album
