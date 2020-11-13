archivo_in = input("Ingrese el nombre del archivo : ")
archivo_ou = input("Ingrese el nombre del archivo a guardar : ")
print("Ingrese rango y paso de tiempo:")
ini  = int(input("Ingrese inicio : "))
fi = int(input("Ingrese fin : "))
pa = int(input("Ingrese paso : "))

data = open(archivo_in,"r")
salida = open(archivo_ou,"w")

linea = data.readlines()

rango = range(ini,fi+pa,pa)

lista = ["#TimeStep","c_msd1"]

for j, line in enumerate(linea):
    if j > 2:
        spl = line.split()
        it = int(spl[0])
        if it in rango:
            salida.write(str(" ".join(lista)))
            salida.write("\n")
            lista.clear()
            lista.append(spl[0])
        else:
            lista.append(spl[1])
    else:
        continue
salida.write(str(" ".join(lista)))

data.close()
salida.close()
