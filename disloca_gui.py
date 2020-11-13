import tkinter as tk
from tkinter import filedialog
import os

# creamos la funcion

def proceso():
	ent = filedialog.askdirectory() # directorio entrada
	ini = int(inicio.get())
	pas = int(paso.get())
	fin = int(final.get())
	guar = nombre.get()
	sali = filedialog.askdirectory() #directorio salida

	rango = range(ini,fin + pas,pas)

	arc = open(str(sali)+"/"+str(guar),"w")

	for i in rango:
		data = open(str(ent)+"/defo."+str(i),"r")
		linea = data.readlines()

		con = 0

		for j, line in enumerate(linea):
			if j > 9:
				spl = line.split()
				if float(spl[6]) < 3.5:
					con = con + 1
				else:
					continue
		arc.write(str(i)+" ")
		arc.write(str(con))
		arc.write("\n")
		data.close()

	arc.close()

#creamos ventana

ventana = tk.Tk()
ventana.title("Numero de Dislocaciones")
ventana.geometry("300x300")

# creamos variables de texto

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
