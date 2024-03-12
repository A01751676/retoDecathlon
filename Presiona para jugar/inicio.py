import tkinter as tk
from PIL import Image, ImageTk
from canvas1 import *

# PANTALLA DE INICIO
class Pantalla1(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # Cargar la imagen
        imagen = Image.open("Diapositiva1.png")
        imagen = imagen.resize((800, 440))  # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.button = tk.Button(self, image=self.imagen, command=self.next_screen)
        self.button.config(borderwidth="0")
        self.button.pack()

    def next_screen(self): # to tarjeta de lealtad 1
        self.destroy()  # Destruye la pantalla actual

        # Crea la siguiente pantalla
        pantalla_siguiente = Pantalla2(master=self.master )
        pantalla_siguiente.mainloop()