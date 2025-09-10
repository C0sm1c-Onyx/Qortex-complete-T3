from django.urls import path, include
from rest_framework.routers import DefaultRouter

from artist_catalog.views import ArtistViewSet, MusicViewSet, AlbumViewSet, TracksInAlbumViewSet


router = DefaultRouter()

router.register(r'artists', ArtistViewSet, basename='artist')
router.register(r'music', MusicViewSet, basename='music')
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'tracks-in-albums', TracksInAlbumViewSet, basename='tracks-in-albums')


urlpatterns = [
    path('v1/', include(router.urls)),
]