import zmq

def main():
    try:
        context = zmq.Context(1)

        frontend = context.socket(zmq.SUB)
        frontend.bind('tcp://*:5559')
        frontend.setsockopt_string(zmq.SUBSCRIBE, '')

        backend = context.socket(zmq.PUB)
        backend.bind('tcp://*:5560')

        print('starting zmq forwarder')
        zmq.device(zmq.FORWARDER, frontend, backend)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        frontend.close()
        backend.close()
        context.term()

if __name__ == '__main__':
    main()
