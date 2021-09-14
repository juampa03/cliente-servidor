import zmq

context = zmq.Context()

x = context.socket(zmq.REP)
x.bind('tcp://*:5555')


i = 0
while True:
    m = x.recv_string()
    print('servidor recibe'+ m) 
    x.send_string(m)
    i= i + 1
    print("se atendio el memsaje{}".format(i))

    
