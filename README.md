# Симуляция пульта сторожа

Симулирует пульт, показывающий информацию о работниках, посещающих склад

### Как установить
Python3 должен быть уже установлен.

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Создайте файл .env в папке "project" и заполните его слудующим содержанием:
```
export DEBUG=<Значение переменной DEBUG - True или False>
export DB_URL=<Ссылка на бд (библиотека dj-database-url)>
export SECRET_KEY=<Ваш SECRET KEY>
export ALLOWED_HOSTS=<Список разрешенных хостов>
```

Запустите скрипт командой
```
python manage.py runserver 0.0.0.0:8000
```

Перейдите по ссылке "http://127.0.0.1:8000/"

### Цель проекта

проект создан в качестве тренировки работы с django
