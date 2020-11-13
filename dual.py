import random

archivo_in = input("Ingrese el nombre del archivo : ")
inter = int(input("Numero de atomos a cambiar : "))
archivo_ou = input("Ingrese el nombre del archivo para guardar : ")

salida = open(archivo_ou, "w")
data = open(archivo_in, "r")

linea = data.readlines()
# obtener numero de atomos
for i, line in enumerate(linea):
    if i == 3:
        num_atom = int(line)
    else:
        continue
# ===============================
# generar indices aleatoriamente
alea = []
n = 0
while n < inter:
    num = random.randint(1,55)
    if num in alea:
        continue
    else:
        alea.append(num)
        n = n + 1
# =================================
# realizar el cambio
rango = range(1,num_atom + 1)

for j, lini in enumerate(linea):
    if j > 8:
        spl = lini.split()
        it = int(spl[0])
        if it in rango:
#            print(spl)
            if it in alea:
                spl[1] = "2"
                salida.write(str(" ".join(spl)))
                salida.write("\n")
                print(spl)
            else:
                salida.write(str(" ".join(spl)))
                salida.write("\n")
        else:
            salida.write(str(" ".join(spl)))
            salida.write("\n")
    else:
        salida.write(lini)


salida.close()
data.close()
