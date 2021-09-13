import zmq
import json

context=zmq.Context()
s=context.socket(zmq.REP)
s.bind("tcp://*:5555")

while True:
    l=s.recv_json()
    res =""
    if l['operador']=='+':
        res=str(l['valor1'] + l['valor2'])
    elif l['operador']=='-':
        res=str(l['valor1'] - l['valor2'])
    elif l['operador']=='x':
        res=str(l['valor1'] * l['valor2'])
        print("se resolvio una mul"+res)
    elif l['operador']=='/':
        res=str(l['valor1'] / l['valor2'])

    s.send(res.encode('utf-8'))
    
    
