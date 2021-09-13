import zmq
import json
import sys


context=zmq.Context()

servidor=context.socket(zmq.REQ)
servidor.connect("tcp://localhost:5555")

username = sys.argv[1]
transaction = sys.argv[2]


if transaction == 'crear':
    balance = sys.argv[3]
    servidor.send_json(
        {"username":username,
         "transaction":transaction,
         "balance": int(balance)}
    )
    m = servidor.recv_json()
    print(m)
else:
    print("operacion")