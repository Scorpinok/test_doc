# test_doc

Тестовый запуск flask на докер

Для запуска нужно установить docker, git

Клонируем репозиторий и создаем образ
git clone https://github.com/Scorpinok/test_doc.git
cd .\test_doc\
docker build -t my_flask_app:latest my_flask_app/

Запускаем контейнер
docker run -d -p 5000:5000 my_flask_app:latest

В браузере переходим на localhost:5000
