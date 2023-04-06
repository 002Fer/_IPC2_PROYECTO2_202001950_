from tkinter import *
from xml.dom import minidom
from lista_simple import listaSimple
from elementos import Elementos
from maquinas import Maquinas
from compuestos import Compuesto
from tkinter.filedialog import askopenfilename
import os

class menu:

    def __init__(self) -> None:

        self.mostrarMenu()
    def mostrarMenu(self):
        opcion =''
        while opcion != '6':
            print("-------------Menu-------------")
            print("1. Abrir archivo")
            print("2. Mostrar grafica")
            print("3. Ingresar Celula")
            print("4. Celdas para sobrevivir")
            print("5. Crear XML")
            print("6. Salir")
            opcion=input("Ingrese una de las opciones: ")
            
            if opcion== '1':
                archivo=askopenfilename(title="Abrir un archivo")
                archXML=minidom.parse(archivo)
                self.porcesoInfo(archXML)


                print("Se cargo el archivo")
                 
                    
            elif opcion=='2':
                self.Grafica()

            elif opcion=='3':
                self.insertarNueva()
                self.Grafica()


            elif opcion=='4':
                self.analizarcelulas()
 

    def porcesoInfo(self,archXML):
        #listado de maquinas
        self.listado_elementos=listaSimple()
        self.listado_maquinas=listaSimple()
        self.listado_compuesto=listaSimple()


        
                #lsitado de compuestos
        compuesto=archXML.getElementsByTagName('compuesto')

        for comp in compuesto:
            nom_compuesto= comp.childNodes[1].firstChild.data
            compuesto_1=Compuesto(nom_compuesto)

        el_compuesto=compuesto[0].getElementsByTagName('elementos')
        elememen1=el_compuesto[0].getElementsByTagName('elemento')
        for h in range(len(elememen1)):
            elemen2=elememen1[h].childNodes[0].data

        pines=archXML.getElementsByTagName('pin')
        

        for j in range(len(pines)):

            elementos=pines[j].getElementsByTagName('elementos')
            elemento1=elementos[0].getElementsByTagName('elemento')

            for i in range(len(elemento1)):
                elemento2=elemento1[i].childNodes[0].data
                
  

        #listado de elementos
        elementosXML=archXML.getElementsByTagName('elemento')
       
        for elementos in elementosXML:
            numero=elementos.getElementsByTagName('numeroAtomico')[0]
            simbolo=elementos.getElementsByTagName('simbolo')[0]
            nombre=elementos.getElementsByTagName('nombreElemento')[0]

            numero1=numero.firstChild.data
            simbolo1=simbolo.firstChild.data
            nombre1=nombre.firstChild.data
            

            nuevoElemento=Elementos(numero1,simbolo1,nombre1)
       


   

cargarmenu=menu()
cargarmenu.mostrarMenu()

