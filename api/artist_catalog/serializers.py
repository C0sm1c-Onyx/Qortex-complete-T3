from rest_framework import serializers

from artist_catalog.models import Artist, Album, AlbumTrack, Music


class ArtistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        read_only=True,
        help_text="Уникальный идентификатор исполнителя"
    )
    artist_name = serializers.CharField(
        max_length=100,
        help_text="Название исполнителя или музыкальной группы"
    )

    class Meta:
        model = Artist
        fields = ("id", "artist_name",)


class MusicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        read_only=True,
        help_text="Уникальный идентификатор музыкального произведения"
    )
    title = serializers.CharField(
        max_length=100,
        help_text="Название музыкального произведения"
    )

    class Meta:
        model = Music
        fields = ("id", "title",)


class AlbumWriteTrackSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=100,
        help_text="Название трека"
    )
    number = serializers.IntegerField(
        min_value=1,
        help_text="Порядковый номер трека в альбоме (начиная с 1)"
    )


class AlbumWriteSerializer(serializers.ModelSerializer):
    tracks = AlbumWriteTrackSerializer(
        many=True, 
        required=False,
        help_text="Список треков альбома"
    )

    class Meta:
        model = Album
        fields = ("id", "artist", "release_date", "tracks")
        read_only_fields = ("id",)

    def create(self, validated_data):
        tracks_data = validated_data.pop("tracks", [])
        album = Album.objects.create(**validated_data)
        if tracks_data:
            self._upsert_tracks(album, tracks_data)

        return album

    def update(self, instance, validated_data):
        tracks_data = validated_data.pop("tracks", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if tracks_data is not None:
            instance.album_tracks.all().delete()
            self._upsert_tracks(instance, tracks_data)

        return instance

    def _upsert_tracks(self, album: Album, tracks_data):
        album_tracks_to_create = []
        for track_item in tracks_data:
            title = track_item["title"].strip()
            number = track_item["number"]
            music, _ = Music.objects.get_or_create(title=title)
            album_tracks_to_create.append(
                AlbumTrack(album=album, track=music, track_number=number)
            )

        if album_tracks_to_create:
            AlbumTrack.objects.bulk_create(album_tracks_to_create)


class AlbumReadSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(
        source="artist.artist_name", 
        read_only=True,
        help_text="Название исполнителя"
    )
    release_date = serializers.DateField(
        help_text="Дата выпуска альбома"
    )

    class Meta:
        model = Album
        fields = ("artist", "release_date")


class TrackInAlbumSerializer(serializers.Serializer):
    title = serializers.CharField(
        help_text="Название трека"
    )
    number = serializers.IntegerField(
        help_text="Порядковый номер трека в альбоме"
    )


class AlbumTracksGroupedSerializer(serializers.Serializer):
    album = AlbumReadSerializer(
        help_text="Информация об альбоме"
    )
    tracks = TrackInAlbumSerializer(
        many=True,
        help_text="Список треков в альбоме"
    )

