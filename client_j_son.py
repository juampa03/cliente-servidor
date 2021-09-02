import zmq
import json




context=zmq.Context()
s=context.socket(zmq.REQ)
s.connect("tcp://localhost:5555")


print("ingrese un numero 1")
a1=int(input())
print("operador")
op= str(input())
print("ingrese un numero 2")
a2=int(input())
m={'valor1':a1,'operador':op,'valor2':a2}
s.send_json(m)
s.recv()
print(m)
