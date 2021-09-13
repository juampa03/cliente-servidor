import zmq
import json
import sys
import time

context=zmq.Context()

servidor=context.socket(zmq.REQ)
servidor.connect("tcp://localhost:5555")

def menu():
    print('A-----Crear cuenta ---\nB-----Transferir saldo ----\nC-----Ver saldo -----\nD-----Depositar saldo ------\nE-----*Retirar saldo------')
    print('Seleccione una opcion!! ')
    selector = str(input())
    return selector

def JSON_crear():
    nombre = input("\nnombre: ")
    saldo = int(input("saldo: "))
    crear = json.dumps(
            {
                "modelo" : "crear",
                "nombre" : nombre,
                "saldo" : saldo
            }
        )  
    return crear      

def Json_depositar():
    nombre = input("\nnombre: ")
    saldo = int(input("\nsaldo a depositar: "))
    
    depositar = json.dumps(
            {
                "modelo": 'deposito',
                "nombre": nombre,
                "saldo": saldo
            }
        )
    return depositar 

def Json_transferir():
    remitente = input("\nremitente: ")
    destinatario = input("\ndestinatario: ")
    saldo = int(input("\nsaldo: "))
    
    mostrar = json.dumps(
            {
                "modelo": 'transf',
                "remitente": remitente,
                "destinatario" : destinatario,
                "saldo": saldo
            }
        )
    return mostrar

def JSON_mostrar():
    nombre = input("\nnombre: ")
    mostrar = json.dumps(
            {
                "modelo" : "mostrar",
                "nombre" : nombre,
            }
        )
    return mostrar

    
while True:
    
    selector = menu()
    
    if selector == 'A':
        request_crear = JSON_crear()
        servidor.send_json(request_crear)
        
    elif selector == 'B':
        request_transferir = Json_transferir()
        servidor.send_json(request_transferir) 
        
    elif selector == 'C':
        request_mostrar = JSON_mostrar()
        servidor.send_json(request_mostrar)        
    
    elif selector == 'D':
        request_depositar = Json_depositar()
        servidor.send_json(request_depositar)        
    
    elif selector == 'E':
        request_retirar = JSON_retirar()
        servidor.send_json(request_retirar)        
    else:
        print('seleccion no valida')
    
    response = servidor.recv_string()
    print(response)
    time.sleep(3)
    
        

    
  
