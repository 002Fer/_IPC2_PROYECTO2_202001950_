from tkinter import *
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
      #  self.imagen1=PhotoImage(self,file="carpeta.jpg")
      #  self.label_imagen1= Label(self,image=self.imagen1)
        self.boton_salida=Button(self, text='Generar Salida',bg='#BDBDBD' )
        self.boton_elementos=Button(self,text='Gestion de elementos',bg='#BDBDBD' )
        self.boton_compuestos=Button(self,text='Gestion de compuestos',bg='#BDBDBD' )
        self.boton_salir=Button(self,text='Salir',bg='#BDBDBD' , command=self.quit)



        self.boton_maquinas=Button(self, text='Gestion de máquinas',bg='#BDBDBD' )
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
      self.ventana=askopenfile(title="seleccione el archivo")
      print("se cargo el archivo")
      

      
      

    
    

root=Tk()
app=Mi_ventan(root)
app.mainloop()
