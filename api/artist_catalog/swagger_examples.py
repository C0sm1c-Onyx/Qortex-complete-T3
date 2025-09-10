"""
Примеры данных для Swagger документации.
"""

# Примеры для исполнителей
ARTIST_EXAMPLES = {
    "create": {
        "summary": "Создание исполнителя",
        "description": "Пример создания нового исполнителя",
        "value": {
            "artist_name": "The Beatles"
        }
    },
    "update": {
        "summary": "Обновление исполнителя",
        "description": "Пример обновления существующего исполнителя",
        "value": {
            "artist_name": "The Rolling Stones"
        }
    }
}

# Примеры для песен
MUSIC_EXAMPLES = {
    "create": {
        "summary": "Создание песни",
        "description": "Пример создания нового музыкального произведения",
        "value": {
            "title": "Bohemian Rhapsody"
        }
    },
    "update": {
        "summary": "Обновление песни",
        "description": "Пример обновления существующей песни",
        "value": {
            "title": "We Will Rock You"
        }
    }
}

# Примеры для альбомов
ALBUM_EXAMPLES = {
    "create_simple": {
        "summary": "Создание альбома без треков",
        "description": "Пример создания альбома без добавления треков",
        "value": {
            "artist": 1,
            "release_date": "1967-06-01"
        }
    },
    "create_with_tracks": {
        "summary": "Создание альбома с треками",
        "description": "Пример создания альбома с треками в одном запросе",
        "value": {
            "artist": 1,
            "release_date": "1967-06-01",
            "tracks": [
                {
                    "title": "Sgt. Pepper's Lonely Hearts Club Band",
                    "number": 1
                },
                {
                    "title": "With a Little Help from My Friends",
                    "number": 2
                },
                {
                    "title": "Lucy in the Sky with Diamonds",
                    "number": 3
                },
                {
                    "title": "Getting Better",
                    "number": 4
                },
                {
                    "title": "Fixing a Hole",
                    "number": 5
                }
            ]
        }
    },
    "update": {
        "summary": "Обновление альбома",
        "description": "Пример обновления альбома с изменением треков",
        "value": {
            "artist": 1,
            "release_date": "1967-06-02",
            "tracks": [
                {
                    "title": "Sgt. Pepper's Lonely Hearts Club Band (Reprise)",
                    "number": 1
                },
                {
                    "title": "A Day in the Life",
                    "number": 2
                }
            ]
        }
    }
}

# Примеры ответов
RESPONSE_EXAMPLES = {
    "artist_list": {
        "summary": "Список исполнителей",
        "description": "Пример ответа со списком исполнителей",
        "value": [
            {
                "id": 1,
                "artist_name": "The Beatles"
            },
            {
                "id": 2,
                "artist_name": "Queen"
            },
            {
                "id": 3,
                "artist_name": "Led Zeppelin"
            }
        ]
    },
    "album_list": {
        "summary": "Список альбомов",
        "description": "Пример ответа со списком альбомов",
        "value": [
            {
                "artist": "The Beatles",
                "release_date": "1967-06-01"
            },
            {
                "artist": "Queen",
                "release_date": "1975-10-31"
            }
        ]
    },
    "tracks_grouped": {
        "summary": "Треки, сгруппированные по альбомам",
        "description": "Пример ответа с треками, сгруппированными по альбомам",
        "value": [
            {
                "album": {
                    "artist": "The Beatles",
                    "release_date": "1967-06-01"
                },
                "tracks": [
                    {
                        "title": "Sgt. Pepper's Lonely Hearts Club Band",
                        "number": 1
                    },
                    {
                        "title": "With a Little Help from My Friends",
                        "number": 2
                    }
                ]
            },
            {
                "album": {
                    "artist": "Queen",
                    "release_date": "1975-10-31"
                },
                "tracks": [
                    {
                        "title": "Bohemian Rhapsody",
                        "number": 1
                    },
                    {
                        "title": "Love of My Life",
                        "number": 2
                    }
                ]
            }
        ]
    }
}

# Примеры ошибок
ERROR_EXAMPLES = {
    "validation_error": {
        "summary": "Ошибка валидации",
        "description": "Пример ошибки валидации данных",
        "value": {
            "artist_name": [
                "Это поле обязательно для заполнения."
            ],
            "release_date": [
                "Введите корректную дату."
            ]
        }
    },
    "not_found": {
        "summary": "Ресурс не найден",
        "description": "Пример ошибки, когда запрашиваемый ресурс не найден",
        "value": {
            "detail": "Не найдено."
        }
    }
}
