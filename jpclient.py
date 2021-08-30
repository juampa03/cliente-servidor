import zmq


context=zmq.Context()
s=context.socket(zmq.REQ)
s.connect("tcp://localhost:5555")
while True:
    m=input()
    s.send_string(m)
    r=s.recv_string()
    print (r)