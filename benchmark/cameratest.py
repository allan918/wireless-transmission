import numpy as np
import cv2
import socket as s
from _datetime import datetime

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
port = 5000
hostname = s.gethostname()
socket.connect(("10.154.32.11", port))
##c, address = socket.accept()
print("connection succeed!")
while True :
    data = c.recv(1024)
    if not data:
        break;
    print("data received", str(data), "at", str(datetime.now()))
#
#
# cap = cv2.VideoCapture(0)
#
# # while(True):
# #     # Capture frame-by-frame
# ret, frame = cap.read()
# print(ret)
# #
# #     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()