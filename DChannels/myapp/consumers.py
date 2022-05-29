from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

# ============== Synchronous =============== #

class MySyncConsumer(SyncConsumer):
  def websocket_connect(self, event):
    self.send({
      'type':'websocket.accept',  # to accept the connection
    })
    print("Websocket Connected...", event)
  
  def websocket_receive(self, event):
    print("Websocket Message Recieved...", event)
    print('Message : ', event['text'])
    self.send({
      'type':'websocket.send',   # to send message to client
      'text':'Hi Client',        # write your message to send client
    })
  
  def websocket_discount(self, event):
    print("Websocket Disconnected...", event)
    raise StopConsumer()


# ============== Asynchronous =============== #

class MyAsyncConsumer(AsyncConsumer):    
  async def websocket_connect(self, event):
    await self.send({
      'type':'websocket.accept'    # to accept the connection
    })
    print("Websocket Connected...", event)
  
  async def websocket_receive(self, event):
    print("Websocket Message Recieved...", event)
    print('Message : ', event['text'])
    await self.send({
      'type':'websocket.send',    # to send message to client
      'text':'Hello Client',      # write your message to send client
    })
  
  async def websocket_discount(self, event):
    print("Websocket Disconnected...", event)
    raise StopConsumer()
