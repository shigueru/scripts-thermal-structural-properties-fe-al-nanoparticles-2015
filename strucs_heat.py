from ovito.io import *
from ovito.modifiers import *
import os
import shutil

archivo_in = input("Ingrese nombre del archivo : ")
ini = int(input("Ingrese el inicio de tiempo : "))
pas = int(input("Ingrese el paso de tiempo : "))
fin = int(input("Ingrese el limite de tiempo : "))
arch = input("Ingrese el nombre del archivo a guardar : ")

arc = open(arch,"w")

to = fin + pas

rango = range(ini,to,pas)

arc.write("paso OTRO FCC HCP BCC ICO")
arc.write("\n")

#refactorizacion del archivo ###

data = open(archivo_in,"r")

tempo = "temp/"

if os.path.exists(tempo):
    shutil.rmtree(tempo)

os.mkdir(tempo)

linea = data.readlines()

ar = open("no_valido.txt","w")
ar.write("BORRAR NO CONTENIDO NI IMPORTANCIA")

for j, line in enumerate(linea):
    if "ITEM: TIMESTEP" in line:
        p = j
    else:
        if j == p + 1:
            ar.close()
            spl = line.split()
            ar = open(tempo+"dump."+spl[0],"w")
            ar.write("ITEM: TIMESTEP")
            ar.write("\n")
            ar.write(line)
        else:
            ar.write(line)

ar.close()
data.close()

#################

modificador = CommonNeighborAnalysisModifier()
modificador.cutoff = 3.2
modificador.adaptative_mode = False

node = None

for j in rango:
    if node:
        node.source.load(tempo+"dump." + str(j))
    else:

        node = import_file(tempo+"dump." + str(j))

        node.modifiers.append(modificador)

    node.compute()

    otro = modificador.counts[CommonNeighborAnalysisModifier.Type.OTHER]
    fcc = modificador.counts[CommonNeighborAnalysisModifier.Type.FCC]
    hcp = modificador.counts[CommonNeighborAnalysisModifier.Type.HCP]
    bcc = modificador.counts[CommonNeighborAnalysisModifier.Type.BCC]
    ico = modificador.counts[CommonNeighborAnalysisModifier.Type.ICO]
    #dia = modificador.counts[CommonNeighborAnalysisModifier.Type.DIA]

    arc.write(str(j))
    arc.write(" ")
    arc.write(str(otro))
    arc.write(" ")
    arc.write(str(fcc))
    arc.write(" ")
    arc.write(str(hcp))
    arc.write(" ")
    arc.write(str(bcc))
    arc.write(" ")
    arc.write(str(ico))
    arc.write(" ")
   # arc.write(str(dia))
    arc.write("\n")

arc.close()
shutil.rmtree(tempo)
