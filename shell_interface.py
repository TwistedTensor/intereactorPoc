import zmq
from zmq.eventloop import ioloop
from zmq.eventloop.zmqstream import ZMQStream
ioloop.install()

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect('tcp://127.0.0.1:5560')
