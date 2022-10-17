#Grupo 1
#Analisis de señales Aleatorias
from tkinter import *

class ObjetoEcualizador:
    #Constructor
    def __init__(self, main) -> None:
        self.Menu(main)
        root.geometry("500x250")
        root.configure(bg='dark green')

    def Menu(self, objetoecualizador):
        self.parametro1 = Variable()
        self.titulo = Label(text="Proyecto - Analisis de Senales Aleatorias", font=('Courier New', 14), fg="black").pack()
        self.btn1 = Button(objetoecualizador, text='Inicio', command=self.Ventana2).pack()
        self.btn2 = Button(objetoecualizador, text='Creditos', command=self.Creditos).pack()
        self.btn3 = Button(objetoecualizador, text='Salir', command=root.destroy).pack()
        self.entr = Entry(objetoecualizador, textvariable=self.parametro1).pack()
        self.btn = Button(objetoecualizador, text='Mandarparametro', command=self.Imprimir).pack()
        self.btn2 = Button(objetoecualizador, text='Crear ventana2', command=self.Ventana2).pack()
        
    #Imprime la variable parametro desde la ventana principal
    def Imprimir(self):
        parametro=self.parametro1.get()
        print(parametro)

    #Crear otra ventana
    def Ventana2(self):
        #Imprime la variable parametro1 desde otra ventana
        def Imprimir2():
            print(self.parametro1.get())
        root.withdraw()
        win=Toplevel()
        win.geometry("500x250")
        win.configure(background='dark turquoise')
        #Imprime info del objeto desde otra ventana
        self.btn = Button(win, text='ImprimirParametro', command=Imprimir2).pack()
    def Creditos(self):
        #Mostrar creditos
        print()
root=Tk()
Ecualizador=ObjetoEcualizador(root)
root.mainloop()
