"""
Теги для организации API в Swagger документации.
"""

from drf_yasg import openapi

# Теги для группировки операций
TAGS = {
    'artists': {
        'name': 'Исполнители',
        'description': 'Операции для управления исполнителями'
    },
    'music': {
        'name': 'Музыка',
        'description': 'Операции для управления музыкальными произведениями'
    },
    'albums': {
        'name': 'Альбомы',
        'description': 'Операции для управления альбомами'
    },
    'tracks': {
        'name': 'Треки в альбомах',
        'description': 'Операции для работы с треками в альбомах'
    }
}

# Параметры запросов
QUERY_PARAMETERS = {
    'search': openapi.Parameter(
        'search',
        openapi.IN_QUERY,
        description="Поиск по названию",
        type=openapi.TYPE_STRING,
        required=False
    ),
    'ordering': openapi.Parameter(
        'ordering',
        openapi.IN_QUERY,
        description="Сортировка результатов (например: 'artist_name', '-release_date')",
        type=openapi.TYPE_STRING,
        required=False
    ),
    'limit': openapi.Parameter(
        'limit',
        openapi.IN_QUERY,
        description="Количество результатов на странице",
        type=openapi.TYPE_INTEGER,
        required=False
    ),
    'offset': openapi.Parameter(
        'offset',
        openapi.IN_QUERY,
        description="Смещение для пагинации",
        type=openapi.TYPE_INTEGER,
        required=False
    )
}

# Заголовки ответов
RESPONSE_HEADERS = {
    'pagination': {
        'X-Total-Count': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Общее количество элементов'
        ),
        'X-Page-Size': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Размер страницы'
        ),
        'X-Page-Number': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Номер текущей страницы'
        )
    }
}
