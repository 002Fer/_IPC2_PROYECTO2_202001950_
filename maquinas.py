from lista_simple import listaSimple

class Maquinas:
    listaPines:listaSimple

    def __init__(self,nombre,num_pines,num_elementos) -> None:
        self.nombre=nombre
        self.num_pines=num_pines
        self.num_elementos=num_elementos
        self.listaPines=listaSimple()