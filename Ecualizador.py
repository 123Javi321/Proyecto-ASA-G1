#Grupo 1
#Analisis de señales Aleatorias
from tkinter import *

class ObjetoEcualizador:

    #Constructor
    def __init__(self, main) -> None:
        self.Menu(main)
        root.geometry("500x250")
        root.configure(bg='dark green')

    #Menu principal
    def Menu(self, objetoecualizador):
        self.titulo = Label(text="Proyecto - Analisis de Senales Aleatorias", font=('Courier New', 14), fg="black").pack(pady = "20")
        self.btn1 = Button(objetoecualizador, text='Inicio', command=self.Importar).pack()
        self.btn2 = Button(objetoecualizador, text='Creditos', command=self.Creditos).pack()
        self.btn3 = Button(objetoecualizador, text='Salir', command=root.destroy).pack()
        #self.entr = Entry(objetoecualizador, textvariable=self.parametro1).pack()
        #self.btn = Button(objetoecualizador, text='Mandarparametro', command=self.Imprimir).pack()
        #self.btn2 = Button(objetoecualizador, text='Crear ventana2', command=self.Ventana2).pack()
        
    #Imprime la variable parametro desde la ventana principal
    def Imprimir(self):
        duracion=self.duracion1.get()
        print(duracion)

    #Crear otra ventana
    """def Ventana2(self):
        #Imprime la variable parametro1 desde otra ventana
        def Imprimir2():
            print(self.parametro1.get())
        root.withdraw()
        win=Toplevel()
        win.geometry("500x250")
        win.configure(background='dark turquoise')
        #Imprime info del objeto desde otra ventana
        self.btn = Button(win, text='ImprimirParametro', command=Imprimir2).pack()"""

    #Ventana de creditos
    def Creditos(self):
        win2=Toplevel()
        win2.geometry("500x250")
        self.grupo = Label(win2, text="GRUPO #1", fg="white", bg="black", font=('Courier New', 14)).place(x=200, y=15)
        self.int1 = Label(win2, text="Javier Castañeda - 1290520", fg="white", bg="black", font=('Courier New', 14)).place(x=110, y=60)
        self.int2 = Label(win2, text="Leonardo Castillo - 1172920 ", fg="white", bg="black", font=('Courier New', 14)).place(x=110, y=90)
        self.int3 = Label(win2, text="Andres Coronado - 1168420 ", fg="white", bg="black", font=('Courier New', 14)).place(x=110, y=120)
        self.int4 = Label(win2, text="Pablo Flores - 1164720", fg="white", bg="black", font=('Courier New', 14)).place(x=110, y=150)
        self.volver = Button(win2, text="Volver", command=win2.destroy, width=12, fg="white", bg="black", font=('Courier New', 14)).place(x=170, y=200)

    #Ventana para importar el audio
    def Importar(self):
        self.duracion1 = Variable()
        win3=Toplevel()
        win3.geometry("500x250")
        self.titulo = Label(win3, text="Importar el audio", fg="white", bg="black", font=('Courier New', 14)).pack()
        self.btnimportar = Button(win3, text="Importar audio").pack()
        self.titulo2 = Label(win3, text="Establecer duracion del audio", fg="white", bg="black", font=('Courier New', 14)).pack()
        self.entr = Entry(win3, textvariable=self.duracion1).pack()
        #def Imprimir2():
        #    print(self.duracion1.get())
        self.btncont = Button(win3, text="Continuar", command=self.opcion).pack()

    #Ventana para elegir la opcion de ecualizacion
    def opcion(self):
        win4=Toplevel()
        win4.geometry("500x250")
        self.titulo = Label(win4, text="Selecciona la opcion para ecualizar", fg="white", bg="black", font=('Courier New', 14)).pack()
        self.btnopt1 = Button(win4, text="Opcion 1").pack()
        self.btnopt2 = Button(win4, text="Opcion 2").pack()

    #Ventana de opcion 1
    

root=Tk()
Ecualizador=ObjetoEcualizador(root)
root.mainloop()
