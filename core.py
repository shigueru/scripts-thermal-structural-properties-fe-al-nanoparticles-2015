import core_functions as cf
import numpy as np

archivo_in = input("Ingrese el nombre del archivo : ")
inter = input("Numero de atomos a cambiar : ")
red = float(input("Ingrese el parametro de red : "))
archivo_ou = input("Ingrese el nombre del archivo para guardar : ")

salida = open(archivo_ou,"w")
data = open(archivo_in, "r")

linea = data.readlines()

# obtener  numero de atomos y paso al atomo central
for i, line in enumerate(linea):
    if i == 3:
        num_atom = int(line)
    else:
        if i == 5:
            dat = line.split()
            pas = (float(dat[1]) - float(dat[0])) / 2
            paso = round(pas,2)
        else:
            continue


#coordenada de atomo central

coor = round(float(dat[0]),2) + paso

#hallar el atomo central

def candidatos(line,co):
    candidato = []
    for i,lin in enumerate(line):
        if i > 8:
            spl = lin.split()
            candi = cf.resta(co,spl[0],spl[2],spl[3],spl[4])
            rpt = candi.count(0.0)
            if rpt > 1:
                candidato.append(candi)
            else:
                continue

    return candidato

candida = candidatos(linea,coor)

atom_cent = cf.filtro(candida)

# obtener coordenadas del atomo central
for k,lin in enumerate(linea):
    if k > 8:
        spl = lin.split()
        if int(spl[0]) == atom_cent[0]:
            coordenadas = [float(spl[2]),float(spl[3]),float(spl[4])]
        else:
            continue
    else:
        continue


# realizando el reemplazo

# -- generamos el rango de radios --
radio = np.arange(red / 2.0,1000 * red, red / 2.0)

# -- cambio --

interc = [] #lista de ID de los atomos a intercambiar

for rd in radio:
    for m,lin in enumerate(linea):
        if m > 8:
            spl = lin.split()
            dist = cf.distancia(coordenadas,spl[2],spl[3],spl[4])
            if dist <= rd:
                if spl[0] in interc:
                    continue
                else:
                    if len(interc) >= int(inter):
                        break
                    else:
                        interc.append(spl[0])
            else:
                continue
        else:
            continue
    if len(interc) > int(inter):
        break


for n,lin in enumerate(linea):
    if n > 8:
        spl = lin.split()
        if spl[0] in interc:
            spl[1] = "2"
            salida.write(str(" ".join(spl)))
            salida.write("\n")
        else:
            salida.write(str(" ".join(spl)))
            salida.write("\n")
    else:
        salida.write(lin)

salida.close()
data.close()
