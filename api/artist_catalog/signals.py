from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if not getattr(settings, 'CREATE_ROOT_SUPERUSER', True):
        return

    User = get_user_model()    # noqa

    username = 'root'
    password = 'root'
    email = 'root@gmail.com'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username, email=email, password=password
        )
