"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiantes:Lara Anahí Giménez 

Práctico 3: funciones, Listas y cadenas de caracteres
"""

#   contador= 2 false #comparar vocales == c
# 1 Escribir una función sum() que sume todos los números de una lista. 
    
from typing import List


def sum(lista:[int])->int:
    sumatoria= 1
    for elemento in  lista:
        sumatoria = sumatoria* elemento
    return sumatoria 

assert sum ([1,2,3,4]) == 10
assert sum ([1,2,3,4]) != 30
assert sum([7,5]) != 50
assert sum([7,5]) == 12


#* 2 Escribir una función mul() que multiplique todos los números de una lista.
def mul(lista:[int])->int:
    multiplicar = 1
    for elemento in  lista:
        multiplicar = multiplicar * elemento
    return multiplicar 

assert mul([1,2,3,4]) == 24
assert mul([2,8,10]) == 160
assert mul([0,0,0,0])== 0

# 3 Definir una función longitud() que calcule la longitud de una lista o una cadena dada. (Python tiene la función len()
#  incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio).
def longitud(lista:list)->int: #funcion de la lista
    contador= 0
    for elemento in lista:
        contador= contador +1
    return contador
assert longitud([1,2,3,4]) == 4
assert longitud([]) == 0
assert longitud([1,2,3,5]) == 4
assert longitud([59,-2,3,10]) == 4

#* 4 Sin usar la funcion de lista count implementar la funcion que cuenta la cantidad de veces que aparece une elemento en una lista.

elem= 0
def contar(l:list,a:elem)->int:
    sumar = 0  
    for elem in l: 
        if elem == a: # compara el elemento dentro de la lista
            sumar =sumar + 1
    return sumar  
        
assert contar([1,2,3,4],3) == 1
assert contar([1,2,3,4],3) != 2
assert contar([1,2,3,4,4],4) == 2
assert contar([10,10,10,4],10) == 3
assert contar([1,2,0,4,2,7],0) == 1

# 5 Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False
#  de lo contrario. Escribir la función usando el bucle for anidado.

from ast import List

def superposicion(a:List,b:List)->bool:
    resultado= False
    for elemento in a :
        for i in b:
            if elemento ==  i :
                resultado= elemento == i or resultado
                resultado=True
                return resultado 
            else:
                a!= b
                return False
    return True

assert superposicion([2,1,3],[2,4,8]) == True #(2 se esta en las 2 listas)
assert superposicion([1,3,5],[2,4,6]) == False #(no hay elementos comunes)
assert superposicion([9,10,5],[0,4,6]) == False #(no hay elementos comunes)

#* 6 Escriba un programa que permita crear una lista de numeros y que, a continuación, elimine los elementos repetidos (dejando 
# únicamente el primero de los elementos repetidos).

def remover_dup(l:list)->list:
    lista= []
    for elemento in l:
        if elemento not in lista:
            lista.append (elemento)
    return lista

assert remover_dup([1,5,6,7,2,3,4,1,2,5]) == [1, 5, 6, 7, 2, 3, 4]
assert remover_dup([1,6,8,7,2,8,4,1,6,5]) == [1, 6, 8, 7, 2, 4, 5]
assert remover_dup([1,0,6,7,10,3,3,10,0,5]) == [1, 0, 6, 7, 10, 3, 5]

# 7 Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def es_vocal (c:str) -> bool:   """compara si c es vocal"""
c= 0
vocales= ["a,e,i,o,u", ["A,E,I,O,U"]]
resultado= False
for elementos in vocales:
    if (elementos ==vocales):
        resultado= c == elementos or resultado
        resultado=True
    return resultado

assert es_vocal ("f") == False
assert es_vocal ("a") == True
assert es_vocal ("ala") == False
assert es_vocal ("aa") == False
assert es_vocal ("e") == True
assert es_vocal ("6") == False

# 8 Escriba un programa que pida una frase y una vocal y cambie todas las vocales de la frase por la vocal (una forma de hacerlo 
# es convertir la frase en una lista y hacer el cambio en la lista.

def reemplazar_vocal(frase:str,vocal:str)->str: 
    lista=  []
    for letra in frase:
        lista.append (letra)
    for i in range (len(lista)): #para ide 0 a la cantidad de elementos de la lista
        if lista[i] in ["a","e","i","o","u"]: #si elemento i esta en la lista las vocales
            lista[i]= vocal #remplazo por la vocal que ingrese
    frase_final= ""
    for letra in lista:
        frase_final= frase_final+ letra
    return frase_final
          
assert reemplazar_vocal ("Cumpleaños feliz",'a') == "Camplaañas falaz"
assert reemplazar_vocal("tengo hambre",'i') == "tingi himbri"  

#* 9 Hacer una función que intercambie los caracteres indice i,j de un string, si los inices son mayores al largo del string no
#  deberia hacer nada
def intercambiar_dos(palabra:str,l:int,j:int)->str:
    lista=  []
    vacio= 0
    for letra in palabra:  #recorro la frase
        lista.append (letra)  #agrego la letra en mu nueva lista
    for i in range (len(lista)):
        index_1= palabra [l]
        index_2= palabra [j]
        if index_1 < len(palabra) and index_2 < len(palabra) :
            vacio = lista [index_1]
            lista [index_1] = index_2
            lista [index_2]= vacio
        else:
            respuests= palabra
    frase_final= ""
    for letra in lista:
        frase_final= frase_final + letra
    return frase_final
    
assert intercambiar_dos("hola mundo",0,5) == "mola hundo"
assert intercambiar_dos("hola mundo",0,20) == "hola mundo"
assert intercambiar_dos("casa rosa",0,5) == "rasa cosa"
assert intercambiar_dos("estudiar mucho",0,20) == "estudiar mucho"

# 10 hacer una función que cuentes las palabras que tiene una oración

def contar_palabras(frase:str)->int:
	pass

assert contar_palabras("Mi mama me mima") == 4

def contar_palabras(frase:str)->int:
    contador= 0
    for elemento in frase:
        contador= contador +1
    return contador

#assert contar_palabras("Mi mama me mima") == 4
#assert contar_palabras("tengo mucha hambre") == 4
#assert contar_palabras("hola") == 1
assert contar_palabras("") == 0

# 11 Hacer una función que de vuelta las palabras sin usar la función reverse.

def dar_vuelta(s:str)-> str:
    palabra:str = s
    return (palabra[len(palabra)::-1])

assert dar_vuelta("hola") == "aloh" 
assert dar_vuelta ("zapallo") == "ollapaz"
assert dar_vuelta ("zapato") == "otapaz"
assert dar_vuelta ("ojota") == "atojo"

#* 12 Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas
#  invertidas)
def es_palindromo (frase:str) -> bool:
    frase= frase.lower()
    frase= frase.replace (" ", "")
    primer_index= 0
    ultimo_idex= len(frase) -1
    for i in range (0,len(frase)):
        if frase [primer_index] == frase [ultimo_idex]:
            primer_index= primer_index + 1
            ultimo_idex=ultimo_idex- 1
        else:
            return False
            
    return True			

assert es_palindromo ("oso") == True
assert es_palindromo ("osos")== False
assert es_palindromo ("radar") == True
assert es_palindromo ("rada") == False
assert es_palindromo ("oso") == True
assert es_palindromo ("casa") == False
