from channels.routing import ProtocolTypeRouter, URLRouter
# import app.routing
from django.urls import re_path
from app.consumers import TextRoomConsumer
from channels.auth import AuthMiddlewareStack
websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$', TextRoomConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'websocket':
        AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        )
    ,
})