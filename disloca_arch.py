ini = int(input("Ingrese el inicio : "))
paso = int(input("Ingrese el paso de tiempo : "))
fin = int(input("Ingrese el final : "))
guar = input("Ingrese nombre del archivo a generar : ")

rango = range(ini,fin + paso,paso)

arc = open(str(guar),"w")

for i in rango:
    data = open("defo."+str(i),"r")
    linea = data.readlines()

    con = 0

    for j, line in enumerate(linea):
        if j > 9:
            spl = line.split()
            if float(spl[6]) > 3.0 and float(spl[6]) < 4.8:
                con = con + 1
            else:
                continue
    arc.write(str(i)+" ")
    arc.write(str(con))
    arc.write("\n")
    data.close()

arc.close()
