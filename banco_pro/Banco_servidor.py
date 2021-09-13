import zmq
import json
import sys


context=zmq.Context()

cliente=context.socket(zmq.REP)
cliente.bind("tcp://*:5555")


accounts ={}

while True:
    print(accounts)
    m = cliente.recv_json()
    print("hola")
    if m["transaction"] =="crear":
        if m["username"] in accounts:
            cliente.send_json({"result":"error","info":"usuario existente"})
        else:
            accounts [m["username"]] = m["balance"]
            cliente.send_json({"result": "ok"})
    else: 
            cliente.send_json({"result": "error","info": "no implementado"})
else:
    


    


         
          