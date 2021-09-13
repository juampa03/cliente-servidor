        
import zmq
import json
import sys


context=zmq.Context()

servidor=context.socket(zmq.REP)
servidor.bind("tcp://*:5555")

accounts ={}

while True:
    request = servidor.recv_json()
    #pasamos a diccionario
    request_dictictionary = json.loads(request)




    if request_dictictionary["modelo"] == 'crear':
        #creamos un nuevo objeto en python
        nombre = request_dictictionary["nombre"]
        saldo = request_dictictionary["saldo"]  
        #verificamos la existencioa del nuevo contacto
        if nombre in accounts:
            servidor.send_string('\nUsuario ya existe !!')
        else:
            nuevo_dato = {nombre:saldo}
            accounts.update(nuevo_dato)
            response = f'\nagregado->{nombre} con saldo {accounts[nombre]}\n'
            servidor.send_string(response)

    elif request_dictictionary["modelo"] == 'deposito':
        if nombre in accounts:
            nombre = request_dictictionary["nombre"]
            nuevo_saldo = accounts[nombre]+request_dictictionary["saldo"]
            depositado = {nombre:nuevo_saldo}
            accounts.update(depositado)
            response= f'\nNuevo saldo de {nombre} es {accounts[nombre]}\n'
            servidor.send_string(response)
        else:
            servidor.send_string('\nusuario no encontrado')


        
    elif request_dictictionary["modelo"] == 'mostrar':
        
        nombre = request_dictictionary["nombre"]
        #verificamos la existencia de los usuarios
        if nombre in accounts:
            response= f'\nEl saldo de {nombre} es: {accounts[nombre]}\n'
            servidor.send_string(response)
        else:
            servidor.send_string('\nUsuario no encontrado !!')

    elif request_dictictionary["modelo"] == 'transf':
        
        remitente = request_dictictionary["remitente"]
        destinatario = request_dictictionary["destinatario"]
        saldo = request_dictictionary["saldo"]
        
        #verificamos la existencia de los usuarios
        if remitente in accounts and destinatario in accounts:
                #verificamos la disponibilidad del remitente
            check_saldo = accounts[remitente] - saldo
            if check_saldo < 0:
                servidor.send_string('\nSaldo insuficiente')
            else:
                #creamos una nueva lista y la actualizamos al accounts
                nuevo_saldo_remitente = accounts[remitente]-saldo
                nuevo_remitente = {remitente : nuevo_saldo_remitente}
                accounts.update(nuevo_remitente)
                
                nuevo_saldo_destinatario = accounts[destinatario]+saldo
                nuevo_destinatario = {destinatario : nuevo_saldo_destinatario}
                accounts.update(nuevo_destinatario)
                response= f'\nTransferencia de {remitente} a {destinatario} por {saldo}\n'
                servidor.send_string(response)
        # usuario no exista
        else:
            servidor.send_string('\nusuario no encontrado')
        
    
    
    
    


   
          