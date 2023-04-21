"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiante:

Práctico 2: Tipos abstractos de datos
"""
"""
1.a*  Implementar una clase llamada AlumnoMateria con las partes Constructor, operaciones y condiciones.
Constructor: nombre, nota, materia
Operaciones: imprimir datos y mostrar_estado() {libre, regular, promocional}
Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero (entre 0 y 10)
"""

class AlumnoMateria:
    def __init__(self, nombre, materia, nota): # Agregar parámetros
        """funcion que inicializa una variable AlumnoMateria
        tener en cuenta las condiciones del TAD (texto e int)
        """
        assert type(nombre) == str, "Esto no es un string"
        assert type(materia) == str, "Esto no es un string"
        assert type(nota) == int, f"Esto no es un entero es {type(nota)}"
        assert nota >= 0 and nota <= 10, "nota no esta entre 0 y 10"
        
        self.nombre = nombre
        self.nota = nota
        self.materia = materia
    def __str__(self)->str:
        return f"{self.nombre}, {self.materia}, {self.nota}"
    def mostrar_estado(self)->str: 
        """calcula si esta regular, promocionado, o libre"""
        nota = self.nota
        if nota<4:
            estado = "libre"
        elif nota >= 4 and nota < 7:
            estado = "regular"
        else:
            estado = "promocionado"
        return estado

# Test
alumno1 = AlumnoMateria ("Juan", "Matemáticas", 4)
assert alumno1.__str__() == "Juan, Matemáticas, 4"
assert alumno1.mostrar_estado() == "regular"

"""
1.b Implementar la clase registroAlumnoMateria() que guarde varias notas y diga si el alumno está regular, promocional o libre. Con las siguientes reglas.
    Constructor: (Nombre, Materia)
    Agregar nota: Agrega una nota al alumno en la materia (lista de notas)
    Promedio: Devuelve el promedio de notas que tiene el alumno
    Mostrar notas: imprime la lsita de notas
    Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero (entre 0 y 10)
"""
class RegistroAlumnoMateria:
    notas = []
    def __init__(self, nombre, materia): # Agregar parámetros
        """funcion que inicializa una variable registroAlumnoMateria"""
        pass
    def __str__(self):
        pass
    def agregar_nota(self):
        pass
    def mostrar_notas(self):
        pass
    def calcular_promedio(self)->float:
        pass
    def mostrar_estado(sef)->str: 
        """calcula si esta regular, promocionado, o libre
        si saca menos de 4 de promedio , queda libre
        Promocion promedio de 7 y todas las notas 6 o mas.
        Sino Regular
        """
        pass


a = RegistroAlumnoMateria ("Nombre", "Materia")
a.agregar_nota(4)
b.agragar_nota(10)
assert alumno1.mostrar_estado() == "promocionado"
assert alumno1.__str__() == "Juan, Matemáticas, promocionado"

"""
2.a* A la clase punto vista en la materia agregarle el método Distancia al origen ()siendo el origen el punto (0,0). Crear un programa que use este método para imprimir en pantalla la distancia entre al origen de los puntos A, B y C.
"""
A = Punto(2,3)
B = Punto(5,5)
C = Punto(1,5)

A.distancia(B)
assert A.distancia_origen() == 3.605551275463989
assert B.distancia_origen() == 7.0710678118654755
assert C.distancia_origen() == 5.0990195135927845

"""
2.b Utilizando el método de distancia al origen cree una función que tome una lista de puntos y devuelva el que se encuentra más alejado del origen.
def mas_lejos(lista:[Punto])->Punto
toma una lista de puntos y devuelve el mas alejado del origen
"""
assert mas_lejos([Punto(2,3) , Punto( 5,5 ), Punto(1,5)]) == Punto(5,5)

"""
3.* Crear una clase circulo: 
constructor: punto(x, y), radio; 
operaciones:diametro,  perimetro y area.
"""
#Tomar de ejemplo la clase rectangulo
class Circulo:
    def __init__( self ): # toma un radio , centro
        pass
    def diametro ( self ):
        pass
    def perimetro ( self ):
        pass 
    def area ( self ):
        pass
    def __eq__(self,otro):
        pass
    def mover(self):
        pass
c = Circulo(0, 0, 4.5)
assert c.diametro() == 9.0
assert c.area_circulo() == 63.61725123519331
assert c.perimetro_circulo() == 28.274333882308138

"""
4. Definir el TAD Fracción junto con su implementación en Clases.
    En python tenemos el tipo de dato float, pero no fraccion (numeros racionales)
    Constructor: arriba, abajo
    Operaciones: mostrar: convertir el objeto en cadena para poder imprimirlo = ⅓.
    Sumar (o restar) fracciones: suma de dos fracciones (tener en cuenta el denominador común)
    Igualdad: ¿Cuando dos fracciones son equivalentes?

Escribir test para los métodos de la clase
"""
class Fraccion:
    def __init__(self,arriba,abajo):
        """inicializa una variable del tipo fraccion"""
        self.num = arriba # Numerador
        self.den = abajo # Denominador
    def __str__(self):
        """Convertir el objeto en cadena para poder imprimirlo"""
        pass
    def __add__(self, otraFrac):
        """Sumar dos fracciones y retornar resultado, pueden tener distinto denominador"""
        pass
    def __eq__(self, otraFrac):
        """compara dos fracciones y dice si son equivalentes"""
        pass

q = Fraccion(2,4)
p = Fraccion(1,2)

assert q == p

"""
5.* Desarrolla una clase Cafetera con 
Atributos:
	+ _capacidadMaxima (la cantidad máxima de café que puede contener la cafetera) y 
	+ _cantidadActual (la cantidad actual de café que hay en la cafetera). 
Métodos:
	+ Constructor predeterminado: establece la capacidad máxima en 1000 (c.c.) y la actual en cero (cafetera vacía).
	+ Constructor con la capacidad máxima de la cafetera; inicializa la cantidad actual de café igual a la capacidad máxima.
	+ Constructor con la capacidad máxima y la cantidad actual. Si la cantidad actual es mayor que la capacidad máxima de la cafetera, la ajustará al máximo.
	+ llenarCafetera(): pues eso, hace que la cantidad actual sea igual a la capacidad.
	+ servirTaza(int): simula la acción de servir una taza con la capacidad indicada.
	+ vaciarCafetera(): pone la cantidad de café actual en cero.
	+ agregarCafe(int): añade a la cafetera la cantidad de café indicada.
Condiciones:
	+ Si la cantidad actual de café “no alcanza” para llenar la taza, se sirve lo que quede.
	+ despues e servir una taza se deberia descontar del contenido de la cafetera lo que se sirvió
	+ las cafeteras no deberian tener nunca cantidades negativas de cafe
	+ la cantidad actual nunca deberia ser mayor a la capacidad maxima de la cafetera

Escriba test usando assert para todos los métodos y las condiciones
"""
