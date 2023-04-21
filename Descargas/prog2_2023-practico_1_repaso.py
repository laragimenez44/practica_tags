"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiante: (Lara Gimenez)

Práctico 1: Repaso comandos programación 1 - Programación imperativa Python
Los ejercicios marcados con un * (asterisco) son obligatorios
"""

# 1 Ejercicio entrada, salida y aritmética:
""" Escriba un programa que pida dos números y que escriba su media aritmética.
Se recuerda que la media aritmética de dos números es la suma de ambos números dividida por 2

CÁLCULO DE LA MEDIA
Escriba el primer numero: 10
Escriba el segundo numero: 5
La media es: 7.5
"""
print("calcula la media")
entrada_1 : str = str (input("Escriba el primer numero: "))
nro_1: int = int(entrada_1)
entrada_2 : str = str (input("Escriba el segundo numero: "))
nro_2: int = int(entrada_2)
resultado= (nro_1 + nro_2) / 2
print ("La media es: ", resultado)

# 2* if (2)
""" Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 2024
Para llegar al año 2020 faltan 5 años.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 1997
Desde el año 1997 han pasado 22 años.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 2019
¡Son el mismo año!
"""

print ("COMPARADOR DE AÑOS")
año_actual = int(input('¿en que año estamos?: '))
año_cualquiera = int (input('escriba un año cualquiera:  '))
if año_actual < año_cualquiera:
	resultado= año_cualquiera - año_actual
	print (f"para llegar al año {año_cualquiera} faltan {resultado} años.")
elif año_actual > año_cualquiera:
	resultado= año_actual - año_cualquiera 
	print (f"Desde el año {año_actual} han pasado {resultado} años")
else:
	if año_actual == año_cualquiera:
		print ("Son el mismo año")

# 3 For (acumulador)
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

print ("SUMA DE VALORES")
entrada: str=str (input("¿Cuántos valores va a introducir? "))
tickets: int = int (entrada)
contador= 0
if tickets <= 0:
    print("¡Imposible!")
else:
    for numero in range (tickets):
        monto: str = str (input(f"Escriba el ticket {numero}: "))
        monto_actual: float = float (monto)
        contador=  monto_actual + contador
    print (f"La suma de los números que ha escrito es: {contador}")

# 4* While (acumulador) - Ahora sesuelva el ejercicio 11 usando el while
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

print ("SUMA DE VALORES")
entrada: str=str (input("¿Cuántos valores va a introducir? "))
tickets: int = int (entrada)
contador= 0
numero= 0
if tickets <= 0:
    print("¡Imposible!")
else:
    while numero < tickets:
    #for numero in range (tickets):
        monto: str = str (input(f"Escriba el ticket {numero}: "))
        numero = numero + 1
        monto_actual: float = float (monto)
        contador=  monto_actual + contador
    print (f"La suma de los números que ha escrito es: {contador}")

# 5 Sin usar la funcion de lista count implementar la funcion que cuenta la cantidad de veces que aparece une elemento en una 
# lista.
def contar(l:list,a:elem)->int:
    pass
assert contar([1,2,3,4],3) == 1
assert contar([1,2,3,4],3) != 2
assert contar([1,2,3,4,4],4) == 2

elem=0
def contar(l:list,a:elem)->int:
    contador= 0
    for elem in l:
        if elem == a:
            contador= contador + 1
    return contador 
assert contar([1,2,3,4],3) == 1
assert contar([1,2,3,4],3) != 2
assert contar([1,2,3,4,4],4) == 2
assert contar([0,7,3,5,9],9) != False
assert contar([1,2,3,4,4],9) == 0

# 6* Definir una función que tome una lista y devuelva el mayor y el menor en una tupla
def max_min(l:list)->tuple:
    respuesta = []
    for numero in l:
        mayor= max (l)
        respuesta.append(mayor)
        menor = min (l)
        respuesta.append(menor)
        tupla=(mayor,menor)
    return tupla 

assert max_min([3,-1,6,22]) == (22,-1)
assert max_min([3,6,22]) == (22,3)
assert max_min([22,67,100]) == (100,22)

# 7 Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas 
# invertidas)
def es_palindromo(s:str)->bool:
    pass
assert es_palindromo ("radar") == True
assert es_palindromo ("rada") == False

# 8* diccionarios
"""
Escriba un programa que tome las notas de programacion 2 de 3 alumnos, los guarde en un diccionario y luego devuelva el nombre del 
alumno con mejor nota.

Ejemplo
Ingrese alumno 1: Juan
Ingrese nota de alumno 1: 8
Ingrese alumno 2: Yessi
Ingrese nota de alumno 2: 9
Ingrese alumno 3: Romi
Ingrese nota de alumno 3: 5
El alumno con mejor nota fue Yessi y saco 9
"""
