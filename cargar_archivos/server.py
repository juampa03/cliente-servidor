import zmq
import os
import sys
from os.path import isfile, join
from os import listdir


def write(filename, bytes):
    ruta = "Files/%s" % str(filename)
    with open(ruta, 'wb') as file:
        file.write(bytes)
        file.close()

def read(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        return data

def validated(filename):
    if os.path.isfile("Files/"+filename):
        return True
    else:
        return False

def save():
    validar = validated(message[2].decode('utf-8'))
    if validar == True:
        socket.send(b'El archivo ya existe en el servidor.')
    else:
        write(message[2].decode('utf-8'), message[1])
        socket.send(b'Archivo almacenado correctamente')

def download():
    validar = validated(message[1].decode('utf-8'))
    if validar == True:
        bytes = read("Files/"+message[1].decode('utf-8'))
        socket.send_multipart([bytes, b'True'])
    else:
        socket.send_multipart([(b'El archivo solicitado no existe'), b'False'])


def listar():
    onlyfiles = [f.encode("utf-8") for f in listdir("Files/") if isfile(join("Files/", f))]
    socket.send_multipart(onlyfiles)


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Run server...")


while True:
    if not os.path.exists("Files"):
        os.mkdir("Files")
    
    message = socket.recv_multipart()
    action = message[0].decode('utf-8')

    if action == 'upload':
        save()
    if action == 'download':
        download()
    if action == 'list':
        listar()

