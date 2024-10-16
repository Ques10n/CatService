import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from django.core.asgi import get_asgi_application
from django.urls import path


import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cat_service.settings')

django.setup()

# from cat_service.cats.consumers import YourConsumer

from channels.consumer import AsyncConsumer

from django.urls import re_path




class YourConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, text_data):
        await self.send({
            "type": "websocket.send",
            "text": "Hello from Django socket"
        })

    async def websocket_disconnect(self, event):
        pass


websocket_urlpatterns = [
    re_path(r'ws/chat/$', YourConsumer.as_asgi()),  # Укажите путь для WebSocket
]


django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})