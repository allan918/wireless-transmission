import socket as s
import time
import server
import client
from _datetime import datetime

class Server:
    def __init__(self):
        self.socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
        port = 5002
        self.socket.bind(("127.0.0.1", port))

    def receive(self):
        print('ready to receive data...')
        # fpsTime = time.time()
        data = self.socket.recv(4096)
        print("Data: ", data)
        # fpsEnd = time.time();
        # print('latency is ', (fpsEnd - fpsTime)/1000, 'ms')
        # print('FPS is ', 1/(fpsEnd - fpsTime))





