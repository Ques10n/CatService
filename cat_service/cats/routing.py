from django.urls import re_path
from .consumers import YourConsumer  # Импортируйте ваш Consumer

websocket_urlpatterns = [
    re_path(r'ws/chat/$', YourConsumer.as_asgi()),  # Укажите путь для WebSocket
]