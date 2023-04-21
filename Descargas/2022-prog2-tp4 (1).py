"""
Programación 1 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiantes:Lara Anahí Giménez 

Práctico 4: diccionarios
"""

"""
Ejercicio 1:
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe 
mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

nombre: str = input ("Escriba su nombre: ")
edad= int(input ("Escriba su edad: "))
direccion: str = input ("Escriba su dirección: ")
telefono =int (input ("ingrse su telefono: "))

datos_del_usuario = {
    'nombre' : nombre,
    'edad' : edad,
    'direccion' : direccion,
    'telefono' : telefono
}

print (f" {datos_del_usuario ['nombre']} tiene {datos_del_usuario  ['edad']} años, vive en {datos_del_usuario ['direccion']} y su número de teléfono es {datos_del_usuario ['telefono']}")

"""
Ejercicio 2:
    Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un
    número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
    mostrar un mensaje informando de ello.
Fruta 	Precio
Plátano 	1.35
Manzana 	0.80
Pera 	0.85
Naranja 	0.70
"""

diccionario_fruta = {
    'Plátano' : 1.35,
    'Manzana' : 0.80,
    'Pera' : 0.85,
    'Naranja' : 0.70
}

fruta: str= input("que fruta necesita?: ")

if fruta in diccionario_fruta:
    kilos = float (input (f"cuantos kilos de {fruta} quiere?: "))
    print (f"{kilos} kilos de {fruta} cuestan $ {diccionario_fruta[fruta]* [kilos]}")
else:
    print (f"{fruta} no se encuentra disponible")


"""
Ejercicio 3:
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, 
sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el 
contenido del diccionario.
"""

datos_del_usuario = {}
nombre: str = input ("Escriba su nombre: ")
edad= int(input ("Escriba su edad: "))
sexo: str = input ("Escriba su sexo: ")
telefono =int (input ("ingrse su telefono: "))
correo_electrónico: str = input ("escriba su correo electronico")
direccion: str = input ("Escriba su dirección: ")

diccionario = {
    'nombre' : nombre,
    'edad' : edad,
    'sexo' : sexo,
    'telefono' : telefono,
    'correo electrónico' : correo_electrónico,
    'direccion' : direccion,
}

print (f" {diccionario ['nombre']} tiene {diccionario ['edad']} años, vive en {diccionario['direccion']} y su número de teléfono es {diccionario['telefono']}")

"""
Ejercicio 4:
    Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su 
    precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la
    compra y el coste total, con el siguiente formato
Lista de la compra 	
Artículo 1 	Precio
Artículo 2 	Precio
Artículo 3 	Precio
… 	…
Total 	Coste
"""

cesta_de_la_compra= {}
i: int= 0
respuesta= True
while respuesta:
    articulo: str= input (" que articulo quiere: ")
    precio_1: str= input (" cuanto sale el articulo: ")
    precio: int= int (precio_1)
    contador= 0
    i= i + 1
    respuesta: str= input("quiere seguir, si/no: ") == "si"
    contador= contador + precio
print("Lista de la compra")
print (f"El articulo: {articulo} {i} su precio: {precio}")
print("… 	…")
print (f"Total de coste {contador}")


"""
* Ejercicio 5.1
Definir un diccionario que almacene los nombres de países como clave y como valor la cantidad de habitantes.
Valores a guardar:

Brasil 210147125
Colombia 50372424
Argentina 44938712
Perú 32131400
Venezuela 28670000
Chile 19107216
Ecuador 17300000
Bolivia  11383940
Paraguay 7152703
Uruguay 3529140
Guyana 761000
Surinam 524000
Guayana Francesa 187000
"""
d= {}

d['Brasil']= 210147125
d['Colombia']= 50372424
d['Argentina']= 44938712
d['Perú']= 32131400
d['Venezuela']= 28670000
d['Chile']= 19107216
d['Ecuador']= 17300000
d['Bolivia']= 11383940
d['Paraguay']= 7152703
d['Uruguay']= 3529140
d['Guyana']= 761000
d['Surinam']= 524000
d['Guayana Francesa']= 187000 

assert d['Argentina'] == 44938712

"""
* 5.2
Implementar una procedimiento para mostrar cada clave y valor.
(nota) los procedimientos son como las funciones pero no devuelven un valor
"""
def mostrar_diccionario(d:dict)->None:
    for paises in d:
        print (d)

"""
* 5.3
Implementar una función que tome el diccionario,
calcule la poblacion total de latinoamerica y devuelva el valor (pista, usar un for para recorrer el diccionario)
"""

def calcular_poblacion(d:dict)->int:
    habitantes= 0
    for habitante in d:
        habitantes= sum (d.values())
        return habitantes

assert calcular_poblacion(d) == 426204660

"""
* Ejercicio 6
Escribir un programa que cree un diccionario de traducción inglés-español.
El programa debe crear un diccionario con las palabras y sus traducciones.

Después pedirá una frase en inglés y utilizará el diccionario para
traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir."""

def agregar_palabra(d:dict , ingles:str, esp:str)-> None:
    dic[ingles] = esp #diccionario -> ingles (clave y valor) -> español 

def traducir(d:dict, frase:str) -> str:
    frase_nueva= []
    for i in frase.split():
        if i in dic:
            frase_nueva.append(d[i])
        else:
            frase_nueva.append(d[i])
    
    frase_nueva= (" ").join(d[i])
    print(frase_nueva)
    return frase_nueva

dic = {}
dic["dog"]= "perro"
dic["the"]= "el"
dic["eat"]= "comer"
dic["dinner"]= "cena"

agregar_palabra(dic,"dog","perro")
agregar_palabra(dic,"the","el")
agregar_palabra(dic,"eat","comer")
agregar_palabra(dic,"dinner","cena")

assert traducir(dic,"the dog eat the dinner late") == "el perro comer el cena late"


# Ejercicio 7
"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario
en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

    Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    Preguntar por el NIF del cliente y mostrar sus datos.
    Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    Terminar el programa.
"""