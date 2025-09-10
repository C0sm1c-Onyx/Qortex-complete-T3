## Установка и запуск проекта

1. Склонируйте репозиторий
```bash
git clone https://github.com/C0sm1c-Onyx/Qortex-complete-T3.git
```
2. Скопируйте файл .env.example и переименуйте на .env
3. Подставьте свои значения в .env (можно не делать)
4. Запустите проект
```bash
docker compose up -d --build
```

### ! Настроена админ панель (для удобного создания сущностей):
### url http://127.0.0.1:8000/admin

### логин: root
### пароль: root

---
## Swagger
url - http://127.0.0.1:8000/swagger
---

## API документация

Ниже описаны доступные REST‑эндпоинты приложения `artist_catalog`. Все URL начинаются с префикса `/api/v1/`.

- Базовый URL: `/api/v1/`
- Формат данных: JSON
- Кодировки: UTF‑8
- Аутентификация: не требуется

### Сущности
- **Artist (Исполнитель)**: `id`, `artist_name`
- **Music (Песня/Трек)**: `id`, `title`
- **Album (Альбом)**: `id`, `artist` (id исполнителя), `release_date` (YYYY-MM-DD)
- **AlbumTrack (Трек в альбоме)**: связь альбома с треком и его номером в альбоме

---

### Artists — CRUD
- Список: `GET /api/v1/artists/`
- Создание: `POST /api/v1/artists/`
- Получение: `GET /api/v1/artists/{id}/`
- Частичное обновление: `PATCH /api/v1/artists/{id}/`
- Полное обновление: `PUT /api/v1/artists/{id}/`
- Удаление: `DELETE /api/v1/artists/{id}/`

---

### Music — CRUD
- Список: `GET /api/v1/music/`
- Создание: `POST /api/v1/music/`
- Получение: `GET /api/v1/music/{id}/`
- Частичное обновление: `PATCH /api/v1/music/{id}/`
- Полное обновление: `PUT /api/v1/music/{id}/`
- Удаление: `DELETE /api/v1/music/{id}/`

---

### Albums — CRUD (с поддержкой добавления нескольких треков)
- Список: `GET /api/v1/albums/`
- Создание: `POST /api/v1/albums/`
- Получение: `GET /api/v1/albums/{id}/`
- Частичное обновление: `PATCH /api/v1/albums/{id}/`
- Полное обновление: `PUT /api/v1/albums/{id}/`
- Удаление: `DELETE /api/v1/albums/{id}/`

Пример:

Создать альбом с несколькими треками
```bash
curl -X POST http://localhost:8000/api/v1/albums/ \
  -H "Content-Type: application/json" \
  -d '{
    "artist": 1,
    "release_date": "1997-05-21",
    "tracks": [
      {"title": "Track 1", "number": 1},
      {"title": "Track 2", "number": 2},
      {"title": "Track 3", "number": 3}
    ]
  }'
```

Ответ (201):
```json
{"id": 1, "artist": 1, "release_date": "1997-05-21", "tracks": [
  {"title": "Track 1", "number": 1},
  {"title": "Track 2", "number": 2},
  {"title": "Track 3", "number": 3}
]}
```

---

### Tracks in Albums — только чтение (список)
- Список сгруппированных треков по альбомам: `GET /api/v1/tracks-in-albums/`

---

