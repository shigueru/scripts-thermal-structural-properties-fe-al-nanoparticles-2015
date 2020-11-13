import tkinter as tk
from tkinter import filedialog
import os

# creamos als funciones

def proceso():
    v = filedialog.askdirectory()
    ini = inicio.get()
    pa = paso.get()
    fi = final.get()
    nom = nombre.get()
    o = filedialog.askdirectory()
    cmd = "ovitos strucs_argv.py %s %s %s %s %s %s"%(ini,pa,fi,nom,v,o)
    os.system(cmd)

#creamos ventana

ventana = tk.Tk()
ventana.title("Estructuras Atomicas")
ventana.geometry("300x300")

# creamos variable sd etexto

inicio = tk.IntVar()
paso = tk.IntVar()
final = tk.IntVar()
nombre = tk.StringVar()
i = tk.StringVar()
o = tk.StringVar()

# creamos etiquetas

init = tk.Label(ventana, text="Inicio")
pas = tk.Label(ventana, text="paso de tiempo")
fin = tk.Label(ventana, text="Fin")
name = tk.Label(ventana, text="Nombre de archivo")

# creamos campos de entrada

init_en = tk.Entry(ventana, textvariable=inicio)
pas_en = tk.Entry(ventana, textvariable=paso)
fin_en = tk.Entry(ventana, textvariable=final)
name_en = tk.Entry(ventana, textvariable=nombre)

# botones

run = tk.Button(ventana, text="procesar", command=proceso)
cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)

# agregamos a la ventana

init.pack()
init_en.pack()
pas.pack()
pas_en.pack()
fin.pack()
fin_en.pack()
name.pack()
name_en.pack()
run.pack()
cerrar.pack()

# iniciamos bucle

ventana.mainloop()
