from rest_framework import viewsets, mixins
from rest_framework.response import Response

from artist_catalog.models import Artist, Music, Album, AlbumTrack
from artist_catalog.serializers import (
    ArtistSerializer,
    MusicSerializer,
    AlbumWriteSerializer,
    AlbumReadSerializer,
    AlbumTracksGroupedSerializer,
)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.select_related("artist").all()

    def get_serializer_class(self):
        if self.action in {"list", "retrieve"}:
            return AlbumReadSerializer

        return AlbumWriteSerializer


class TracksInAlbumViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset = AlbumTrack.objects.select_related("album", "album__artist", "track").all()

    def list(self, request, *args, **kwargs):
        tracks = self.get_queryset().order_by("album_id", "track_number")
        grouped = []
        current_album_id = None
        current_group = None
        
        for at in tracks:
            if at.album_id != current_album_id:
                if current_group is not None:
                    grouped.append(current_group)

                current_group = {
                    "album": at.album,
                    "tracks": [],
                }

                current_album_id = at.album_id

            current_group["tracks"].append({
                "title": at.track.title,
                "number": at.track_number,
            })

        if current_group is not None:
            grouped.append(current_group)

        serializer = AlbumTracksGroupedSerializer(grouped, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = [{
            "album": instance.album,
            "tracks": [{
                "title": instance.track.title,
                "number": instance.track_number,
            }],
        }]

        serializer = AlbumTracksGroupedSerializer(data, many=True)
        return Response(serializer.data)
