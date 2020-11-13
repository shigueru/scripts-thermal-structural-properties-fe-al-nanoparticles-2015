import math


"""
Funciones para el programa
core.py
"""

"""
Funcion para ubicar el atomo central
------------------------------------

parametros:

- id : identificador del atomo 
- x : coordenada x
- y : coordenada y
- z : coordenada z

devuelve:

- lista : lista conteniendo id y valor absoluto
          de la resta de la coordenada buscada
          y la coordenada actual.

"""

def resta(cor,id,x,y,z):
	"""
	 calculamos los valores absolutos
	 de las diferencias
	"""
	res_1 = abs(cor - float(x))
	res_2 = abs(cor - float(y))
	res_3 = abs(cor - float(z))
	# creamos una lista
	lista = []
	#agregamos los valores
	lista.append(int(id))
	lista.append(round(res_1,2))
	lista.append(round(res_2,2))
	lista.append(round(res_3,2))
	
	return lista

def filtro(lista):
	tem = [1,20]
	for i in range(len(lista)):
		rpt = lista[i].count(0.0)
		if rpt == 3:
			return lista[i]
		else:
			for j in range(1,4):
				if lista[i][j] != 0.0:
					if lista[i][j] < tem[1]:
						tem[0] = i
						tem[1] = lista[i][j]
					else:
						continue
				else:
					continue
	return lista[tem[0]]

def distancia(cent,x,y,z):
	xx = float(x)
	yy = float(y)
	zz = float(z)
	xc = cent[0]
	yc = cent[1]
	zc = cent[2]

	d = math.sqrt((xc - xx)**2 + (yc - yy)**2 + (zc - zz)**2)
	return d
