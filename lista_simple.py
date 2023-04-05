class Nodo:

    def __init__(self, datos):
        self.datos=datos
        self.siguiente=None
        

class listaSimple:
    def __init__(self):
        self.cabeza=None
        self.tamaño=0
         

    def insertar(self,datos):
        nuevoNodo=Nodo(datos)
        if self.tamaño == 0:
            self.cabeza = nuevoNodo

        else:
            auxiliar=self.cabeza
            while auxiliar.siguiente !=None:
                auxiliar=auxiliar.siguiente
            auxiliar.siguiente=nuevoNodo 
        self.tamaño += 1

    def buscar(self,nombre_cel):
        aux=self.cabeza
        while aux !=None:
            if aux.nombre_cel == nombre_cel:
                print("")
            aux=aux.siguiente
'''
        nom=archXML.getElementsByTagName('nombre')
        pines=archXML.getElementsByTagName('numeroPines')
        elemen=archXML.getElementsByTagName('numeroElementos')

        nom_maquina= nom[0].childNodes[0].data
        num_pines= pines[0].childNodes[0].data
        num_elementos=elemen[0].childNodes[0].data

        nuevaMaquina = Maquinas(nom_maquina,num_pines,num_elementos)

        pin_maquina=archXML.getElementsByTagName('pin')

        for pines in pin_maquina:

            elemento_pin=pines.getElementsByTagName('elemento')[0]
            elemento_pin1=elemento_pin.firstChild.data

            nuevaMaquina.listaPines.insertar(elemento_pin1)


        
'''