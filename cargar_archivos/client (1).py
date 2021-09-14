import zmq
import sys
import os


def read(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        return data

def write(filename, bytes):
    with open(filename, 'wb') as file:
        file.write(bytes)

def validated(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False

def upload():
    filename = sys.argv[2]
    validar = validated(filename)
    if validar == True:
        bytes = read(filename)
        print("Enviando archivo al servidor")
        socket.send_multipart([sys.argv[1].encode('utf-8'), bytes, filename.encode('utf-8')])
        message = socket.recv()
        print(message.decode())
    else:
        print("El archivo no se encuentra")

def download():
    socket.send_multipart([sys.argv[1].encode('utf-8'), sys.argv[2].encode('utf-8')])
    message = socket.recv_multipart()
    if message[1].decode('utf-8') == 'True':
        print("Descargando archivo...")
        write(sys.argv[2], message[0])
        print("Archivo descargado correctamente")
    else:
        print(message[0].decode('utf-8'))




context = zmq.Context()

print("Conectado al servidor...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://25.98.141.90:5555")

#python client.py     download                 Litigando.docx
####################### sys.argv[1]############ sys.argv[2]


if sys.argv[1] == 'upload':
    upload()

if sys.argv[1] == 'download':
    download()

if sys.argv[1] == 'list':
    socket.send_multipart([sys.argv[1].encode('utf-8')])
    message = socket.recv_multipart()
    print(message)





