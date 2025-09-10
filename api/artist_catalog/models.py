from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(
        max_length=100,
        verbose_name="Имя исполнителя",
        help_text="Название исполнителя или музыкальной группы"
    )

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"
        ordering = ["artist_name"]

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    artist = models.ForeignKey(
        Artist, 
        on_delete=models.CASCADE,
        verbose_name="Исполнитель",
        help_text="Исполнитель, выпустивший альбом"
    )
    release_date = models.DateField(
        verbose_name="Дата выпуска",
        help_text="Дата выпуска альбома"
    )

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ["release_date", "artist__artist_name"]

    def __str__(self):
        return f"{self.artist} - {self.release_date}"


class Music(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название песни",
        help_text="Название музыкального произведения"
    )

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"
        ordering = ["title"]

    def __str__(self):
        return self.title


class AlbumTrack(models.Model):
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE, 
        related_name="album_tracks",
        verbose_name="Альбом",
        help_text="Альбом, в который входит трек"
    )
    track = models.ForeignKey(
        Music, 
        on_delete=models.CASCADE, 
        related_name="album_tracks",
        verbose_name="Трек",
        help_text="Музыкальное произведение"
    )
    track_number = models.PositiveIntegerField(
        verbose_name="Номер трека",
        help_text="Порядковый номер трека в альбоме"
    )

    class Meta:
        verbose_name = "Трек в альбоме"
        verbose_name_plural = "Треки в альбоме"
        ordering = ["album", "track_number"]
        constraints = [
            models.UniqueConstraint(
                fields=["album", "track_number"], 
                name="uniq_track_number_per_album"
            ),
            models.UniqueConstraint(
                fields=["album", "track"], 
                name="uniq_track_per_album"
            ),
        ]

    def __str__(self) -> str:
        return f"{self.album.artist.artist_name}: {self.track_number}. {self.track.title}"