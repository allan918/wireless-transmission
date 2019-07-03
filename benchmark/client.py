import socket as s
import cv2
import zlib

class Client:
    def __init__(self):
        # Init variables
        self.hostAddr = '127.0.0.1'  # (server IP address, can be a local IP address, can also be global IP address)
        self.PORT = 5050
        self.ip = '127.0.0.1'
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
        #self.s.bind((self.ip, self.PORT))
        try:
            time = 1
            while True:
            # grab frame
                image = self.getImage()
                data = self.prepare_zlib_jpg(image)
                self.send(data)
                print('No. {} frame is sent'.format(time))
                time = time + 1
                self.s.sendto(b'sent', (self.hostAddr, self.PORT))
        except KeyboardInterrupt:
            self.s.close()
            print("Stop streaming")

    def send(self, data):
        while len(data) > 0:
            temp = data[:self.MAX_PAYLOAD]
            self.s.sendto(temp, (self.hostAddr, self.PORT))
            data = data[self.MAX_PAYLOAD:]


if __name__ == "__main__":
    client = Client()
    client.start_stream()