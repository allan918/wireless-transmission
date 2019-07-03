import socket as s
import time


class Server:
    def __init__(self):
        self.s = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.port = 5050
        self.ip = '127.0.0.1'
        self.s.bind((self.ip, self.port))
        self.BUFSIZE = 200


    def start_receive(self):
        # conn, (host, remoteport) = self.s.accept()
        # fps = 0
        # arr1 = b""
        try:
            while True:
                start_time = time.time()
                fps = 0
                while True:
                    data = self.s.recvfrom(self.BUFSIZE)
                   # arr1 += data
                   # print(data[0])
                    if data[0] == b'sent':
                        fps = fps + 1
                        if fps > 30:
                            print("Average FPS in {} frames is {}".format(fps, fps / (time.time() - start_time)))

        except KeyboardInterrupt:
            print("Stop streaming")


if __name__ == "__main__":
    server = Server()
    server.start_receive()





