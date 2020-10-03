
from funksjoner import *


# inndata:

print("(1) Oppgi de opplysninger du har (2) Svar blankt når du ikke vet")

print("Nåverdi: ", end = '')
nåverdi = input()

print("Fremtidsverdi: ", end = '')
fremtidsverdi = input()

print("Antall perioder: ", end = '')
perioder = input()

print("Avkastningskrav %: ", end = '')
avkastningskrav = input()
avkastningskrav = avkastningskrav.replace(" ", "").replace("%", "")


# sjekker

finnNåverdi = len(fremtidsverdi) > 0 and len(avkastningskrav) > 0 and len(perioder) > 0
finnFremtidsverdi = len(nåverdi) > 0 and len(avkastningskrav) > 0 and len(perioder) > 0
finnAvkastningskrav = len(nåverdi) > 0 and len(fremtidsverdi) > 0 and len(perioder) > 0


# utdata:

if finnNåverdi:
	fremtidsverdi = float(fremtidsverdi)
	avkastningskrav = float(avkastningskrav) / 100
	perioder = int(perioder)

	nåverdi = fremtidsverdiTilNåverdi(fremtidsverdi, avkastningskrav, perioder)
	print("Nåverdi: " + formaterTall(nåverdi))

	renter = nåverdi * avkastningskrav;
	print("Renter på nåverdi: " + formaterTall(renter))

	if perioder > 1:
		rentesrenter = avkastningskrav * fremtidsverdi - renter
		print("Rentesrenter i fremtidsverdi: " + formaterTall(rentesrenter), end = '')

if finnFremtidsverdi:
	nåverdi = float(nåverdi)
	avkastningskrav = float(avkastningskrav) / 100
	perioder = int(perioder)

	fremtidsverdi = nåverdiTilFremtidsverdi(nåverdi, avkastningskrav, perioder)
	print("Fremtidsverdi: " + formaterTall(fremtidsverdi))

	renter = nåverdi * avkastningskrav;
	print("Renter på nåverdi: " + formaterTall(renter))

	if perioder > 1:
		rentesrenter = avkastningskrav * fremtidsverdi - renter
		print("Rentesrenter i fremtidsverdi: " + formaterTall(rentesrenter), end = '')

if finnAvkastningskrav:
	nåverdi = float(nåverdi)
	fremtidsverdi = float(fremtidsverdi)
	perioder = int(perioder)

	avkastningskrav = nåverdiOgFremtidsverdiTilAvkastningskrav(nåverdi, fremtidsverdi, perioder)
	avkastningskrav *= 100
	avkastningskrav = round(avkastningskrav, 2)

	print("Avkastningskrav %: " + str(avkastningskrav), end = '')
