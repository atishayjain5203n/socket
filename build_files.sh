pip install -r requirements.txt
python manage.py collectstatic
daphne socket_chat.asgi:application