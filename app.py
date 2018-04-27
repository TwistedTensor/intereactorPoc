import zmq
from zmq.eventloop import ioloop
from zmq.eventloop.zmqstream import ZMQStream
ioloop.install()

from tornado.websocket import WebSocketHandler
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

class ZMQPair:
    def __init__(self,callback):
        self.callback = callback
    
    def connect(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.bind('tcp://127.0.0.1:5560')
        self.stream = ZMQStream(self.socket)
        self.stream.on_recv(self.callback)

class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html')

class WSHandler(WebSocketHandler):
    def open(self):
        self.pair = ZMQPair(self.on_data)
        self.pair.connect()
        print('connection initialized')

    def on_message(self,message):
        print(message)
        self.write_message(message[::-1])

    def on_close(self):
        print('connection closed')

    def on_data(self,data):
        print(data[0])
        self.write_message(data[0])

    def check_origin(self,origin):
        return True

application = Application([
    (r'/',MainHandler),
    (r'/ws',WSHandler),
])
if __name__ == "__main__":
    application.listen(8888)
    io_loop = IOLoop.current()
    io_loop.start()
