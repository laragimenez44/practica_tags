"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiante: Lara Giménez

Práctico 1: Repaso comandos programación 1 - Programación imperativa Python
"""

# 1 Ejercicio entrada, salida y aritmética:

print ("CALCULO DE LA MEDIA")
entrada_1: str = input ("Escriba el primer numero: ")
numero_1 : int = int (entrada_1)
entrada_2 : str = input ("Escriba el segundo numero: ")
numero_2: int = int (entrada_2)

resultado : float = (numero_1 + numero_2) / 2
print("la media es" ,resultado)

# 2* Ejercicio entrada, salida y aritmética:

from cmath import sqrt

ancho_del_rectangulo: str = input("Escriba la anchura del rectangulo: ")
ancho: int = int (ancho_del_rectangulo)
altura_del_rectangulo: str = input ("escriba la altura del rectangulo: ")
altura : int = int (altura_del_rectangulo) 
if altura > 0 and ancho > 0:
    area = ancho * altura
    print ("el area de un rectangulo es: ", area)
    perimetro = (ancho *2) + (altura *2)
    print ("el perimetro del rectangulo es: ", perimetro)
    diagonal= sqrt ((ancho**2) + (altura**2) )
    print ("la diagonal del rectangulo es: ", diagonal)
else:
    print ("Ingrese un valor mayor que 0")
 
# # ejercicio 3
v = x <= -7 # x tiene que ser mas chico que -7.
v = x > 16  # x tiene que ser mas grande que 16.   
v = x != -33 # x tiene que ser distinto de -33.

# 4 Expresion Lógica o Booleana
"""Reemplace x por un valor que haga v == False, describa como comentario que tiene que pasar para que v sea False"""

v = x <= -7 # x tiene que ser mas grande que _-7 para que te de false.
v = x > 16 # x tiene que menor o igual a 16 para que te de False.
v = x != -33 # x tiene que ser igual a -33 para que de False.

# 5* Expresion Lógica o Booleana
"""asigne a x un valor para hacer v == True"""

x = #Escriba un valor aquí: 1
v = x <= 1 and x != -75 or x == 48
x = #Escriba un valor aquí: 71
x > -71 and x != 7 and x != 75
x = #Escriba un valor aquí: -117
x >= -117 and x <= -45 or x > 19


# 6 Ejercicio if

print ("comprador de numeros") 
entrada1 : str = input ("escriba un numero: ")
numero1 : float = float (entrada1)
entrada2: str = input("escriba otro numero: ")
numero2 : float = float (entrada2) 

if numero1 == numero2:
    print ("los numeros son iguales ")
elif numero1 < numero2:
    print (f"menor {numero1} ; mayor: {numero2}" )
else:
    print (f"menor {numero2} ; mayor: {numero1}" )

# 7* if (2)

print ("COMPARADOR DE AÑOS")
COMPARADOR_DE_AÑOS_ACTUAL: str = input ("¿En qué año estamos?: ")
año_actual : int = int (COMPARADOR_DE_AÑOS_ACTUAL)
COMPARADOR_DE_AÑOS_CUALQUIERA: str = input ("Escriba un año cualquiera:")
año_cualquiera: int = int (COMPARADOR_DE_AÑOS_CUALQUIERA)
if año_actual < año_cualquiera:
    resultado_1= año_cualquiera - año_actual
    print (f"Para llegar al año {año_actual} faltan {resultado_1} años.")
elif  año_actual > año_cualquiera:
    resultado_2= año_actual - año_cualquiera
    print (f"Desde el año {año_cualquiera} han pasado {resultado_2} años. ")
else:
    año_actual == año_cualquiera
    print ("¡Son el mismo año!")


# 8 For 

for i in range (10):
    print ("Tengo que hacer la tarea" )

# 9 For 

Entrada: str = input ("¿Cual tabla quiere repasar?: ") 
tabla_de_multiplicar : int= int (Entrada)
print ("¡Perfecto!")
for i in range (1,11):
    print ((i), "x" ,(tabla_de_multiplicar) , "=" ,(i*tabla_de_multiplicar) )

# 10 For

tabla: str=  input ("ingrese la tabla que quiere repasar: ")
num_tabla: int =int (tabla)
for i in range (1,11):
	resultado= input (f"ingrese el resultado: {i} x {num_tabla} = ")
	numero: int = int (resultado)
	print (f" {i} x {num_tabla} = {numero}")
	if i*num_tabla ==numero:
		print ("bien")
	else:
		i*num_tabla !=numero
		print ("mal")


# 11* For (acumulador)

print ("SUMA DE VALORES")
entrada: str= input ("¿Cuantos valores va a introducir?:  ")
tickets :int = int (entrada)
contador = 0
if tickets < 0:
	print ("¡Imposible!")
else:
    for i in range (tickets):
        monto_gastado: str= input (f"¿Cuanto gasto en con cada tickets {i+1}: ")
        monto: float = float (monto_gastado)
        contador =  contador + monto
    print (contador)
	
# 12 While

entrada_1: str = input("Escriba su contraseña: ")
contraseña: str = str (entrada_1)
intentos: int=3
print ("Tiene 3 intentos para confirmar su contraseña.")
entrada_2: str= input("Escriba de nuevo su contraseña: ")
primer_intento: str = str (entrada_2)
contador= 1
while contraseña != primer_intento and contador < intentos:
    print ("Las contraseñas no coinciden. Inténtelo de nuevo.")
    entrada_3 = input("Escriba de nuevo su contraseña: ")
    segundo_intento : str = str (entrada_3) 
    contador = contador +1
    if contraseña != entrada_3:
      print ("Lo siento, no ha confirmado la contraseña. ¡Hasta la vista!")
    else:
        contraseña == entrada_3
print("Contraseña confirmada. ¡Hasta la vista!")


# 13* While (acumulador) - Ahora sesuelva el ejercicio 11 usando el while

print ("SUMA DE VALORES")
entrada: str= input ("¿Cuantos valores va a introducir?:  ")
tickets :int = int (entrada) 
contador:int = 0
i: int= 0
if tickets < 0:
      print ("¡Imposible!")
else:
    while i < tickets: 
      i= i + 1
      cantidad_de_tickets: str= input (f"Escriba el ticket {i} : ")
      monto : float = float (cantidad_de_tickets)
      contador= contador + monto 
print (f"La suma de los números que ha escrito es {contador}")

# 14 While

import random
numero_alazar: int = random.randint(1,100)
print ("Intente adivinar un número entero entre 0 y 100.")
contador: int = 0
numero_1 = -1
while numero_1 != numero_alazar and contador < 6:
    adivinar= input ("Escriba un número: ")
    numero: int = int (adivinar)
    if numero < numero_alazar:   
      print ("¡Demasiado pequeño! ")
    elif numero > numero_alazar: 
      print(f"¡Demasiado grande! ")
    else:
      numero == numero_alazar
      print(f"¡Acertó! Le ha costado {contador} intentos")
    contador = contador +1
if contador ==6:
  print (f"perdiste, el numero era {numero_alazar}")