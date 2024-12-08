# cyprus_bot

## Запуск бота 

### Зависимости

pip uninstall -y aiogram aiohttp

pip install aiogram==2.25 aiohttp==3.8.5

### Обновить credentials

указать credential.yml для тг

### Команда для запуска бота 

ngrok http 5005 --> вставить forwarding url в credentials telegram url

rasa run --enable-api --cors "*" --debug
