import os
import shutil

archivo_in = input("Ingrese el nombre del archivo : ")
g = input("Guardar en : ")
print("Ingrese rango y paso de tiempo:")
ini = int(input("inicio : "))
fi = int(input("fin : "))
pa = int(input("paso : "))
cor = int(input("Ingrese corte : "))

data = open(archivo_in, "r")

tempo = g + "/" + "temp/"
perm = g + "/" + "rdf/"
if os.path.exists(tempo):
    shutil.rmtree(tempo)
if os.path.exists(perm):
    shutil.rmtree(perm)
os.mkdir(tempo)
linea = data.readlines()

rango = range(ini,fi+pa,pa)
ar = open("no_valido.txt","w")
ar.write("BORRAR: NO TIENE CONTENIDO NI IMPORTANCIA")
for j, line in enumerate(linea):
    if j > 2:
        spl = line.split()
        it = int(spl[0])
        if it in rango:
            ar.close()
            ar = open(tempo+spl[0]+".txt","w")
        else:
            ar.write(line)

ar.close()
data.close()

os.mkdir(perm)
ar2 = open("no vale.txt","w")
ar2.write("BORRAR NO TIENE VALOR")
for h in rango:
    arc = open(tempo+str(h)+".txt","r")
    lin = arc.readlines()
    ar2.close()
    ar2 = open(perm+str(h)+".txt","w")
    for t, li in enumerate(lin):
        #print(li)
        if t > cor:
            ar2.write(li)
        else:
            continue
    arc.close()

shutil.rmtree(tempo)
