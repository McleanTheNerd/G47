
import socket

class Listener(object):
    """docstring for Listener."""
    def __init__(self):
        super(Listener, self).__init__()
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    def start_listening(self):
        self.s.bind(("127.0.0.1",8001))
        self.s.listen(5)
        target ,ip = self.s.accept()

    def stop_listening(self):
        self.s.close()
