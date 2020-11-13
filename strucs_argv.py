from ovito.io import *
from ovito.modifiers import *
import sys

ini = int(sys.argv[1])
pas = int(sys.argv[2])
fin = int(sys.argv[3])
arch = str(sys.argv[4])
ent = str(sys.argv[5]) #path d eentrada
sal = str(sys.argv[6]) #path salida

#ini = int(input("Ingrese el inicio de tiempo : "))
#pas = int(input("Ingrese el paso de tiempo : "))
#fin = int(input("Ingrese el limite de tiempo : "))
#arch = input("Ingrese el nombre del archivo a guardar : ")

ar = open(str(sal) + "/" + arch,"w")

to = fin + pas

rango = range(ini,to,pas)

ar.write("paso OTRO FCC HCP BCC ICO DIA")
ar.write("\n")

modificador = CommonNeighborAnalysisModifier()
modificador.cutoff = 3.2
modificador.adaptative_mode = False

node = None

for j in rango:
    if node:
        node.source.load(str(ent) + "/dump." + str(j))
    else:

        node = import_file(str(ent) + "/dump." + str(j))

        node.modifiers.append(modificador)

    node.compute()

    otro = modificador.counts[CommonNeighborAnalysisModifier.Type.OTHER]
    fcc = modificador.counts[CommonNeighborAnalysisModifier.Type.FCC]
    hcp = modificador.counts[CommonNeighborAnalysisModifier.Type.HCP]
    bcc = modificador.counts[CommonNeighborAnalysisModifier.Type.BCC]
    ico = modificador.counts[CommonNeighborAnalysisModifier.Type.ICO]
    dia = modificador.counts[CommonNeighborAnalysisModifier.Type.DIA]

    ar.write(str(j))
    ar.write(" ")
    ar.write(str(otro))
    ar.write(" ")
    ar.write(str(fcc))
    ar.write(" ")
    ar.write(str(hcp))
    ar.write(" ")
    ar.write(str(bcc))
    ar.write(" ")
    ar.write(str(ico))
    ar.write(" ")
    ar.write(str(dia))
    ar.write("\n")

ar.close()
