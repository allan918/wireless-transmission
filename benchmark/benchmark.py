import server
import client
import time
server = server.Server()
client = client.Client()

total = 0
fpsTime = time.time()

for i in range(0, 5):
    client.sendFrame()
server.receive()

