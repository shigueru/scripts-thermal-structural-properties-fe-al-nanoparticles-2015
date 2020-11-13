from ase.lattice.cubic import FaceCenteredCubic
from ase.io import *
from ase.visualize import view
import math

a = float(input("Ingrese parametro de red : "))
arc = open("fcc_108000.txt","w")

atomos = FaceCenteredCubic(directions=[[1,0,0],[0,1,0],[0,0,1]],
 										size=(30,30,30),symbol='Cu',pbc=(1,1,1),latticeconstant=a)

posi = atomos.get_positions()
simbol = atomos.get_chemical_symbols()

arc.write(str(len(simbol))+"\n")

for i in range(len(simbol)):
	arc.write(str(posi[i,0])+" ")
	arc.write(str(posi[i,1])+" ")
	arc.write(str(posi[i,2])+"\n")

#----Luego borrar----#
#write('fcc_108000.txt',atomos,format='xyz')
pos = atomos.get_positions()
c_m = atomos.get_center_of_mass()
coor_x = pos[:,0]
coor_y = pos[:,1]
coor_z = pos[:,2]
print "posicion de cero",pos[0]
print "centro de masa", c_m
print "x_max y x_min:",coor_x.max(),coor_x.min()
#view(atoms)
