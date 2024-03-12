import tkinter as tk
from PIL import Image, ImageTk
from canvas2 import Pantalla3
from canvas3 import Pantalla4

# PANTALLA DE TARJETA DE LEALTAD 1
class Pantalla2(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
         # imagen fondo
        imagen = Image.open("Diapositiva2.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

        # boton sin tarjeta
        imagen1 = Image.open("Diapositiva9.png")
        imagen1 = imagen1.resize((400, 130)) # Redimensionar la imagen
        self.imagen1 = ImageTk.PhotoImage(imagen1)
        self.button = tk.Button(self, image=self.imagen1, command=self.previoRegistro())
        self.button.place(x=0, y=310, anchor="nw")
        self.button.config(borderwidth="0")

        # boton con tarjeta
        imagen2 = Image.open("Diapositiva10.png")
        imagen2 = imagen2.resize((400, 130)) # Redimensionar la imagen
        self.imagen2 = ImageTk.PhotoImage(imagen2)
        self.button = tk.Button(self, image=self.imagen2, command=self.start_game())
        self.button.place(x=400, y=310, anchor="nw")
        self.button.config(borderwidth="0")

    def start_game(self): # enviar a inicio de juego
        self.destroy()  # Destruye la pantalla actual

        # Crea la pantalla anterior
        pantalla_anterior = Pantalla4(master=self.master)
        pantalla_anterior.mainloop()
    
    def previoRegistro(self): # enviar a inicio de juego
        self.destroy()  # Destruye la pantalla actual
        # Crea la pantalla anterior
        pantalla_anterior = Pantalla3(master=self.master)
        pantalla_anterior.mainloop()