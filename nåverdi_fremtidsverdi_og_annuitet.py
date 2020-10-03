
from funksjoner import *


# inndata:

print("(1) Oppgi de opplysninger du har (2) Svar blankt når du ikke vet")

print("Nåverdi: ", end = '')
nåverdi = input()

print("Fremtidsverdi: ", end = '')
fremtidsverdi = input()

print("Annuitet: ", end = '')
annuitet = input()

print("Antall perioder: ", end = '')
perioder = input()

print("Avkastningskrav %: ", end = '')
avkastningskrav = input()
avkastningskrav = avkastningskrav.replace(" ", "").replace("%", "")

print("Vekst %: ", end = '')
vekst = input()
vekst = vekst.replace(" ", "").replace("%", "")


# sjekker

finnNåverdiOgFremtidsverdi = len(annuitet) > 0 and len(avkastningskrav) > 0 and len(perioder) > 0
finnAnnuitetMedNåverdi = len(nåverdi) > 0 and len(avkastningskrav) > 0 and len(perioder) > 0
finnAnnuitetMedFremtidsverdi = len(fremtidsverdi) > 0 and len(avkastningskrav) > 0 and len(perioder) > 0
finnAnnuitetMedVekst = len(annuitet) > 0 and len(vekst) > 0 and len(avkastningskrav) > 0 and len(perioder) > 0 
finnEvigAnnuitetMedVekst = len(annuitet) > 0 and len(vekst) > 0 and len(avkastningskrav) > 0
finnPerioderMedFremtidsverdi = len(annuitet) > 0 and len(fremtidsverdi) > 0 and len(avkastningskrav) > 0
finnPerioderMedNåverdi = len(annuitet) > 0 and len(nåverdi) > 0 and len(avkastningskrav) > 0
finnAvkastningskravMedNåverdi = len(annuitet) > 0 and len(nåverdi) > 0 and len(perioder) > 0
finnAvkastningskravMedFremtidsverdi = len(annuitet) > 0 and len(fremtidsverdi) > 0 and len(perioder) > 0


# utdata

if finnAnnuitetMedVekst:
	annuitet = float(annuitet)
	vekst = float(vekst) / 100
	avkastningskrav = float(avkastningskrav) / 100
	perioder = int(perioder)

	nåverdi = økendeAnnuitetTilNåverdi(annuitet, vekst, avkastningskrav, perioder)		
	print("Nåverdi: " + formaterTall(nåverdi))

elif finnEvigAnnuitetMedVekst:
	annuitet = float(annuitet)
	vekst = float(vekst) / 100
	avkastningskrav = float(avkastningskrav) / 100

	nåverdi = evigØkendeAnnuitetTilNåverdi(annuitet, vekst, avkastningskrav)		
	print("Nåverdi: " + formaterTall(nåverdi))

elif finnNåverdiOgFremtidsverdi:
	annuitet = float(annuitet)
	avkastningskrav = float(avkastningskrav) / 100
	perioder = int(perioder)

	if len(nåverdi) == 0:
		nåverdi = annuitetTilNåverdi(annuitet, avkastningskrav, perioder)		
		print("Nåverdi: " + formaterTall(nåverdi))

	if len(fremtidsverdi) == 0:
		fremtidsverdi = annuitetTilFremtidsverdi(annuitet, avkastningskrav, perioder)
		print("Fremtidsverdi: " + formaterTall(fremtidsverdi), end = '')

elif finnAnnuitetMedNåverdi:
	nåverdi = float(nåverdi)
	avkastningskrav = float(avkastningskrav) / 100
	perioder = int(perioder)

	annuitet = finnAnnuitet(nåverdi, None, avkastningskrav, perioder)
	print("Annuitet: " + formaterTall(annuitet), end = '')

elif finnAnnuitetMedFremtidsverdi:
	fremtidsverdi = float(fremtidsverdi)
	avkastningskrav = float(avkastningskrav) / 100
	perioder = int(perioder)

	annuitet = finnAnnuitet(None, fremtidsverdi, avkastningskrav, perioder)
	print("Annuitet: " + formaterTall(annuitet), end = '')

elif finnPerioderMedFremtidsverdi:
	annuitet = float(annuitet)
	fremtidsverdi = float(fremtidsverdi)
	avkastningskrav = float(avkastningskrav) / 100

	perioder = finnPerioderForAnnuitet(annuitet, None, fremtidsverdi, avkastningskrav)
	print("Perioder: " + str(perioder))

elif finnPerioderMedNåverdi:
	annuitet = float(annuitet)
	nåverdi = float(nåverdi)
	avkastningskrav = float(avkastningskrav) / 100

	perioder = finnPerioderForAnnuitet(annuitet, nåverdi, None, avkastningskrav)
	print("Perioder: " + str(perioder))

elif finnAvkastningskravMedNåverdi:
	annuitet = float(annuitet)
	nåverdi = float(nåverdi)
	perioder = int(perioder)

	avkastningskrav = finnAvkastningskravForAnnuitet(annuitet, nåverdi, None, perioder)
	avkastningskrav *= 100

	print("Avkastningskrav %: " + formaterTall(avkastningskrav), end = '')

elif finnAvkastningskravMedFremtidsverdi:
	annuitet = float(annuitet)
	fremtidsverdi = float(fremtidsverdi)
	perioder = int(perioder)

	avkastningskrav = finnAvkastningskravForAnnuitet(annuitet, None, fremtidsverdi, perioder)
	avkastningskrav *= 100

	print("Avkastningskrav %: " + formaterTall(avkastningskrav), end = '')

else:
	print("For lite opplysninger til å gjøre noe.")
