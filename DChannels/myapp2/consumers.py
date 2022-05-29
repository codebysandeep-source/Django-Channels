from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

class MySync(SyncConsumer):
  def websocket_connect(self, event):
    self.send({
      'type':'websocket.accept'
    })
    print("Connected..." , event)

  def websocket_receive(self, event):
    print("Received...", event)
    for i in range(11):
      self.send({
        'type':'websocket.send',
        'text': str(i)
      })
      sleep(1)

  def websocket_disconnect(self, event):
    print("Disconnected...", event)
    raise StopConsumer()




class MyAsync(AsyncConsumer):
  async def websocket_connect(self, event):
    await self.send({
      'type':'websocket.accept'
    })
    print("Connected..." , event)

  async def websocket_receive(self, event):
    print("Received...", event)
    for i in range(11):
      await self.send({
        'type':'websocket.send',
        'text': str(i)
      })
      await asyncio.sleep(1)

  async def websocket_disconnect(self, event):
    print("Disconnected...", event)
    raise StopConsumer()