import zmq
import sys
from random import seed
from random import randint
import time
import hwserver

seed(1)

context = zmq.Context()

s = context.socket(zmq.REQ)
s.connect('tcp://localhost:5555')

name = sys.argv[0]

for _ in range(10):
    value = randint(0, 10)
    message = name +' '+ str(value)
    s.send_string(message)
    m = s.recv_string()
    print('Recibido' + message)
    time.sleep(value)