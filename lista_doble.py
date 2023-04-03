class Persona():
    def __init__(self, id, nombre, edad):
        self.id= id
        self.nombre= nombre
        self.edad= edad
"""Clase del nodo"""
class Nodo():
    def __init__(self, dato=None,siguiente=None, anterior=None):
        self.dato=dato
        self.siguiente=siguiente
        self.anterior=anterior
class ListaDobleEnlazada():
    def __init__(self):
        self.cabeza=None
        self.cola=None
    def insertar(self,dato):
        nodo=Nodo(dato)
        if self.cabeza is None:
            self.cabeza=nodo
            self.cola=self.cabeza
        else:
            nodo.anterior=self.cola
            self.cola.siguiente=nodo
            self.cola=nodo
    def recorrer(self):
        actual=self.cabeza
        while actual:
            dato=actual.dato
            actual=actual.siguiente
            yield dato
"""Creacion de las personas"""
persona1=Persona(1,"Fernando",22)
persona2=Persona(2,"Fer",10)
persona3=Persona(3,"Carlos",30)
persona4=Persona(4,"Pablo",12)
persona5=Persona(5,"Juan",30)
persona6=Persona(6,"Benito",30)
"""insertar las edades a los nodos"""
numero=ListaDobleEnlazada()
numero.insertar(persona1.edad)
numero.insertar(persona2.edad)
numero.insertar(persona3.edad)
numero.insertar(persona4.edad)
numero.insertar(persona5.edad)
numero.insertar(persona6.edad)
print()
"""mostrar los contenidos de los nodos """
for recorrer in numero.recorrer():
    print(recorrer)