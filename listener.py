import zmq
from zmq.eventloop.ioloop import ZMQIOLoop
from zmq.eventloop.zmqstream import ZMQStream

def callback(message):
    s = message[0].decode('utf-8')
    print(s)

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind('tcp://127.0.0.1:5560')
stream = ZMQStream(socket)
stream.on_recv(callback)

if __name__ == "__main__":
    ZMQIOLoop.instance().start()
