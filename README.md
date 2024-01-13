# Developer experience на Django

Из выступления Фёдора Борщёва [Воркшоп «Современный DX в Django»](https://www.youtube.com/watch?v=Zsr4aWKkdOc).

Запуск:

```bash
source env/bin/activate
make deps
docker compose up -d
cd src/
./manage.py migrate && ./manage.py runserver
```

URL:

[localhost:8000/api/v1/books](http://localhost:8000/api/v1/books)