# NLP IR Project

## Описание
Проект реализует систему извлечения информации (IR) из docx-документов для улучшения качества работы QA чат-ботов. Включает обработку таблиц и списков, векторизацию данных и интеграцию IR-модели с генеративной языковой моделью.

## Структура
- **data/**: Примеры данных
- **scripts/**: Основные скрипты проекта
- **models/**: Предобученные модели
- **README.md**: Описание проекта

## Установка
1. Клонировать репозиторий:
    ```bash
    git clone https://github.com/pinky228/NLP_IR_Project.git
    cd NLP_IR_Project
    ```
2. Установить зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск
1. Создать 2 документа hard и:
    ```bash
    python scripts/create_docx.py
    ```
2. Спарсить данные:
    ```bash
    python scripts/parse_docx.py
    ```
3. Векторизовать данные:
    ```bash
    python scripts/vectorize_data.py
    ```
4. Построить IR-систему:
    ```bash
    python scripts/ir_system.py
    ```

## Оценка
Для оценки результатов используйте скрипт `evaluate.py`:
```bash
python scripts/evaluate.py
```

## Альтернативный запуск
Альтернативный запуск делает все те 4 действия + оценка из пунктов выше простой командой:
```bash
python main.py
```

