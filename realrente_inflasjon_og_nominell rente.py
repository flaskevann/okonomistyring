
from funksjoner import *


# inndata

print("(1) Oppgi nøyaktig to opplysninger (2) Svar blankt når du ikke vet")

print("Realrente %: ", end = '')
realrente = input()
realrente = realrente.replace(" ", "").replace("%", "")

print("Inflasjon %: ", end = '')
inflasjon = input()
inflasjon = inflasjon.replace(" ", "").replace("%", "")

nominellRente = ""
if len(realrente) == 0 or len(inflasjon) == 0:
	print("Nominell rente %: ", end = '')
	nominellRente = input()
	nominellRente = nominellRente.replace(" ", "").replace("%", "")


# sjekker

finnReal = len(realrente) == 0 and len(inflasjon) > 0 and len(nominellRente) > 0
finnInf = len(inflasjon) == 0 and len(realrente) > 0 and len(nominellRente) > 0
finnNominell = len(nominellRente) == 0 and len(realrente) > 0 and len(inflasjon) > 0


# utdata

if finnReal:
	inflasjon = float(inflasjon) / 100
	nominellRente = float(nominellRente) / 100

	realrente = finnRealrente(nominellRente, inflasjon)

	realrente *= 100
	realrente = round(realrente, 2)
	print("Realrente %: " + str(realrente))

elif finnInf:
	realrente = float(realrente) / 100
	nominellRente = float(nominellRente) / 100

	inflasjon = finnInflasjon(nominellRente, realrente)

	inflasjon *= 100
	inflasjon = round(inflasjon, 2)
	print("Inflasjon %: " + str(inflasjon))

elif finnNominell:
	realrente = float(realrente) / 100
	inflasjon = float(inflasjon) / 100

	nominellRente = finnNominellRente(realrente, inflasjon)

	nominellRente *= 100
	nominellRente = round(nominellRente, 2)
	print("Nominell rente %: " + str(nominellRente))

else:
	print("For lite opplysninger til å gjøre noe.")
