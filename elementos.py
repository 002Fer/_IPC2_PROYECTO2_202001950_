from lista_simple import listaSimple
class Elementos:
    listaElementos:listaSimple

    def __init__(self, numAtomico, simbolo,nombre) -> None:
        self.numAtomico=numAtomico
        self.simbolo=simbolo
        self.nombre=nombre
        self.listaElementos=listaSimple()
    