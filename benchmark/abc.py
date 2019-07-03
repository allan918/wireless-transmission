import socket as s
import cv2
import zlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import time
from _datetime import  datetime
# The client part which sends cameras
# https://github.com/ramonidea/wireless-data-transmission/blob/master/RealSense/server.py
class Client:
    def __init__(self):
        # Init variables
        self.hostAddr = '0.0.0.0'  # (server IP address, can be a local IP address, can also be global IP address)
        self.PORT = 5050
        self.ip = '0.0.0.0'
        self.MAX_PAYLOAD = 200
        self.image_finish = b"\ffffff"
        self.camera = cv2.VideoCapture(0)
        self.image = b""

    def prepare_jpg(self, image):
        # This can be using other compression as well
        return cv2.imencode('.jpg', image)[1]

    def prepare_zlib_jpg(self, image):
        return zlib.compress(cv2.imencode('.jpg', image)[1])

    def prepare_raw(self, image):
        return image

    def getImage(self):
        ret, frame = self.camera.read()
        return frame

    def start_stream(self):
        # Set up link
        self.s = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.s.bind((self.ip, self.PORT))
        try:
            time = 1
            while True:
            # grab frame
                image = self.getImage()
                data = self.prepare_jpg(image)
                self.send(data)
                print('No. {} frame is sent'.format(time))
                time = time + 1
        except KeyboardInterrupt:
            self.s.close()
            print("Stop streaming")

    def send(self, data):
    # here data should be a binary
        #data = self.image + data + self.image_finish
        while len(data) > 0:
            temp = data[:self.MAX_PAYLOAD]
            self.s.sendto(temp, (self.hostAddr, self.PORT))
            data = data[self.MAX_PAYLOAD:]


if __name__ == "__main__":
    client = Client()
    client.start_stream()


# The server side which receiev camera frames
# YOu can check this
class Server:
    def __init__(self):
        self.s = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.port = 5002
        self.ip = "127.0.0.1"
        self.s.bind((self.ip, self.port))
        self.BUFSIZE = 65500

def start_receive(self):
    conn, (host, remoteport) = self.s.accept()
    fps = 0
    arr1 = b""
    try:
        while True:
            start_time = time.time()
            while True:
                data = conn.recv(BUFSIZE)
                arr1 += data
                if b"\ffffff" in arr1:
                    image = arr1[:arr1.index(b"\ffffff")]
                    arr1 = arr1[arr1.index(b"\ffffff") + 7:]
        # determine fps
                    fps += 1
                    if fps > 30:
                        print("Averate FPS in %s frames is %s".format(fps, (time.time() - start_time) / fps))
                        fps = 0
    except KeyboardInterrupt:
        print("Stop streaming")

