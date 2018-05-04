import zmq
from zmq.eventloop import ioloop
from zmq.eventloop.zmqstream import ZMQStream
import asyncio
from zmq.asyncio import Context
ioloop.install()

ctx = Context.instance()
s = ctx.socket(zmq.PAIR)
s.connect('tcp://127.0.0.1:5560')

async def recv():
    while True:
        msg = await s.recv_multipart()
        print('received', msg)

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(recv())]
loop.run_forever()
