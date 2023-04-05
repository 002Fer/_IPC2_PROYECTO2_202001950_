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

'''
        nom=archXML.getElementsByTagName('nombre')
        pines=archXML.getElementsByTagName('numeroPines')
        elemen=archXML.getElementsByTagName('numeroElementos')

        nom_maquina= nom[0].childNodes[0].data
        num_pines= pines[0].childNodes[0].data
        num_elementos=elemen[0].childNodes[0].data

        self.nuevaMaquina = Maquinas(nom_maquina,num_pines,num_elementos)

        pin_maquina=archXML.getElementsByTagName('pin')
        for pi in pin_maquina:
            

 

        #listado de elementos
        elementosXML=archXML.getElementsByTagName('elemento')
       
        for elementos in elementosXML:
            numero=elementos.childNodes[1].firstChild.data
            simbolo=elementos.childNodes[3].firstChild.data
            nombre=elementos.childNodes[5].firstChild.data
            

            nuevoElemento=Elementos(numero,simbolo,nombre)
            
            self.listado_elementos.insertar(nuevoElemento)
            

        #lsitado de compuestos
        compuesto=archXML.getElementsByTagName('nombre')
        nom_compuesto= compuesto[0].childNodes[0].data

        nuevo_compuesto=Compuesto(nom_compuesto)
'''