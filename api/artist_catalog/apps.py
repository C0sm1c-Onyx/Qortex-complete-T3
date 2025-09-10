from django.apps import AppConfig


class ArtistCatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artist_catalog'

    def ready(self):
        from . import signals   # noqa