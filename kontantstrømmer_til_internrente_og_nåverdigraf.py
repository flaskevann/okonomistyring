
from funksjoner import *


# inndata

print("Antall kontantstrømmer: ", end = '')
antall = input()
antall = int(antall)

kontantstrømmer = []
indeks1 = 0
while indeks1 < antall:
	print("Kontantstrøm " + str(indeks1+1) + ": ", end = '')
	kontantstrøm = input()
	kontantstrøm = kontantstrøm.split()
	kontantstrømmer.append(kontantstrøm)
	indeks1 += 1

	indeks2 = 0
	while indeks2 < len(kontantstrøm):
		kontantstrøm[indeks2] = float(kontantstrøm[indeks2])
		indeks2 += 1


# utdata

kontantstrømmerTilNåverdigraf(kontantstrømmer)
