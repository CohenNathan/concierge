# Локален Setup - Cohen House Concierge

## Защо не работи localhost:8000?

Сървърът, който стартирах, работи в GitHub Actions среда (облачен сървър), **не на вашия локален компютър**. За да достъпите приложението на `localhost:8000`, трябва да го стартирате на вашата машина.

## Как да стартирам локално?

### Стъпка 1: Клонирайте проекта

```bash
git clone https://github.com/CohenNathan/concierge.git
cd concierge
```

### Стъпка 2: Checkout на реорганизираната branch

```bash
git checkout copilot/reorganize-project-structure
```

### Стъпка 3: Инсталирайте Python зависимости

```bash
# Препоръчва се виртуална среда
python3 -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate

# Инсталирайте зависимостите
pip install -r requirements.txt
```

### Стъпка 4: Конфигурирайте .env файла

```bash
# Копирайте примерния файл
cp .env.example .env

# Редактирайте .env с вашите API ключове
nano .env  # или използвайте вашия любим редактор
```

Необходими API ключове:
- `OPENAI_API_KEY` - За AI асистента
- `ELEVENLABS_API_KEY` - За text-to-speech
- Други опционални ключове в .env.example

### Стъпка 5: Стартирайте сървъра

**Опция A - С uvicorn (препоръчвана за development):**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Опция B - Със скрипта start_server.py:**

```bash
python3 start_server.py
```

### Стъпка 6: Отворете браузър

Отидете на: http://localhost:8000/

Трябва да видите Solomon - 3D avatar интерфейса на Cohen House.

## Проверка на структурата

След като сървърът стартира, проверете:

✅ **Web интерфейс:** http://localhost:8000/
✅ **3D Модел:** http://localhost:8000/avatar.glb
✅ **WebSocket:** ws://localhost:8000/ws
✅ **API документация:** http://localhost:8000/docs

## Реорганизирана структура

Проектът сега използва модулна структура:

```
app/
├── api/          # OpenAI интеграции
├── services/     # Бизнес логика (TTS, Spotify, Face Recognition)
├── handlers/     # HTTP endpoints (Booking, Actions, Search)
├── utils/        # Помощни функции (Browser, Cache, Window Manager)
└── config/       # Конфигурация

web/
├── assets/
│   ├── models/   # 3D модели (avatar.glb)
│   └── js/       # JavaScript файлове
└── index.html    # Главна страница
```

## Тестване

Всички тестове са обновени за новата структура:

```bash
# Тест с mock данни (не изисква API ключове)
python3 test_mocked_system.py

# Пълен тест (изисква API ключове)
python3 test_complete_system.py
```

## Логове и Debugging

Логовете от сървъра се записват в:
- **Console output** - Директно в терминала
- **server.log** - Ако използвате start_server.py

Проверете логовете за грешки:
```bash
tail -f server.log
```

## Често срещани проблеми

### ModuleNotFoundError
Инсталирайте отново зависимостите:
```bash
pip install -r requirements.txt
```

### Port 8000 is already in use
Спрете другия процес или използвайте друг порт:
```bash
uvicorn app.main:app --reload --port 8001
```

### API Keys not working
Проверете .env файла и уверете се, че ключовете са валидни.

## Документация

- **STRUCTURE.md** - Подробна структура на проекта
- **MIGRATION_SUMMARY.md** - Промени от реорганизацията
- **TEST_RESULTS.md** - Резултати от тестовете
- **SERVER_STATUS.md** - Информация за сървъра

## Поддръжка

Всички модули са тествани и работят правилно. Проектът е готов за production след като добавите реалните API ключове.

---

**Забележка:** Реорганизацията е завършена успешно. Всички импорти са обновени, файловете са преместени, а тестовете потвърждават, че функционалността е запазена.
