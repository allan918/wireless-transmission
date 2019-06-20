import socket
import cv2
from _datetime import  datetime
s = socket.socket()
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
s.connect(('10.19.154.82', 5000))
print(datetime.now())
s.send(cv2.imencode('.jpg', frame)[1])
