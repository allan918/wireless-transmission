import socket
import cv2
import time
from _datetime import  datetime

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.s.connect(('127.0.0.1', 5002))
        self.cap = cv2.VideoCapture(0)
        print('Connect succeed!')

    # def calculateFPS(self):
    #     start = time.time()
    #     for i in range(0, 30) :
    #         ret, frame = self.cap.read()
    #     end = time.time()
    #     print("FPS is {}".format(30/(end - start)))
    def sendFrame(self):
        ret, frame = self.cap.read()
        print(cv2.imencode('.jpg', frame)[1])
        self.s.sendto(cv2.imencode('.jpg', frame)[1], ('127.0.0.1', 5002))
    def close(self):
        self.socket.close()