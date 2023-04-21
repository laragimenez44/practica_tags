# Título del Proyecto:  Turnero y pacientes

## Descripción del proyecto:

Este proyecto está basado en resolver un sistema de turno para una clínica odontológica privada, está dirigido en la organización de las fichas de pacientes, y realizar las altas y bajas de turnos que son expedidos por el centro odontológico en cuestión. A pedido de nuestro cliente se le darán las siguientes funcionalidades que se describen a continuación. También se tendrán en cuenta las obras sociales y pacientes para la carga en la base de datos para llevar un registro ordenado. La ejecución del programa en principio consta de poder cargar y modificar y eliminar. se crearán dos diccionarios uno para pacientes y otro de turnero.

## Funcionalidades:

Diccionario tipo de dato dict, compuesto por una clave y un valor
Pacientes (Nombre:->str, apellido:->str, dni:->int, domicilio:->str, teléfono->int, mutual->int).
Obra social (Nombre, apellido, dni, domicilio, teléfono).
Alta (asignar turnos, día y hora y crear pacientes).
Baja (cancelar el turno).
Buscar pacientes.
Reprogramar turno (modificaciones).

## Prerequisistos: 
Como requsitos solo destacaremos los principales, deberemos usar (Python) lenguaje donde se realizara el codigo,  para luego ser interpretado y ejecutado por algun interprete, tambien desde el codigo accederemos a un modulo denominado pickle siendo este de lectura y escritura.

## Instalacion:
En este caso no tendremos un ejcutable del software sino que sera ejecutado en leguaje python a traves del inrprete thony o con visual studio code, y las pruebas se realizan por consola durante la ejecucion donde se eligen la opcion correspondiente del menu e ingresamos los datos para lo que requiera el usuario. 

## Descripcion de paso a paso del sistema: 
En la ejecucion del programa, se desplegara el siguiente menu con opciones:
codigo 

El usuario introduce una opcion:
este cumple con el pedido de alta, baja y modificaciones; de turnos 
### codigo:

    def menu():
    print("--")
    print("(1) Asignar turno")
    print("(2) Cancelar turno ")
    print("(3) Crear pacientes")
    print("(4) Reprogramar turno")
    print("(5) Buscar pacientes")
    print("(6) Imprimir turno")
    print("(7) Imprimir pacientes")
    print("(8) Guardar en archivo de agenda pacientes") 
    print("(9) Leer el archivo de agenda pacientes")
    print("(10) Guardar en archivo de turnero ")
    print("(11) Leer el archivo de turnero ")
    print("(12) Salir del programa de turnero y agenda pacientes") 
    opcion = (input("Elija una opcion: "))
    return opcion

turnero = {}

agenda_de_paciente = {}

### El usuario accedera a traves del menu mediante opciones los requerimientos mas importantes es que el sistema sea un A.B.M, 
### Alta, Baja y modificaciones.- 
### Se incorpora un modulo import pickle para la lectura y escritura de archivos donde se guardaran y leeran como archivo binario.

## una vez ingresado al sistema:
Si elegimos la opción (1) se asignará un turno como alta del turnero
la opción (3) también actuará como un alta de pacientes
 
La opción (2) se tomará como la baja, esto quiere decir que eliminamos un turno y como alta se le asigna uno nuevo
 
La opción (4) que es la reprogramación de un turno se toma como modificación del turno, cumpliendo así con las características principales en cuanto al A.B.M.
 
 
Incorporamos las opciones de imprimir para visualizar los turnos o datos del paciente que han sido creados al guardados al crear el archivo con el módulo pickle, dando así como resultado la lectura del mismo.

### Pre-requisitos 📋

Para instalar el software necesitamos el lenguaje python y el intérprete  Thonny o Visual Studio Code, además necesitamos tener una carpeta con dos archivos llamados “agenda de paciente.pickle” y “Turnero.pickle”.

### Instalación 🔧
Instalación de Turnero .py

Ya teniendo instalado Python o algun interprete de lenguaje Python que pueda leer el archivo se procede a lo siguiente:
Paso 1: Abrimos la carpeta que contiene el archivo del programa . 
Paso 2 : Seleccionamos el archivo, elegimos con qué intérprete usarlo y lo cargamos.
Paso 3 : Seleccionar la opción ejecutar.
Paso 4 :  Luego de seleccionar la opción anterior se abre una pestaña, que permite guardarlo para luego poder ejecutarlo.  Al guardarlo le asignamos el nombre “Turnero.py”.
Paso 4:  En este paso volvemos a seleccionar la opción ejecutar,  este es el momento en el que el programa  da comienzo ...

Ejemplo:
Por consola escribo el comando:
>>>  python3 Turnero.py

Después de ejecutar el comando, aparecerá lo que es el menú con sus opciones. donde se elije una opción: opción “ 3) crear paciente”, donde se despliega y aparece los datos a completar del paciente. Luego de completarlo se oprime “enter” para guardar los datos.


### Ejecutando pruebas

assert es_numero ("12234563573") == True
assert es_numero ("chihuhua") == False

assert es_letra ("hola") == True
assert es_letra ("HOLA") == True
assert es_letra ("12") == False
assert es_letra ("Que") == True

## Paso a Paso de las funciones:

Primero necesitamos importar la función pickle en donde se puede guardar y leer los archivos que necesitamos. 
import pickle

A continuación creamos una función llamada “asignar turno” Esta función registra los turnos que sacan los pacientes. Me toma un diccionario llamado “turnero”, su clave es el dni (tiene que ingresar un entero) del usuario, luego con otro diccionario me tomaría los siguientes datos del paciente: nombre (string), apellido (string), el dia (string) y hora (string). 
En esta función llamada “cancelar_turno”.

def asignar_turno(turnero:dict, dni:int, nombre : str, apellido:str, dia: str, hora: str)-> None: 
   turnero[dni] = {"nombre": nombre, "apellido" : apellido, "dia" : dia, "hora" : hora}

En esta función llamada “cancelar_turno”  busca si el paciente (dni), anteriormente saco un turno, si es así elimina el turno, en caso contrario si anteriormente no saco el turno me devuelve -1 quiere decir que el turno que quiere cancelar no existe. En esta función le doy los siguientes datos: turnero (un diccionario) y el dni (int) para corroborar si ha sacado un turno.

def cancelar_turno (turnero:dict ,dni: int) -> None:
    if dni in turnero:
        del (turnero[dni]) 
        devolver = 1
    else:
        devolver = -1
    return devolver

Se define la función “crear pacientes”, me toma como argumento el diccionario “agenda de pacientes” , nombre, apellido, dni, teléfono y mutual.
En esta función y en todo el programa la clave de nuestro diccionario es “dni”. En el diccionario me toma la clave ( que sería dni) y entre las llaves se tiene el valor y nombre de las variables, que serían los datos del paciente.

def crear_pacientes(agenda_de_paciente:dict, dni: int, nombre:str, apellido: str, domicilio: str, telefono: int, mutual: str) -> None: 
    agenda_de_paciente[dni]= {"nombre": nombre ,"apellido": apellido, "domicilio": domicilio, "teléfono": telefono, "mutual": mutual }

Se define la función “Buscar Pacientes”, que toma como argumento el diccionario “agenda de pacientes” y la variable dni.
si dni  se encuentra en agenda de pacientes va a devolver la agenda con  información de un paciente. si el paciente no está registrado me devuelve -1, que este paciente no existiría.

def buscar_pacientes(agenda_de_paciente:dict, dni: int )-> None:
    if dni in agenda_de_paciente: 
        devolver= agenda_de_paciente[dni] 
    else:
        devolver= -1        
    return devolver

La función “reprogramar_turno”  recorre los turnos que han sido registrado anteriormente en el diccionario “turnero”, verifica si es la misma hora y el dia que paso el paciente, si cumple con esas condiciones me cambia la fecha y la hora que había pedido anteriormente, en caso contrario me retorna el dia y la hora. La función me toma el turnero (diccionario), dia (string),  dia_nuevo (string), hora (string), hora_nueva (string).

def reprogramar_turno(turnero:dict,dia:str,dia_nueva:str,hora:str,hora_nueva:str)->str: 
    for turno in turnero:
        if turno in turnero:
            turnero[dia]= dia_nueva
            turnero[hora]= hora_nueva
        else:
            return dia, hora

Función imprimir turno: desde el diccionario turnero recorremos los turnos de turnero para luego imprimir en pantalla; por cada turno imprime desde la clave turnos.

def imprimir_turno (turnero:dict) -> None: 
    for turnos in turnero:
      print(turnos, ":", turnero [turnos])

Función imprimir pacientes: desde el diccionario agenda pacientes este recorre a los pacientes guardados ubicados en la agenda de pacientes, para visualizarlo con print tomados desde clave pacientes.

def imprimir_pacientes(agenda_de_paciente:dict) -> None:
    for pacientes in agenda_de_paciente:
      print(pacientes, ":", agenda_de_paciente [pacientes])

Función imprimir turno modificado: toma como argumento el diccionario turnero, con for recorremos desde la variable turno y  por cada turno  el turnero y me recorra este, luego con print imprimimos del turnero (el turno reprogramado), se visualiza en consola.

def imprimir_turno_modificado (turnero: dict):
    for turno in turnero:
        print (turnero [reprogramar_turno]) 

Se crearán las siguientes funciones: tanto para los diccionarios  agenda de pacientes y turnero, al importar pickle accederemos también a la creación de archivos de lectura y escritura con sus debidos métodos
dump: volcado de datos al fichero creando un fichero binario; 
load: carga los datos de un archivo binario externo;
En el caso de la función  “guardar agenda de pacientes”  me permite crear un archivo que se guardará en la misma carpeta que se encuentra nuestro código este toma los datos del diccionario agenda de pacientes el cual con open  y “wr” (escribe binario), este escribirá el pondrá aquí la información y en conjunto con “dump” creará el fichero en cuestión también le diremos que lo cierre ya que un archivo abierto debe ser cerrado para cumplir su función,  
por ejemplo al crear un paciente desde la opción menú (3) le daremos los datos con la opción (8) guardamos y opción (9) hacemos la lectura que se mostrará en consola el cual utilizamos la función leer agenda de paciente que describe su funcionalidad en la siguientes líneas. 
En el archivo open escribimos la lista y con “rb” (lee en binario), se realiza la lectura del fichero una vez que tenemos la lista como variable le decimos “load” carga y le damos print agenda de pacientes  para ver el contenido del archivo en consola. 
En el caso de función turnero realiza los mismos pasos pero con un diccionario “turnero” realizando lo mismo pero con la diferencia de que cuando procede a  la lectura del archivo devuelve el turnero para visualizar en consola. 

def guardar_agenda_de_pacientes(agenda_de_paciente:dict, archivo="agenda de pacientes.pickle"):
    pickle_file = open(archivo, 'wb')
    print(agenda_de_paciente)
    pickle.dump(agenda_de_paciente, pickle_file)
    pickle_file.close()

def leer_agenda_de_pacientes(agenda_de_paciente:dict, archivo="agenda de pacientes.pickle"):
    pickle_file = open(archivo,'rb')
    agenda = pickle.load(pickle_file)
    print(agenda_de_paciente)
    pickle_file.close()
    return agenda_de_paciente

def guardar_turnero(turnero:dict,archivo="Turnos.pickle"):
    pickle_file = open(archivo, 'wb')
    print(turnero)
    pickle.dump(turnero, pickle_file)
    pickle_file.close()

def leer_turnero(turnero:dict,archivo="Turnos.pickle"):
    pickle_file = open(archivo,'rb')
    agenda = pickle.load(pickle_file)
    print(turnero)
    pickle_file.close()
    return turnero

### Integrantes:
Andrea Suarez.
Carolina Garaycoechea. 
Giménez Lara.











