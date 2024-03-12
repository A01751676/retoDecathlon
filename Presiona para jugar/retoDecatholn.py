import tkinter as tk
from PIL import Image, ImageTk
import pygame
import cv2

def midSize(file,fileout):
    img = cv2.imread(file) 
    crop = img[0:310,0:800] 
    cv2.imwrite(fileout, crop) 

def littleLeftSize(file,fileout):
    img = cv2.imread(file) 
    crop = img[311:440,0:400] 
    cv2.imwrite(fileout, crop) 

def littleRightSize(file,fileout):
    img = cv2.imread(file) 
    crop = img[311:440,401:800] 
    cv2.imwrite(fileout, crop) 

def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=-1)

# PANTALLA DE INICIO ----------------------------------------------------------------------------------------
class Default(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        global tlealtad
        tlealtad = 0
        global game_tries
        game_tries = 0
        print("tiene tarjeta: " +str(tlealtad))
        
        self.create_widgets()
        play_music("tema.mp3")

    def create_widgets(self):

        # Cargar la imagen
        imagen = Image.open("default.png")
        imagen = imagen.resize((800, 440))  # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.button = tk.Button(self, image=self.imagen, command=self.next_screen)
        self.button.config(borderwidth="0")
        self.button.pack()

    def next_screen(self): # to tarjeta de lealtad 1
        self.destroy()  # Destruye la pantalla actual
        #pygame.mixer.music.stop()
        # Crea la siguiente pantalla
        pantalla_siguiente = TarjetaLealtadInicio(master=root)
        pantalla_siguiente.mainloop()

# PANTALLA DE TARJETA DE LEALTAD 1 --------------------------------------------------------------------------
class TarjetaLealtadInicio(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
         # imagen fondo
        imagen = Image.open("clubDecathlon.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

        # boton sin tarjeta
        imagen1 = Image.open("clubDecathlonLeft.png")
        imagen1 = imagen1.resize((400, 130)) # Redimensionar la imagen
        self.imagen1 = ImageTk.PhotoImage(imagen1)
        self.button = tk.Button(self, image=self.imagen1, command=self.registro1)
        self.button.place(x=0, y=310, anchor="nw")
        self.button.config(borderwidth="0")

        # boton con tarjeta
        imagen2 = Image.open("clubDecathlonRight.png")
        imagen2 = imagen2.resize((400, 130)) # Redimensionar la imagen
        self.imagen2 = ImageTk.PhotoImage(imagen2)
        self.button = tk.Button(self, image=self.imagen2, command=self.game_rules)
        self.button.place(x=400, y=310, anchor="nw")
        self.button.config(borderwidth="0")

    def registro1(self): # to registro 1
        global tlealtad
        tlealtad = 0
        print("tiene tarjeta: " +str(tlealtad))
        self.destroy()  # Destruye la pantalla actual

        # Crea la pantalla anterior
        pantalla_anterior = PreguntarXRegistroInicio(master=root)
        pantalla_anterior.mainloop()

    def game_rules(self): # rules
        self.destroy()  # Destruye la pantalla actual

        # Crea la pantalla anterior
        pantalla_anterior = Leer_Tarjeta(master=root)
        pantalla_anterior.mainloop()

# LEER TARJETA -------------------------------------------------------------------------------------------------
class Leer_Tarjeta(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # Cargar la imagen
        imagen = Image.open("scan.png")
        imagen = imagen.resize((800, 440))  # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.button = tk.Button(self, image=self.imagen, command=self.next_screen)
        self.button.config(borderwidth="0")
        self.button.pack()

    def next_screen(self): # to tarjeta de lealtad 1
        global tlealtad
        tlealtad = 1
        global game_tries
        print("tiene tarjeta: " +str(tlealtad))
        self.destroy()  # Destruye la pantalla actual
        print("game tries: " +str(game_tries))
        if game_tries > 0:
            pantalla_siguiente = SendReward(master=root)

        # Crea la siguiente pantalla
        else:
            pantalla_siguiente = Reglas1(master=root)
        pantalla_siguiente.mainloop()

# PANTALLA REGLAS -------------------------------------------------------------------------------------------
class Reglas1(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        pygame.mixer.music.stop()
        self.instr1()
        play_music("s2.mp3")
        self.after(4500, self.next_screen)

    def instr1(self):
         # imagen fondo
        imagen = Image.open("reglas1.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

    def next_screen(self): # to game
        self.destroy()  # Destruye la pantalla actual

        # Crea la siguiente pantalla
        pantalla_siguiente = Reglas2(master=root)
        pantalla_siguiente.mainloop()

class Reglas2(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.instr2()
        self.after(4500, self.next_screen)

    def instr2(self):
         # imagen fondo
        imagen = Image.open("reglas2.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

    def next_screen(self): # to game
        self.destroy()  # Destruye la pantalla actual
        pygame.mixer.music.stop()
        # Crea la siguiente pantalla
        pantalla_siguiente = Reglas3(master=root)
        pantalla_siguiente.mainloop()

class Reglas3(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        play_music("juego_latidos.mp3")
        self.instr3()

    def instr3(self):
        # Cargar la imagen
        imagen = Image.open("reglas3.png")
        imagen = imagen.resize((800, 440))  # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.button = tk.Button(self, image=self.imagen, command=self.next_screen)
        self.button.config(borderwidth="0")
        self.button.pack()

    def next_screen(self): # to game
        self.destroy()  # Destruye la pantalla actual
        # Crea la siguiente pantalla
        global raqueta
        if raqueta == 1:
            pantalla_siguiente = Pala1(master=root)
        if raqueta == 2:
            pantalla_siguiente = Pala2(master=root)
        if raqueta == 3:
            pantalla_siguiente = Pala3(master=root)
        else:
            pantalla_siguiente = Reglas1(master=root)
        pantalla_siguiente.mainloop()

class Pala1(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.instr2()
        self.after(5500, self.next_screen)

    def instr2(self):
         # imagen fondo
        imagen = Image.open("pala1.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

    def next_screen(self): # to game
        self.destroy()  # Destruye la pantalla actual
        # Crea la siguiente pantalla
        pantalla_siguiente = CheckSpeed(master=root)
        pantalla_siguiente.mainloop()

class Pala2(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.instr2()
        self.after(5500, self.next_screen)

    def instr2(self):
         # imagen fondo
        imagen = Image.open("pala2.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

    def next_screen(self): # to game
        self.destroy()  # Destruye la pantalla actual
        # Crea la siguiente pantalla
        pantalla_siguiente = CheckSpeed(master=root)
        pantalla_siguiente.mainloop()

class Pala3(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.instr2()
        self.after(5500, self.next_screen)

    def instr2(self):
         # imagen fondo
        imagen = Image.open("pala3.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

    def next_screen(self): # to game
        self.destroy()  # Destruye la pantalla actual
        # Crea la siguiente pantalla
        pantalla_siguiente = CheckSpeed(master=root)
        pantalla_siguiente.mainloop()

# PANTALLA REGISTRO 1 ---------------------------------------------------------------------------------------
class PreguntarXRegistroInicio(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
         # imagen fondo
        imagen = Image.open("unir.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

        # boton fill data
        imagen1 = Image.open("unirLeft.png")
        imagen1 = imagen1.resize((400, 130)) # Redimensionar la imagen
        self.imagen1 = ImageTk.PhotoImage(imagen1)
        self.button = tk.Button(self, image=self.imagen1, command=self.get_data)
        self.button.place(x=0, y=310, anchor="nw")
        self.button.config(borderwidth="0")

        # boton jugar
        imagen2 = Image.open("unirRight.png")
        imagen2 = imagen2.resize((400, 130)) # Redimensionar la imagen
        self.imagen2 = ImageTk.PhotoImage(imagen2)
        self.button = tk.Button(self, image=self.imagen2, command=self.game_rules)
        self.button.place(x=400, y=310, anchor="nw")
        self.button.config(borderwidth="0")

    def get_data(self): # to form
        self.destroy()  # Destruye la pantalla actual

        # Crea la pantalla anterior
        pantalla_anterior = InstruccionesRegistro(master=root)
        pantalla_anterior.mainloop()

    def game_rules(self):
        self.destroy()  # Destruye la pantalla actual

        # Crea la pantalla anterior
        pantalla_anterior = Reglas1(master=root)
        pantalla_anterior.mainloop()

# PANTALLA DISPARO ------------------------------------------------------------------------------------------
# REVISAR ENTRADA DE MATRIZ AQUI
class CheckSpeed(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        global game_tries

        if game_tries >= 3:
            self.final_results()
        else:
            game_tries = game_tries +1
            self.create_widgets()

    def create_widgets(self):

        # Cargar la imagen
        imagen = Image.open("jugar.png")
        imagen = imagen.resize((800, 440))  # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.button = tk.Button(self, image=self.imagen, command=self.run_results)
        self.button.config(borderwidth="0")
        self.button.pack()

    def run_results(self): # to run results
        self.destroy()  # Destruye la pantalla actual

        # Crea la siguiente pantalla
        pantalla_siguiente = ShowSpeed(master=root)
        pantalla_siguiente.mainloop()
    
    def final_results(self): # to final results
        self.destroy()  # Destruye la pantalla actual

        # Crea la siguiente pantalla
        pantalla_siguiente = ShowBest(master=root)
        pantalla_siguiente.mainloop()

# PANTALLA DE RESULTADO PROVISIONAL -------------------------------------------------------------------------
class ShowSpeed(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.instr2()
        self.after(5000, self.next_screen)

    def instr2(self):
         # imagen fondo
        imagen = Image.open("res1.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

        self.label_mensaje = tk.Label(self, text="Velocidad",font=("Arial", 40), bg="#0066FF", foreground="white")
        self.label_mensaje.place(x=400, y=100, anchor="n")

        msg = "30" + " km/hr"
        self.label_mensaje = tk.Label(self, text=msg,font=("Arial", 80), bg="#0066FF", foreground="white")
        self.label_mensaje.place(x=400, y=250, anchor="n")

    def next_screen(self): # to tarjeta de lealtad 1
        self.destroy()  # Destruye la pantalla actual

        # Crea la siguiente pantalla
        pantalla_siguiente = Reglas3(master=root)
        pantalla_siguiente.mainloop()

# PANTALLA RESULTADOS CON Y SIN TARJETA ---------------------------------------------------------------------
class ShowBest(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        global tlealtad
        if tlealtad == 0:
            self.create_widgets_sin_tarj()
        else:
            self.create_widgets_tarj()

    def create_widgets_tarj(self):
         # imagen fondo
        imagen = Image.open("res3.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

        self.after(5000, self.game_rules)

    def create_widgets_sin_tarj(self):
         # imagen fondo
        imagen = Image.open("res3.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

        # boton fill data
        imagen1 = Image.open("res3Left.png")
        imagen1 = imagen1.resize((400, 130)) # Redimensionar la imagen
        self.imagen1 = ImageTk.PhotoImage(imagen1)
        self.button = tk.Button(self, image=self.imagen1, command=self.get_data)
        self.button.place(x=0, y=310, anchor="nw")
        self.button.config(borderwidth="0")

        # boton jugar
        imagen2 = Image.open("res3Right.png")
        imagen2 = imagen2.resize((400, 130)) # Redimensionar la imagen
        self.imagen2 = ImageTk.PhotoImage(imagen2)
        self.button = tk.Button(self, image=self.imagen2, command=self.game_rules)
        self.button.place(x=400, y=310, anchor="nw")
        self.button.config(borderwidth="0")

    def get_data(self): # to form
        self.destroy()  # Destruye la pantalla actual

        # Crea la pantalla anterior
        pantalla_anterior = InstruccionesRegistro(master=root)
        pantalla_anterior.mainloop()

    def game_rules(self):
        self.destroy()  # Destruye la pantalla actual
        global tlealtad
        if tlealtad == 1:
            pantalla_anterior = SendReward(master=root)
        # Crea la pantalla anterior
        else:
            pantalla_anterior = Default(master=root)
        pantalla_anterior.mainloop()

# ENVIAR RECOMPENSA ----------------------------------------------------------------------------------------------------
class SendReward(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        global tlealtad
        tlealtad = 0
        global game_tries
        game_tries = 0
        print("tiene tarjeta: " +str(tlealtad))
        
        self.instr2()
        self.after(5000, self.next_screen)

    def instr2(self):
         # imagen fondo
        imagen = Image.open("send.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

    def next_screen(self): # to tarjeta de lealtad 1
        self.destroy()  # Destruye la pantalla actual

        # Crea la siguiente pantalla
        pantalla_siguiente = Default(master=root)
        pantalla_siguiente.mainloop()


# PANTALLA DE TARJETA DE LEALTAD 1 --------------------------------------------------------------------------
class InstruccionesRegistro(tk.Frame): # --------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
         # imagen fondo
        imagen = Image.open("registro.png")
        imagen = imagen.resize((800, 440)) # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = tk.Label(self, image=self.imagen)
        self.label.pack()

        # boton sin tarjeta
        imagen1 = Image.open("registroLeft.png")
        imagen1 = imagen1.resize((400, 130)) # Redimensionar la imagen
        self.imagen1 = ImageTk.PhotoImage(imagen1)
        self.button = tk.Button(self, image=self.imagen1, command=self.leertarjeta)
        self.button.place(x=0, y=310, anchor="nw")
        self.button.config(borderwidth="0")

        # boton con tarjeta
        imagen2 = Image.open("registroRight.png")
        imagen2 = imagen2.resize((400, 130)) # Redimensionar la imagen
        self.imagen2 = ImageTk.PhotoImage(imagen2)
        self.button = tk.Button(self, image=self.imagen2, command=self.game_rules)
        self.button.place(x=400, y=310, anchor="nw")
        self.button.config(borderwidth="0")

    def leertarjeta(self): # to registro 1
        print("tiene tarjeta: " +str(tlealtad))
        self.destroy()  # Destruye la pantalla actual

        # Crea la pantalla anterior
        pantalla_anterior = Leer_Tarjeta(master=root)
        pantalla_anterior.mainloop()

    def game_rules(self): # rules
        self.destroy()  # Destruye la pantalla actual

        # Crea la pantalla anterior
        pantalla_anterior = Reglas1(master=root)
        pantalla_anterior.mainloop()

littleLeftSize("clubDecathlon.png", "clubDecathlonLeft.png")
littleRightSize("clubDecathlon.png", "clubDecathlonRight.png")
littleLeftSize("unir.png", "unirLeft.png")
littleRightSize("unir.png", "unirRight.png")
littleLeftSize("registro.png", "registroLeft.png")
littleRightSize("registro.png", "registroRight.png")
littleLeftSize("res3.png", "res3Left.png")
littleRightSize("res3.png", "res3Right.png")

# Crear la ventana principal
root = tk.Tk()
root.title("Padel Decathlon")
root.geometry("800x440")

game_tries = 0
tlealtad = 1
raqueta = 3
# Iniciar con la primera pantalla
pantalla_inicial = Default(master=root)
pantalla_inicial.mainloop()