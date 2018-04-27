from tornado.websocket import WebSocketHandler
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html')

class WSHandler(WebSocketHandler):
    def open(self):
        print('connection initialized')

    def on_message(self,message):
        print(message)
        self.write_message(message[::-1])

    def on_close(self):
        print('connection closed')

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
