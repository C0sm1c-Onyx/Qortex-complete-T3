from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from artist_catalog.views import ArtistViewSet, MusicViewSet, AlbumViewSet, TracksInAlbumViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="Artist Catalog API",
        default_version='v1',
        description="""
        # API каталога исполнителей
        
        Это API для управления музыкальным каталогом, включающим:
        
        ## Основные сущности:
        - **Исполнители** - музыкальные исполнители и группы
        - **Альбомы** - музыкальные альбомы с датой выпуска
        - **Песни** - отдельные музыкальные произведения
        - **Треки в альбомах** - связь между альбомами и песнями с номерами треков
        
        ## Возможности API:
        - Полный CRUD для всех сущностей
        - Создание альбомов с треками в одном запросе
        - Группировка треков по альбомам
        - Пагинация и фильтрация результатов
        - Подробная документация всех операций
        
        ## Примеры использования:
        
        ### Создание исполнителя:
        ```json
        {
            "artist_name": "The Beatles"
        }
        ```
        
        ### Создание альбома с треками:
        ```json
        {
            "artist": 1,
            "release_date": "1967-06-01",
            "tracks": [
                {"title": "Sgt. Pepper's Lonely Hearts Club Band", "number": 1},
                {"title": "With a Little Help from My Friends", "number": 2}
            ]
        }
        ```
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@artistcatalog.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()

router.register(r'artists', ArtistViewSet, basename='artist')
router.register(r'music', MusicViewSet, basename='music')
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'tracks-in-albums', TracksInAlbumViewSet, basename='tracks-in-albums')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    
    # Swagger UI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]