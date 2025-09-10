from rest_framework import viewsets, mixins
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from artist_catalog.models import Artist, Music, Album, AlbumTrack
from artist_catalog.serializers import (
    ArtistSerializer,
    MusicSerializer,
    AlbumWriteSerializer,
    AlbumReadSerializer,
    AlbumTracksGroupedSerializer,
)
from artist_catalog.swagger_examples import (
    ARTIST_EXAMPLES,
    MUSIC_EXAMPLES,
    ALBUM_EXAMPLES,
    RESPONSE_EXAMPLES,
    ERROR_EXAMPLES,
)
from artist_catalog.swagger_tags import TAGS, QUERY_PARAMETERS


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    @swagger_auto_schema(
        operation_summary="Получить список всех исполнителей",
        operation_description="Возвращает список всех исполнителей в системе",
        tags=[TAGS['artists']['name']],
        manual_parameters=[
            QUERY_PARAMETERS['search'],
            QUERY_PARAMETERS['ordering'],
            QUERY_PARAMETERS['limit'],
            QUERY_PARAMETERS['offset']
        ],
        responses={
            200: openapi.Response(
                description="Список исполнителей",
                schema=ArtistSerializer(many=True),
                examples=RESPONSE_EXAMPLES["artist_list"]
            )
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Создать нового исполнителя",
        operation_description="Создает нового исполнителя в системе",
        tags=[TAGS['artists']['name']],
        request_body=ArtistSerializer,
        responses={
            201: openapi.Response(
                description="Исполнитель успешно создан",
                schema=ArtistSerializer,
                examples=ARTIST_EXAMPLES["create"]
            ),
            400: openapi.Response(
                description="Некорректные данные",
                examples=ERROR_EXAMPLES["validation_error"]
            )
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Получить информацию об исполнителе",
        operation_description="Возвращает детальную информацию о конкретном исполнителе",
        tags=[TAGS['artists']['name']],
        responses={
            200: openapi.Response(
                description="Информация об исполнителе",
                schema=ArtistSerializer
            ),
            404: openapi.Response(
                description="Исполнитель не найден",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Обновить информацию об исполнителе",
        operation_description="Обновляет информацию о существующем исполнителе",
        tags=[TAGS['artists']['name']],
        request_body=ArtistSerializer,
        responses={
            200: openapi.Response(
                description="Исполнитель успешно обновлен",
                schema=ArtistSerializer,
                examples=ARTIST_EXAMPLES["update"]
            ),
            400: openapi.Response(
                description="Некорректные данные",
                examples=ERROR_EXAMPLES["validation_error"]
            ),
            404: openapi.Response(
                description="Исполнитель не найден",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Частично обновить информацию об исполнителе",
        operation_description="Частично обновляет информацию о существующем исполнителе",
        tags=[TAGS['artists']['name']],
        request_body=ArtistSerializer,
        responses={
            200: openapi.Response(
                description="Исполнитель успешно обновлен",
                schema=ArtistSerializer,
                examples=ARTIST_EXAMPLES["update"]
            ),
            400: openapi.Response(
                description="Некорректные данные",
                examples=ERROR_EXAMPLES["validation_error"]
            ),
            404: openapi.Response(
                description="Исполнитель не найден",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Удалить исполнителя",
        operation_description="Удаляет исполнителя из системы",
        tags=[TAGS['artists']['name']],
        responses={
            204: openapi.Response(description="Исполнитель успешно удален"),
            404: openapi.Response(
                description="Исполнитель не найден",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    @swagger_auto_schema(
        operation_summary="Получить список всех песен",
        operation_description="Возвращает список всех музыкальных произведений в системе",
        tags=[TAGS['music']['name']],
        manual_parameters=[
            QUERY_PARAMETERS['search'],
            QUERY_PARAMETERS['ordering'],
            QUERY_PARAMETERS['limit'],
            QUERY_PARAMETERS['offset']
        ],
        responses={
            200: openapi.Response(
                description="Список песен",
                schema=MusicSerializer(many=True)
            )
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Создать новую песню",
        operation_description="Создает новое музыкальное произведение в системе",
        tags=[TAGS['music']['name']],
        request_body=MusicSerializer,
        responses={
            201: openapi.Response(
                description="Песня успешно создана",
                schema=MusicSerializer,
                examples=MUSIC_EXAMPLES["create"]
            ),
            400: openapi.Response(
                description="Некорректные данные",
                examples=ERROR_EXAMPLES["validation_error"]
            )
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Получить информацию о песне",
        operation_description="Возвращает детальную информацию о конкретной песне",
        tags=[TAGS['music']['name']],
        responses={
            200: openapi.Response(
                description="Информация о песне",
                schema=MusicSerializer
            ),
            404: openapi.Response(
                description="Песня не найдена",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Обновить информацию о песне",
        operation_description="Обновляет информацию о существующей песне",
        tags=[TAGS['music']['name']],
        request_body=MusicSerializer,
        responses={
            200: openapi.Response(
                description="Песня успешно обновлена",
                schema=MusicSerializer,
                examples=MUSIC_EXAMPLES["update"]
            ),
            400: openapi.Response(
                description="Некорректные данные",
                examples=ERROR_EXAMPLES["validation_error"]
            ),
            404: openapi.Response(
                description="Песня не найдена",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Частично обновить информацию о песне",
        operation_description="Частично обновляет информацию о существующей песне",
        tags=[TAGS['music']['name']],
        request_body=MusicSerializer,
        responses={
            200: openapi.Response(
                description="Песня успешно обновлена",
                schema=MusicSerializer,
                examples=MUSIC_EXAMPLES["update"]
            ),
            400: openapi.Response(
                description="Некорректные данные",
                examples=ERROR_EXAMPLES["validation_error"]
            ),
            404: openapi.Response(
                description="Песня не найдена",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Удалить песню",
        operation_description="Удаляет песню из системы",
        tags=[TAGS['music']['name']],
        responses={
            204: openapi.Response(description="Песня успешно удалена"),
            404: openapi.Response(
                description="Песня не найдена",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.select_related("artist").all()

    def get_serializer_class(self):
        if self.action in {"list", "retrieve"}:
            return AlbumReadSerializer
        return AlbumWriteSerializer

    @swagger_auto_schema(
        operation_summary="Получить список всех альбомов",
        operation_description="Возвращает список всех альбомов с информацией об исполнителях",
        tags=[TAGS['albums']['name']],
        manual_parameters=[
            QUERY_PARAMETERS['search'],
            QUERY_PARAMETERS['ordering'],
            QUERY_PARAMETERS['limit'],
            QUERY_PARAMETERS['offset']
        ],
        responses={
            200: openapi.Response(
                description="Список альбомов",
                schema=AlbumReadSerializer(many=True),
                examples=RESPONSE_EXAMPLES["album_list"]
            )
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Создать новый альбом",
        operation_description="Создает новый альбом с возможностью добавления треков",
        tags=[TAGS['albums']['name']],
        request_body=AlbumWriteSerializer,
        responses={
            201: openapi.Response(
                description="Альбом успешно создан",
                schema=AlbumWriteSerializer,
                examples=ALBUM_EXAMPLES["create_with_tracks"]
            ),
            400: openapi.Response(
                description="Некорректные данные",
                examples=ERROR_EXAMPLES["validation_error"]
            )
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Получить информацию об альбоме",
        operation_description="Возвращает детальную информацию о конкретном альбоме",
        tags=[TAGS['albums']['name']],
        responses={
            200: openapi.Response(
                description="Информация об альбоме",
                schema=AlbumReadSerializer
            ),
            404: openapi.Response(
                description="Альбом не найден",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Обновить информацию об альбоме",
        operation_description="Обновляет информацию о существующем альбоме и его треках",
        tags=[TAGS['albums']['name']],
        request_body=AlbumWriteSerializer,
        responses={
            200: openapi.Response(
                description="Альбом успешно обновлен",
                schema=AlbumWriteSerializer,
                examples=ALBUM_EXAMPLES["update"]
            ),
            400: openapi.Response(
                description="Некорректные данные",
                examples=ERROR_EXAMPLES["validation_error"]
            ),
            404: openapi.Response(
                description="Альбом не найден",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Частично обновить информацию об альбоме",
        operation_description="Частично обновляет информацию о существующем альбоме",
        tags=[TAGS['albums']['name']],
        request_body=AlbumWriteSerializer,
        responses={
            200: openapi.Response(
                description="Альбом успешно обновлен",
                schema=AlbumWriteSerializer,
                examples=ALBUM_EXAMPLES["update"]
            ),
            400: openapi.Response(
                description="Некорректные данные",
                examples=ERROR_EXAMPLES["validation_error"]
            ),
            404: openapi.Response(
                description="Альбом не найден",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Удалить альбом",
        operation_description="Удаляет альбом и все связанные с ним треки из системы",
        tags=[TAGS['albums']['name']],
        responses={
            204: openapi.Response(description="Альбом успешно удален"),
            404: openapi.Response(
                description="Альбом не найден",
                examples=ERROR_EXAMPLES["not_found"]
            )
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TracksInAlbumViewSet(mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = AlbumTrack.objects.select_related("album", "album__artist", "track").all()

    @swagger_auto_schema(
        operation_summary="Получить все треки, сгруппированные по альбомам",
        operation_description="Возвращает все треки в системе, сгруппированные по альбомам с информацией об исполнителях",
        tags=[TAGS['tracks']['name']],
        manual_parameters=[
            QUERY_PARAMETERS['search'],
            QUERY_PARAMETERS['ordering'],
            QUERY_PARAMETERS['limit'],
            QUERY_PARAMETERS['offset']
        ],
        responses={
            200: openapi.Response(
                description="Треки, сгруппированные по альбомам",
                schema=AlbumTracksGroupedSerializer(many=True),
                examples=RESPONSE_EXAMPLES["tracks_grouped"]
            )
        }
    )
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

