from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.contrib import messages

from .models import Artist, Album, Music, AlbumTrack


class AlbumTrackInline(admin.TabularInline):
    model = AlbumTrack
    extra = 1
    fields = ('track', 'track_number')
    ordering = ('track_number',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'albums_count', 'tracks_count')
    list_filter = ('artist_name',)
    search_fields = ('artist_name',)
    ordering = ('artist_name',)
    actions = ['duplicate_artist']
    
    def albums_count(self, obj):
        count = obj.album_set.count()
        if count > 0:
            url = reverse('admin:artist_catalog_album_changelist') + f'?artist__id__exact={obj.id}'
            return format_html('<a href="{}">{} альбомов</a>', url, count)
        return '0 альбомов'
    
    def tracks_count(self, obj):
        count = AlbumTrack.objects.filter(album__artist=obj).count()
        if count > 0:
            return f'{count} треков'
        return '0 треков'

    albums_count.short_description = 'Количество альбомов'
    tracks_count.short_description = 'Общее количество треков'


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist', 'release_date', 'tracks_count', 'album_link')
    list_filter = ('release_date', 'artist')
    search_fields = ('artist__artist_name',)
    ordering = ('-release_date', 'artist__artist_name')
    inlines = [AlbumTrackInline]
    actions = ['duplicate_album']
    date_hierarchy = 'release_date'
    
    def tracks_count(self, obj):
        count = obj.album_tracks.count()
        if count > 0:
            url = reverse('admin:artist_catalog_albumtrack_changelist') + f'?album__id__exact={obj.id}'
            return format_html('<a href="{}">{} треков</a>', url, count)
        return '0 треков'
    
    def album_link(self, obj):
        url = reverse('admin:artist_catalog_album_change', args=[obj.id])
        return format_html('<a href="{}">Редактировать альбом</a>', url)

    tracks_count.short_description = 'Количество треков'
    album_link.short_description = 'Действия'


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'albums_count', 'music_link')
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
    actions = ['duplicate_music']
    
    def albums_count(self, obj):
        count = obj.album_tracks.count()
        if count > 0:
            url = reverse('admin:artist_catalog_albumtrack_changelist') + f'?track__id__exact={obj.id}'
            return format_html('<a href="{}">В {} альбомах</a>', url, count)

        return 'Не используется'
    
    def music_link(self, obj):
        url = reverse('admin:artist_catalog_music_change', args=[obj.id])
        return format_html('<a href="{}">Редактировать</a>', url)

    albums_count.short_description = 'Использование в альбомах'
    music_link.short_description = 'Действия'


@admin.register(AlbumTrack)
class AlbumTrackAdmin(admin.ModelAdmin):
    list_display = ('album', 'track', 'track_number', 'artist_name', 'release_date')
    list_filter = ('album__artist', 'album__release_date')
    search_fields = ('track__title', 'album__artist__artist_name')
    ordering = ('album', 'track_number')
    actions = ['reorder_tracks']
    
    def artist_name(self, obj):
        return obj.album.artist.artist_name

    def release_date(self, obj):
        return obj.album.release_date
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('album__artist', 'track')
    
    def reorder_tracks(self, request, queryset):
        albums_updated = 0

        for album_track in queryset:
            album = album_track.album
            tracks = album.album_tracks.all().order_by('track_number')
            for i, track in enumerate(tracks, 1):
                if track.track_number != i:
                    track.track_number = i
                    track.save()

            albums_updated += 1
        
        self.message_user(
            request,
            f'Перенумерованы треки в {albums_updated} альбомах.',
            messages.SUCCESS
        )

    artist_name.short_description = 'Исполнитель'
    artist_name.admin_order_field = 'album__artist__artist_name'
    release_date.short_description = 'Дата выпуска'
    release_date.admin_order_field = 'album__release_date'
    reorder_tracks.short_description = "Перенумеровать треки в альбомах"
