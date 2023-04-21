"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiante: Lara Giménez

Práctico 1: Repaso comandos programación 1 - Programación imperativa Python
"""

# 1 Ejercicio entrada, salida y aritmética:

#print ("CALCULO DE LA MEDIA")
#pedimos la entrada al usuario
#entrada_1: str = input ("Escriba el primer numero: ")
#numero_1 : int = int (entrada_1)
#entrada_2 : str = input ("Escriba el segundo numero: ")
#numero_2: int = int (entrada_2)

#Ahora calculamos el resultado
#resultado : float = (numero_1 + numero_2) / 2
#print("la media es" ,resultado)

# 2* Ejercicio entrada, salida y aritmética:

from cmath import sqrt

#ancho_del_rectangulo: str = input("Escriba la anchura del rectangulo: ")
#ancho: int = int (ancho_del_rectangulo)
#altura_del_rectangulo: str = input ("escriba la altura del rectangulo: ")
#altura : int = int (altura_del_rectangulo) 
#if altura > 0 and ancho > 0:
#    area = ancho * altura
#    print ("el area de un rectangulo es: ", area)
#    perimetro = (ancho *2) + (altura *2)
#    print ("el perimetro del rectangulo es: ", perimetro)
#    diagonal= sqrt ((ancho**2) + (altura**2) )
#    print ("la diagonal del rectangulo es: ", diagonal)
#else:
#    print ("Ingrese un valor mayor que 0")

# ejercicio 3
#v = x <= -7 # x tiene que ser mas chico que -7.
#v = x > 16  # x tiene que ser mas grande que 16.   
#v = x != -33 # x tiene que ser distinto de -33.

# 4 Expresion Lógica o Booleana
"""Reemplace x por un valor que haga v == False, describa como comentario que tiene que pasar para que v sea False"""

#v = x <= -7 # x tiene que ser mas grande que _-7 para que te de false.
#v = x > 16 # x tiene que menor o igual a 16 para que te de False.
#v = x != -33 # x tiene que ser igual a -33 para que de False.

# 5* Expresion Lógica o Booleana
"""asigne a x un valor para hacer v == True"""

#x = #Escriba un valor aquí: 1
#v = x <= 1 and x != -75 or x == 48
#x = #Escriba un valor aquí: 71
#x > -71 and x != 7 and x != 75
#x = #Escriba un valor aquí: -117
#x >= -117 and x <= -45 or x > 19


# 6 Ejercicio if
"""
Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.

COMPARADOR DE NÚMEROS
Escriba un número: 23
Escriba otro número: 14.5
Menor: 14.5; Mayor: 23.0
---
COMPARADOR DE NÚMEROS
Escriba un número: 23
Escriba otro número: 23
Los números son iguales
"""

#print ("comprador de numeros") 
#entrada1 : str = input ("escriba un numero: ")
#numero1 : float = float (entrada1)
#entrada2: str = input("escriba otro numero: ")
#numero2 : float = float (entrada2) 

#if numero1 == numero2:
#    print ("los numeros son iguales ")
#elif numero1 < numero2:
#    print (f"menor {numero1} ; mayor: {numero2}" )
#else:
#    print (f"menor {numero2} ; mayor: {numero1}" )

# 7* if (2)
""" Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuánto
años faltan para llegar a ese año.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 2024
Para llegar al año 2024 faltan 5 años.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 1997
Desde el año 1997 han pasado 22 años.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 2019
¡Son el mismo año!
"""
#print ("COMPARADOR DE AÑOS")
#COMPARADOR_DE_AÑOS_ACTUAL: str = input ("¿En qué año estamos?: ")
#año_actual : int = int (COMPARADOR_DE_AÑOS_ACTUAL)
#COMPARADOR_DE_AÑOS_CUALQUIERA: str = input ("Escriba un año cualquiera:")
#año_cualquiera: int = int (COMPARADOR_DE_AÑOS_CUALQUIERA)
#if año_actual < año_cualquiera:
#    resultado_1= año_cualquiera - año_actual
#    print (f"Para llegar al año {año_actual} faltan {resultado_1} años.")
#elif  año_actual > año_cualquiera:
#    resultado_2= año_actual - año_cualquiera
#    print (f"Desde el año {año_cualquiera} han pasado {resultado_2} años. ")
#else:
#    año_actual == año_cualquiera
#    print ("¡Son el mismo año!")


# 8 For 
""" Escriba un programa que imprima 10 veces "Tengo que hacer la tarea"

Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
"""

#for i in range (10):
#    print ("Tengo que hacer la tarea" )

# 9 For 
""" Escriba un programa que ayude a recordar una tabla de multiplicar 

¿Cual tabla quiere repasar?: 5
¡Perfecto!
1	x 	5 	= 	5
2 	x 	5 	= 	10
3	x 	5 	= 	15
4 	x 	5 	= 	20
5	x 	5 	= 	25
6 	x 	5 	= 	30
7	x 	5 	= 	35
8 	x 	5 	= 	40
9	x 	5 	= 	45
10 	x 	5 	= 	50
"""

#Entrada =int (input ("¿Cual tabla quiere repasar?: ") )
#print ("¡Perfecto!")
#for i in range (1,11):
#    print ((i), "x" ,(Entrada) , "=" ,(i*Entrada) )

# 10 For
""" Escriba un programa que ayude a recordar una tabla de multiplicar , ahora pidiendo al usuario que ingrese el valor

¿Cual tabla quiere repasar?: 5
¡Perfecto!
1	x 	5: 5
Bien
2 	x 	5: 15
Nop
3	x 	5: 	15
Bien
4 	x 	5 	= 	25
Nop
5	x 	5 	= 	25
Bien
6 	x 	5 	= 	30
Bien
7	x 	5 	= 	35
Bien
8 	x 	5 	= 	40
Bien
9	x 	5 	= 	45
Bien
10 	x 	5 	= 	50
Bien
"""
#tabla= int (input ("ingrese la tabla que quiere repasar: "))
#num_tabla: int =int (tabla)
#for i in range (1,11):
#	resultado= input (f"ingrese el resultado: {i} x {num_tabla} = ")
#	numero: int = int (resultado)
#	print (f" {i} x {num_tabla} = {numero}")
#	if i*num_tabla ==numero:
#		print ("bien")
#	else:
#		i*num_tabla !=numero
#		print ("mal")


# 11* For (acumulador)
"""
Escriba un programa que pregunte cuantos tickets tiene, luego le pida el monto gastado con cada ticket e imprime el monto total al final

SUMA DE VALORES
¿Cuántos valores va a introducir? -1
¡Imposible!

SUMA DE VALORES
¿Cuántos valores va a introducir? 5
Escriba el ticket 1: 25
Escriba el ticket 2: 30
Escriba el ticket 3: 10.5
Escriba el ticket 4: 14
Escriba el ticket 5: 23
La suma de los números que ha escrito es 102.5
"""

#print ("SUMA DE VALORES")
#entrada: str= input ("¿Cuantos valores va a introducir?:  ")
#tickets :int = int (entrada)
#contador = 0
#if tickets < 0:
#	print ("¡Imposible!")
#else:
#    for i in range (tickets):
#        monto_gastado: str= input (f"¿Cuanto gasto en con cada tickets {i+1}: ")
#        monto: float = float (monto_gastado)
#        contador =  contador + monto
#    print (contador)
	
# 12 While
""""Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que
las dos contraseñas coincidan, con un límite de tres peticiones.

CONFIRME SU CONTRASEÑA (2)
Escriba su contraseña: cantidubi dubi dubi
Tiene 3 intentos para confirmar su contraseña.
Escriba de nuevo su contraseña: cantidubi dubi da
Las contraseñas no coinciden. Inténtelo de nuevo.
Escriba de nuevo su contraseña: cantidubi dubi dubi
Contraseña confirmada. ¡Hasta la vista!

CONFIRME SU CONTRASEÑA
Escriba su contraseña: pezespada
Tiene 3 intentos para confirmar su contraseña.
Escriba de nuevo su contraseña: Pezespada
Las contraseñas no coinciden. Inténtelo de nuevo.
Escriba de nuevo su contraseña: pezEspada
Las contraseñas no coinciden. Inténtelo de nuevo.
Escriba de nuevo su contraseña: PezEspada
Lo siento, no ha confirmado la contraseña. ¡Hasta la vista!
"""
#entrada_1 = input("Escriba su contraseña: ")
#contraseña: str = str (entrada_1)
#intentos=3
#print ("Tiene 3 intentos para confirmar su contraseña.")
#entrada_2= input("Escriba de nuevo su contraseña: ")
#primer_intento: str = str (entrada_2)
#contador= 1
#while contraseña != primer_intento and contador < intentos:
#    print ("Las contraseñas no coinciden. Inténtelo de nuevo.")
#    entrada_3 = input("Escriba de nuevo su contraseña: ")
#    segundo_intento : str = str (entrada_3) 
#    contador = contador +1
#    if contraseña != entrada_3:
#      print ("Lo siento, no ha confirmado la contraseña. ¡Hasta la vista!")
#    else:
#        contraseña == entrada_3
#print("Contraseña confirmada. ¡Hasta la vista!")


# 13* While (acumulador) - Ahora sesuelva el ejercicio 11 usando el while
"""
Escriba un programa que pregunte cuantos tickets tiene, luego le pida el monto gastado con cada ticket e imprime el monto total al final

SUMA DE VALORES
¿Cuántos valores va a introducir? -1
¡Imposible!

SUMA DE VALORES
¿Cuántos valores va a introducir? 5
Escriba el ticket 1: 25
Escriba el ticket 2: 30
Escriba el ticket 3: 10.5
Escriba el ticket 4: 14
Escriba el ticket 5: 23
La suma de los números que ha escrito es 102.5
"""

#print ("SUMA DE VALORES")
#entrada: str= input ("¿Cuantos valores va a introducir?:  ")
#tickets :int = int (entrada) 
#contador = 0
#i= 0
#if tickets < 0:
#      print ("¡Imposible!")
#else:
#    while i < tickets: 
#      i= i + 1
#      cantidad_de_tickets: str= input (f"Escriba el ticket {i} : ")
#      monto : float = float (cantidad_de_tickets)
#      contador= contador + monto 
#print (f"La suma de los números que ha escrito es {contador}")

# 14 While
""" Escriba un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario tiene que adivinarlo).
El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y después el usuario va 
probando valores y el programa va diciendo si son demasiado grandes o pequeños.

Valor mínimo: 0
Valor máximo: 100
Intente adivinar un número entero entre 0 y 100.
Escriba un número: 20
¡Demasiado pequeño! Inténtelo de nuevo: 30
¡Demasiado grande! Inténtelo de nuevo: 27
¡Acertó! Le ha costado 3 intentos.
"""

import random
a= random.randint(1,100)
print ("Intente adivinar un número entero entre 0 y 100.")
contador= 0
numero_1 = -1
while numero_1 != a and contador < 6:
    adivinar= input ("Escriba un número: ")
    numero_1: int = int (adivinar)
    if numero_1 < a:   
      print ("¡Demasiado pequeño! ")
    elif numero_1 > a: 
      print(f"¡Demasiado grande! ")
    else:
      numero_1 == a
      print(f"¡Acertó! Le ha costado {contador} intentos")
    contador = contador +1
if contador ==6:
  print (f"perdiste, el numero era {a}")