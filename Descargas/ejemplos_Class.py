"""""
class   Persona():
    def __init__(self, nombre,apellido,telefono, direccion, anio):
        self.nombre = nombre
        self.apellido =apellido
        self.telefono = telefono
        self.direccion= direccion
        self.año = año
    def edad (self) -> int:
        return 2023 - self.año
    def es_millenial(self)->bool:
        anioss= [1983,1984,1985,1986,1987,1988,1989.1989,1990,1991.1992,1993]
        for elemento in anio:
            if self.año in anio:
                return True
            else:
                return False 
    
persona_1= Persona ("Martin", "Garay", 342, "av. maipu", 1999 )
print (persona_1.nombre)
print (persona_1.edad())
print (persona_1.apellido)
print (persona_1.es_millenial())

#contador= 0
#contador = contador + 1
#while alumnos == 3 and contador < 3

alumnos= {}

#def notas (alumnos: dict, nombre: str, apellido: str, nota: int)->None:
#    alumnos [alumnos] = {"nombre": nombre, "apellido": apellido, "nota" : nota}

def nota_mayor (alumnos:dict, nota:int) -> None:
    mayor = max (alumnos[nota])
    return (mayor)

def imprimir_nombre_nota_alumno(alumnos:dict) -> None:
    for nombre in alumnos:
        print(nombre, ":", alumnos [nombre])

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
Alumnos= {}
valor= 3
contador= 0 
while contador <= 3 and valor < 3:
    nombre: str = str (input("Ingrese el nombre: " ))
    apellido: str = str (input("Ingrese el apellido: " ))
    nota: float = str (input("Ingrese la nota: " ))
    contador = contador + 1
    lista= [nota]
    mayor= max (lista)
    print (f"el alumno con mejor nota fue {nombre} y saco {mayor}")



