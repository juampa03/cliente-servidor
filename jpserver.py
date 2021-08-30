import zmq

context=zmq.Context()
s=context.socket(zmq.REP)
s.bind("tcp://*:5555")

while True:
	r=0
	m=s.recv_string()
	maux=m.split("")   #formato envio2 + 2 = 2+2
	a= int(maux[0])
	sig= str(maux[1])
	b= int(maux[2])
    
	if sig == "+":
		r=a+b
	elif sig == "-":
		r=a-b
	elif sig == "*":
		r=a*b
	elif sig == "/":
		r=a/b
	else:
		print("null")
	print(r)
	s.send_string(str(r))