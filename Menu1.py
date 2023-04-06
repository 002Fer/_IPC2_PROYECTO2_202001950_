from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from xml.dom import minidom
from lista_simple import listaSimple
from elementos import Elementos
from maquinas import Maquinas
from compuestos import Compuesto
from tkinter.filedialog import askopenfile
import os

class Mi_ventan(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=520,height=370,bg='#04B45F')
        self.master=master
        self.pack()
        self.ventana_principal()
    
    def datos(self):
        ventana2=Toplevel()
        ventana2.title("Datos personales")
        ventana2.geometry("500x250")
        ventana2.config(bg='#04B45F')
        label_curso=Label(ventana2, text='Lab. IPC2')
        label_nombre=Label(ventana2,text="Fernando Misael Morales Ortíz")
        label_carnet=Label(ventana2, text='202001950')
        boton_regresar=Button(ventana2,bg='red', text="Regresar",command=ventana2.destroy)
      
        label_curso.place(x=100,y=20, width=300, height=35)
        label_nombre.place(x=100,y=65, width=300, height=35)
        label_carnet.place(x=100,y=110, width=250, height=35)
        boton_regresar.place (x=100, y=155,width=100,height=30)

    def ventana_principal(self):
        self.boton_abrir=Button(self, text='Cargar Archivo', bg='#BDBDBD', command=self.buscar_archivo)

        a="Generar Salida"     
        self.boton_salida=Button(self, text=a,bg='#BDBDBD' )
        self.boton_elementos=Button(self,text='Gestion de elementos',bg='#BDBDBD', command=self.mostrar_elementos )
        self.boton_compuestos=Button(self,text='Gestion de compuestos',bg='#BDBDBD' )
        self.boton_salir=Button(self,text='Salir',bg='#BDBDBD' , command=self.quit)

        self.boton_maquinas=Button(self, text='Gestion de máquinas',bg='#BDBDBD',command=self.mostrar_maquinas )
        self.boton_ayuda=Button(self,text='Ayuda',bg='#BDBDBD',command=self.datos  )

   
        self.boton_abrir.place(x=50, y=70,width=130, height=30 )
            # self.label_imagen1.place(x=5,y=60,width=30, height=30)
        self.boton_salida.place(x=50,y=110, width=130, height=30)
        self.boton_elementos.place(x=50, y=150, width=130, height=30 )
        self.boton_compuestos.place(x=50, y=190, width=130, height=30)
        self.boton_salir.place(x=50,y=230, width=130, height=30)

        self.boton_maquinas.place(x=310, y=70,width=130, height=30 )
        self.boton_ayuda.place(x=310,y=110, width=130, height=30)

    def buscar_archivo(self):
        ventana=askopenfile(title="seleccione el archivo")
        archXML=minidom.parse(ventana)
        self.porcesoInfo(archXML)

    def porcesoInfo(self,archXML):
        #listado de maquinas
        self.listado_elementos=listaSimple()
        self.listado_maquinas=listaSimple()
        self.listado_compuesto=listaSimple()


        
        #---------///////////-----lsitado de compuestos-----////////////------------
        compuesto=archXML.getElementsByTagName('compuesto')

        for comp in compuesto:
            nom_compuesto= comp.childNodes[1].firstChild.data
            compuesto_1=Compuesto(nom_compuesto)

        el_compuesto=compuesto[0].getElementsByTagName('elementos')
        elememen1=el_compuesto[0].getElementsByTagName('elemento')
        for h in range(len(elememen1)):
            elemen2=elememen1[h].childNodes[0].data
            self.listado_compuesto.insertar(elemen2)

         #----------/////////////////-----------listado de maquinas------///////////-------
        self.maquinasXML=archXML.getElementsByTagName('Maquina')
        for el in self.maquinasXML:
            nom_=el.getElementsByTagName('nombre')[0]
            pines_=el.getElementsByTagName('numeroPines')[0]
            tamaño=el.getElementsByTagName('numeroElementos')[0]

            self.numero2=nom_.firstChild.data
            self.simbolo2=pines_.firstChild.data
            self.nombre2=tamaño.firstChild.data

        pines=archXML.getElementsByTagName('pin')
        

        for j in range(len(pines)):

            elementos=pines[j].getElementsByTagName('elementos')
            elemento1=elementos[0].getElementsByTagName('elemento')

            for i in range(len(elemento1)):
                elemento2=elemento1[i].childNodes[0].data
                self.listado_maquinas.insertar(elemento2)
  

        #-----------///////////------listado de elementos---------//////////------------
        self.elementosXML=archXML.getElementsByTagName('elemento')
       
        for elementos in self.elementosXML:
            numero=elementos.getElementsByTagName('numeroAtomico')[0]
            simbolo=elementos.getElementsByTagName('simbolo')[0]
            nombre=elementos.getElementsByTagName('nombreElemento')[0]

            numero1=numero.firstChild.data
            simbolo1=simbolo.firstChild.data
            nombre1=nombre.firstChild.data
            

            nuevoElemento=Elementos(numero1,simbolo1,nombre1)
            
            self.listado_elementos.insertar(nuevoElemento)


#--------////////////-----ventana para mostrar los elementos //////////////////////----

    def mostrar_elementos(self):
        ventana3=Toplevel()
        ventana3.title("tabla de elementos")
        ventana3.geometry("600x250")
        ventana3.config(bg='#04B45F')

        botonN_elemento=Button(ventana3,text="Agregar elemento",command=self.nuevo_elemento)
        botonN_elemento.place (x=450,y=100,width=100,height=30)
      

        boton_regresar=Button(ventana3,bg='red', text="Regresar",command=ventana3.destroy)
        boton_regresar.place(x=450,y=150,width=100,height=30)
     

        
        tv=ttk.Treeview(ventana3,columns=("col1","col2"))

        tv.column('#0', width=100)
        tv.column('col1', width=100)
        tv.column('col2', width=100)

        tv.heading('#0',text='numero atomico', anchor=CENTER)
        tv.heading('col1',text='SIMBOLO', anchor=CENTER)
        tv.heading('col2',text='NOMBRE', anchor=CENTER)

        while self.elementosXML!=None:
            for elementos in self.elementosXML:
                numero=elementos.getElementsByTagName('numeroAtomico')[0]
                simbolo=elementos.getElementsByTagName('simbolo')[0]
                nombre=elementos.getElementsByTagName('nombreElemento')[0]

                numero1=numero.firstChild.data
                simbolo1=simbolo.firstChild.data
                nombre1=nombre.firstChild.data
                tv.insert("",END,text=numero1,values=(simbolo1,nombre1))
                tv.place(x=10,y=10)



#--------////////////-----ventana para mostrar maquinas //////////////////////----

    def mostrar_maquinas(self):
        ventana4=Toplevel()
        ventana4.title("tabla de elementos")
        ventana4.geometry("500x250")
        ventana4.config(bg='#04B45F')
        
        tv2=ttk.Treeview(ventana4,columns=("col1","col2"))

        tv2.column('#0', width=100)
        tv2.column('col1', width=100)
        tv2.column('col2', width=100)

        tv2.heading('#0',text='Nombre ', anchor=CENTER)
        tv2.heading('col1',text='Numero', anchor=CENTER)
        tv2.heading('col2',text='elementos', anchor=CENTER)


        tv2.insert("",END,text=self.numero2,values=(self.simbolo2,self.nombre2))
        tv2.pack()
    
        #--------////////////-----ventana para insetar nuevo elemento //////////////////////----
    def nuevo_elemento(self):
        ventana_nuevo=Toplevel()
        ventana_nuevo.title("Nuevo elemento")
        ventana_nuevo.geometry("600x250")
        ventana_nuevo.config(bg='#04B45F')
        
        label_numero=Label(ventana_nuevo,text="Numero Atomico")
        label_simbolo=Label(ventana_nuevo,text="Simbolo")
        label_elemento=Label(ventana_nuevo,text="Nombre del elemento")

        self.numero=Entry(ventana_nuevo)
        self.simbolo=Entry(ventana_nuevo)
        self.elemento=Entry(ventana_nuevo)


        boton_regresar=Button(ventana_nuevo,bg='red', text="Regresar",command=ventana_nuevo.destroy)
        boton_guardar=Button(ventana_nuevo,bg='blue', text="Guardar",command=self.recoger_datos)

        label_numero.place (x=100,y=70,width=150,height=30)
        label_simbolo.place (x=100,y=115,width=150,height=30)
        label_elemento.place (x=100,y=160,width=150,height=30)

        self.numero.place (x=300,y=70,width=150,height=30)
        self.simbolo.place (x=300,y=115,width=150,height=30)
        self.elemento.place (x=300,y=160,width=150,height=30)

        boton_regresar.place(x=100,y=200,width=150,height=30)
        boton_guardar.place(x=320,y=200,width=100,height=30)
    
    def recoger_datos(self):
        nuevo_numero=self.numero.get()
        nuevo_simbolo=self.simbolo.get()
        nuevo_elemento=self.elemento.get()
        self.listado_elementos.insertar(nuevo_numero,nuevo_simbolo,nuevo_elemento)

        messagebox.showinfo("Se guardado el nuevo elemento")

        

root=Tk()
app=Mi_ventan(root)
app.mainloop()

