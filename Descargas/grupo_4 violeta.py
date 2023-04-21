import pickle
def asignar_turno(turnero:dict, dni:int, nombre : str, apellido:str, dia: str, hora: str)-> None:  
    turnero[dni] = {"nombre": nombre, "apellido" : apellido, "dia" : dia, "hora" : hora}


def cancelar_turno (turnero:dict ,dni: int) -> None:
    if dni in turnero:
        del (turnero[dni]) 
        devolver = 1
    else:
        devolver = -1
    return devolver


def crear_pacientes(agenda_de_paciente:dict, dni: int, nombre:str, apellido: str, domicilio: str, telefono: int, mutual: str) -> None: 
    agenda_de_paciente[dni]= {"nombre": nombre ,"apellido": apellido, "domicilio": domicilio, "teléfono": telefono, "mutual": mutual }

#Lara

def buscar_pacientes(agenda_de_paciente:dict, dni: int )-> None:
    if dni in agenda_de_paciente:
        devolver= agenda_de_paciente[dni] 
    else:
        devolver= -1
    return devolver

#Lara

def reprogramar_turno(turnero:dict,dia:str,dia_nueva:str,hora:str,hora_nueva:str)->str: #dni
    for turno in turnero:    
        if turno in turnero:
            turnero[dia]= dia_nueva
            turnero[hora]= hora_nueva
        else:
            print ("No a sacado un turno")
            return turno

#Andrea

def imprimir_turno (turnero:dict) -> None:
    for turnos in turnero:
      print(turnos, ":", turnero [turnos])

#Caro

def imprimir_pacientes(agenda_de_paciente:dict) -> None:
    for pacientes in agenda_de_paciente:
      print(pacientes, ":", agenda_de_paciente [pacientes])
  
#Lara

def imprimir_turno_modificado (turnero: dict):
    for turno in turnero:
        print (turnero [reprogramar_turno])      
    
#Caro

def guardar_agenda_de_pacientes(agenda_de_paciente:dict, archivo="agenda de pacientes.pickle"):
    pickle_file = open(archivo, 'wb')
    print(agenda_de_paciente)
    pickle.dump(agenda_de_paciente, pickle_file)
    pickle_file.close()

#Andrea

def leer_agenda_de_pacientes(agenda_de_paciente:dict, archivo="agenda de pacientes.pickle"):
    pickle_file = open(archivo,'rb')
    agenda = pickle.load(pickle_file)
    print(agenda_de_paciente)
    pickle_file.close()
    return agenda_de_paciente

# 

def guardar_turnero(turnero:dict,archivo="Turnos.pickle"):
    pickle_file = open(archivo, 'wb')
    print(turnero)
    pickle.dump(turnero, pickle_file)
    pickle_file.close()

#Andrea

def leer_turnero(turnero:dict,archivo="Turnos.pickle"):
    pickle_file = open(archivo,'rb')
    turnos= pickle.load(pickle_file) #corregi el nombre
    print(turnero)
    pickle_file.close()
    return turnero

def es_numero(entrada: str)-> bool:
    digitos = ["0","1","2","3","4","5","6","7","8","9"]
    devolver = True
    for numero in entrada:
        if numero not in digitos:
            devolver = False
    return devolver

assert es_numero ("12234563573") == True
assert es_numero ("chihuahua") == False

#Caro

def es_letra(entrada: str)-> bool:
    abecedario_1 = ["a","b","c","d","e","f","g","h","i","j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    abecedario_2 = ["A","B","C","D","E","F","G","H","I","J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    devolver = True
    for letra in entrada:
        if letra not in abecedario_1 and letra not in abecedario_2:
            devolver = False
    return devolver

assert es_letra ("hola") == True
assert es_letra ("HOLA") == True
assert es_letra ("12") == False
assert es_letra ("Que") == True

#Lara

def menu():
    print("--")
    print("(1) Asignar turno")
    print("(2) Cancelar turno")
    print("(3) Crear pacientes")
    print("(4) Reprogramar turno")
    print("(5) Buscar pacientes")
    print("(6) Imprimir turno")
    print("(7) Imprimir pacientes")
    print("(8) Guardar en archivo de agenda pacientes") 
    print("(9) Leer el archivo de agenda pacientes")
    print("(10) Guardar en archivo de turnero")
    print("(11) Leer el archivo de turnero")
    print("(12) Salir del programa de turnero y agenda pacientes") 
    opcion = (input("Elija una opcion: "))
    return opcion

turnero = {}
agenda_de_paciente = {}

lista= ["1", "2", "3", "4", "5", "6", "7" ,"8", "9", "10", "11", "12"] 
inicio = input ("Quiere ingresar al sistema de turno? (0)no, (1)si: ")
if inicio != "1":
    print ("Salio del programa.")
else:
    while inicio == "1":  
        opcion = menu()
        if opcion not in ["1", "2", "3", "4", "5", "6", "7" ,"8", "9", "10", "11", "12" ]:
            print ("intente nuevamente. ")
            break
        else:
            if opcion in ["1", "2", "3", "4", "5", "6", "7" ,"8", "9", "10", "11" ] :
                if opcion == "1":
                    print ("Debe de ingresar numeros, no se permite otro caracter.")
                    dni = input ("ingrese su DNI: ")
                    lista_de_dni_posibles= []
                    for turno in turnero:
                        dni = str (turno["dni"])
                        lista_de_dni_posibles.append(dni)
                    if lista_de_dni_posibles == es_numero:
                        print (" Se agrego el dni.") 
                    else:
                        print("No ingreso bien el caracter.")
                    print ("Debe de ingresar letras, no se permite otro tipo de caracter.")
                    nombre= input (" Ingrese su nombre: ")
                    lista_de_nombres_posibles= []
                    for nombre in turnero:
                        nombre = str (turno["nombre"])
                        lista_de_nombres_posibles.append(nombre)
                    if  lista_de_nombres_posibles == es_letra:
                        print ("Se agrego su nombre.")
                    else:
                        print("no aceptamos ese tipo de caracteres.")
                    print ("Debe de ingresar letras, no se permite otro tipo de caracter.")
                    apellido = input ("Ingrese su apellido: ")
                    lista_de_apellidos_posibles= []
                    for apellidos in turnero:
                        apellidos = str (turno["apellidos"])
                        lista_de_apellidos_posibles.append(apellidos)
                    if lista_de_apellidos_posibles == es_letra:
                        print ("Se agrego el apellido.")
                    else:
                        print("No aceptamos ese tipo de caracteres.")
                    print ("Debe de ingresar numeros, por ejemplo doce de marzo, no se permite otro tipo de caracter.")
                    dia = input ("Ingrese el dia: ")
                    lista_de_dia_posibles= []
                    for dia in turnero:
                        dia = str (turno["dia"])
                        lista_de_dia_posibles.append(dia)
                    if lista_de_dia_posibles == es_letra:
                        print ("Se agrego el dia.")
                    else:    
                        print("No aceptamos ese tipo de caracteres.")
                    print ("Debe de ingresar numeros por ejemplo: dieciocho y treinta, no se permite otro tipo de caracter.")
                    hora  =  input ("Ingrese la hora: ")
                    lista_de_hora_posibles= []
                    for hora in turnero:
                        hora = str (turno["hora"])
                        lista_de_hora_posibles.append(hora)
                    if lista_de_hora_posibles == es_letra:
                        print ("Se agrego la hora.")
                    else:  
                        print("No aceptamos ese tipo de caracteres.")
                    asignar_turno (turnero, dni, nombre, apellido, dia, hora)
                    print ("El turno ya se registro.")

                if opcion == "2":
                    print ("Debe de ingresar numeros, no se permite otro caracter.")
                    dni = input ("ingrese su DNI: ")
                    for dia in turnero:
                        dni = str (turno["dni"])
                        lista_de_dni_posibles.append(dni)
                    if lista_de_dni_posibles == es_letra:
                        print (" Se agrego el dni.") 
                    else:
                        print("No ingreso bien el caracter.")
                    respuesta = cancelar_turno(turnero,dni)
                    if respuesta != -1:
                        print (f"{dni} ha sido eliminado del turnero.")
                    else:
                        print (f"{dni} no se encuentra en la turnero.")   
                
                if opcion == "3":
                    print ("Debe de ingresar numeros, no se permite otro caracter.")
                    dni = input ("ingrese su DNI: ")
                    lista_de_dni_posibles= []
                    for dni in agenda_de_paciente:
                        dni = str (dni["dni"])
                        lista_de_dni_posibles.append(dni)
                    if lista_de_dni_posibles == es_numero:
                        print (" Se agrego el dni.") 
                    else:
                        print("No ingreso bien el caracter.")
                    print ("Debe de ingresar letras, no se permite otro tipo de caracter.")
                    nombre = input ("Ingrese su nombre: " )
                    for nombre in agenda_de_paciente:
                        nombre = str (nombre["nombre"])
                        lista_de_nombres_posibles.append(nombre)
                    if lista_de_nombres_posibles == es_letra:
                        print ("Se agrego su nombre.")
                    else:
                        print("No aceptamos ese tipo de caracteres.")
                    print ("Debe de ingresar letras, no se permite otro tipo de caracter.")
                    apellido = input ("Ingrese su apellido: ")
                    for apellido in agenda_de_paciente:
                        apellido = str (apellido["apellido"])
                        lista_de_apellidos_posibles.append(apellido)
                    if lista_de_apellidos_posibles == es_letra:
                        print ("Se agrego su apellido.")
                    else:
                        print("No aceptamos ese tipo de caracteres.")
                    print ("Debe de ingresar letras, no se permite otro tipo de caracter.")
                    domicilio = input ("Ingrese su domicilio: ")
                    lista_de_domicilio_posibles= []
                    for domicilio in agenda_de_paciente:
                        domicilio = str (domicilio["domicilio"])
                        lista_de_domicilio_posibles.append(domicilio)
                    if lista_de_domicilio_posibles == es_letra:
                        print ("Se agrego su domicilio.")
                    else:
                        print("No aceptamos ese tipo de caracteres.")
                    print ("Debe de ingresar numeros, no se permite otro caracter.")
                    telefono = int(input ("Ingrese su telefono: "))
                    lista_de_telefono_posibles= []
                    for telefono in agenda_de_paciente:
                        telefono = str (telefono["telefono"])
                        lista_de_telefono_posibles.append(telefono)
                    if lista_de_telefono_posibles == es_numero:
                        print ("Se agrego su telefono.")
                    else:
                        print("No aceptamos ese tipo de caracteres.")
                    print ("Debe de ingresar letras, no se permite otro tipo de caracter.")
                    mutual = input ("Ingrese su mutual: ")
                    lista_de_mutual_posibles= []
                    for mutual in agenda_de_paciente:
                        mutual = str (mutual["mutual"])
                        lista_de_mutual_posibles.append(mutual)
                    if lista_de_mutual_posibles == es_letra:
                        print ("Se agrego su mutual.")
                    else:
                        print("No aceptamos ese tipo de caracteres.")
                    crear_pacientes( agenda_de_paciente ,dni,nombre, apellido, domicilio, telefono, mutual)
                    print("EL paciente ya esta agregado.")    
                
                if opcion == "4":
                    for turno in turnero:
                        if turno in turnero:
                            print ("Debe de ingresar numeros por ej 12/11, no se permite otro caracter.")
                        dia = input ("Ingrese la fecha nueva: ")
                        for dia in turnero:
                            dia = str (dia["dia"])
                        lista_de_dia_posibles.append(dia)
                        if lista_de_dia_posibles == es_letra:
                            print("ya se agrego el dia.")
                        else:
                            print("no aceptamos ese tipo de caracteres.")
                        print ("Debe de ingresar numeros por ej 12:30, no se permite otro caracter.")
                        hora = input ("Ingrese la hora nueva: ")
                        for hora in turnero:
                            hora= str (hora["hora"])
                        lista_de_hora_posibles.append(hora)
                        if lista_de_hora_posibles == es_letra:
                            #llamar a la funcion
                            print ("Se agrego la hora.")
                        else:
                            print("no aceptmos ese tipo de caracteres.")
                        print ("Su turno ya a sido reprogramado")
                    else:
                        print("no a sacado un turno anteriormente.")      
                
                if opcion == "5":
                    print ("Debe de ingresar numeros, no se permite otro caracter.")
                    dni = input ("ingrese su DNI: ")
                    lista_de_dni_posibles= []
                    for dni in agenda_de_paciente:
                        dni = str (turno["dni"])
                        lista_de_dni_posibles.append(dni)
                    if lista_de_dni_posibles == es_numero:
                        print (" Se agrego el dni.") 
                    else:
                        print("No ingreso bien el caracter.")
                    respuesta = buscar_pacientes(agenda_de_paciente,dni)
                    if respuesta != -1:
                        print (f"El dni del {nombre} es: {respuesta}")
                    else:
                        print (f"{nombre} no se encuentra en la agenda de pacientes.")
                
                if opcion == "6":
                    imprimir_turno (turnero)
                    
                if opcion == "7":
                    imprimir_pacientes(agenda_de_paciente)
            
                if opcion == "8":
                    guardar_agenda_de_pacientes(agenda_de_paciente)
                
                if opcion == "9":
                    leer_agenda_de_pacientes(agenda_de_paciente)   

                if opcion == "10":
                    guardar_turnero( turnero == guardar_turnero)

                if opcion == "11":
                    leer_turnero(turnero)   
            
            if opcion == "12":
                break