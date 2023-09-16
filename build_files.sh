pip install -r requirements.txt
python3.9 manage.py collectstatic
web: daphne socket_chat.asgi: application --port $PORT --bind 0.0.0.0 