from django.urls import path
from myapp.consumers import *
from myapp2.consumers import *

websocket_urlpatterns = [
  # myapp
  path('ws/sc', MySyncConsumer.as_asgi()),
  path('ws/ac', MyAsyncConsumer.as_asgi()),

  # myapp2
  path('ws/s', MySync.as_asgi()),
  path('ws/a', MyAsync.as_asgi()),
]



# http://127.0.0.1:8000/     - default   (http - hypertext transfer protocol)
# https://127.0.0.1:8000/     - default  (http - hypertext transfer protocol secured)

# ws://127.0.0.1:8000/     - Django channels    (ws - WebSocket)
# wss://127.0.0.1:8000/     - Django channels   (ws - WebSocket secured)