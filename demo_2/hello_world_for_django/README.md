
## celery
celery -A hello_world_for_django worker -l=debug

## django
python3 manage.py runserver

## test
http get http://127.0.0.1:8000/test/