
import math
import matplotlib.pyplot as plotlib

# ---

def formaterTall(tall):
	tall = round(tall, 2)
	tall = '{:,}'.format(tall).replace(',', ' ') # tusenmellomrom
	tall = tall.replace(".0", ".00")
	return tall

# ---

def finnRealrente(nominellRente, inflasjon):
	realrente = (1+nominellRente) / (1+inflasjon) - 1
	return realrente

def finnInflasjon(nominellRente, realrente):
	inflasjon = (1+nominellRente) / (realrente + 1) - 1
	return inflasjon

def finnNominellRente(realrente, inflasjon):
	nominellRente = (1+realrente) * (1+inflasjon) - 1
	return nominellRente

# ---

def nåverdiTilFremtidsverdi(nåverdi, avkastningskrav, perioder):
	fremtidsverdi = nåverdi * (1+avkastningskrav)**perioder
	return fremtidsverdi

def fremtidsverdiTilNåverdi(fremtidsverdi, avkastningskrav, perioder):
	nåverdi = fremtidsverdi / ((1+avkastningskrav)**perioder)
	return nåverdi

def nåverdiOgFremtidsverdiTilAvkastningskrav(nåverdi, fremtidsverdi, perioder):

	# regnestykket: fremtidsverdi = nåverdi * (1+avkastningskrav)^perioder
	trinn1 = fremtidsverdi / nåverdi
	trinn2 = math.log10(trinn1)
	trinn3 = trinn2 / perioder
	trinn4 = 10**trinn3

	avkastningskrav = round(trinn4 - 1, 4)
	return avkastningskrav

# ---

def finnAnnuitet(nåverdi, fremtidsverdi, avkastningskrav, perioder):

	if nåverdi is not None:
		annuitet = nåverdi * avkastningskrav * (1+avkastningskrav)**perioder / ((1+avkastningskrav)**perioder - 1)
		return annuitet

	elif fremtidsverdi is not None:
		annuitet = fremtidsverdi * avkastningskrav / ((1 + avkastningskrav)**perioder - 1)
		return annuitet

def annuitetTilNåverdi(annuitet, avkastningskrav, perioder):
	nåverdi = annuitet * ((1+avkastningskrav)**perioder - 1) / (avkastningskrav * (1+avkastningskrav)**perioder)
	return nåverdi

def annuitetTilFremtidsverdi(annuitet, avkastningskrav, perioder):
	fremtidsverdi = annuitet * ((1+avkastningskrav)**perioder - 1) / avkastningskrav
	return fremtidsverdi

def finnAvkastningskravForAnnuitet(annuitet, nåverdi, fremtidsverdi, perioder):

	if nåverdi is not None:

		teller = 1
		while True:

			testAvkastningskrav = teller * 0.0001
			testNåverdi = annuitetTilNåverdi(annuitet, testAvkastningskrav, perioder)

			if abs(testNåverdi-nåverdi) < 10:
				return round(testAvkastningskrav, 4)
			else:
				teller += 1

	if fremtidsverdi is not None:

		teller = 1
		while True:

			testAvkastningskrav = teller * 0.0001
			testFremtidsverdi = annuitetTilFremtidsverdi(annuitet, testAvkastningskrav, perioder)

			if round(testFremtidsverdi) == round(fremtidsverdi):
				return round(testAvkastningskrav, 4)
			else:
				teller += 1

def finnPerioderForAnnuitet(annuitet, nåverdi, fremtidsverdi, avkastningskrav):

	if nåverdi is not None:
		teller = 1
		while True:

			testNåverdi = annuitetTilNåverdi(annuitet, avkastningskrav, teller)

			if round(testNåverdi) == round(nåverdi):
				return teller
			else:
				teller += 1

	elif fremtidsverdi is not None:
		perioder = math.log10((fremtidsverdi*avkastningskrav/annuitet) + 1) / math.log10(1 + avkastningskrav)
		return perioder

def økendeAnnuitetTilNåverdi(annuitet, vekst, rente, perioder):
	nåverdi = annuitet * ((1+rente)**perioder - (1+vekst)**perioder) / ((1+rente)**perioder * (rente-vekst))
	return nåverdi

def evigØkendeAnnuitetTilNåverdi(annuitet, vekst, rente):
	kapitaliseringsfaktor = 1 / (rente - vekst)
	nåverdi = annuitet * kapitaliseringsfaktor
	return nåverdi

# ---

def nåverdiTilNåverdiindeks(nåverdi, investeringsbeløp):
	nåverdiindeks = nåverdi / investeringsbeløp
	return nåverdiindeks

def kontantstrømTilInternrente(kontantstrøm): # list med floats

	# lag regnestykke
	regnestykke = ""
	indeks = 0
	while indeks < len(kontantstrøm):
		beløp = kontantstrøm[indeks]
		ledd = str(beløp) + "/" + "((1+internrente)**" + str(indeks) + ")"
		if indeks == 0:
			regnestykke += ledd
		else:
			regnestykke += " + " + ledd
		indeks += 1

	# løs regnestykke
	internrente = "0.0001" # 0.01% startverdi
	inkrementellTeller = 1
	while True:
		svar = eval(regnestykke.replace("internrente", internrente))
		if svar < 0:
			raise ValueError("Negativ internrente")
			break
		if round(svar, 2) == 0:
			return round(float(internrente), 4)
			break
		else:
			inkrementellTeller += 1
			internrente = str(inkrementellTeller * 0.0001) # 0.01 prosentpoeng som inkrementell økning

def kontantstrømmerTilNåverdigraf(kontantstrømmer):

	# maks avkastningskrav
	maksAvkastningskrav = 0
	indeks = 0
	while indeks < len(kontantstrømmer):
		internrente = kontantstrømTilInternrente(kontantstrømmer[indeks])
		internrente *= 100
		print("Internrente " + str(indeks+1) + ": " + str(internrente) + " %")
		internrente = round(internrente) + 50
		if internrente > maksAvkastningskrav:
			maksAvkastningskrav = internrente
		indeks += 1

	# beregn nåverdier
	avkastningskrav = range(1, maksAvkastningskrav) # prosentverdier
	nåverdierForKontantstrømmer = [] # blir 2D-tabell
	for kontantstrøm in kontantstrømmer:
		nåverdier = []

		indeksAvkastningskrav = 0
		while indeksAvkastningskrav < len(avkastningskrav):
			bestemtAvkastningskrav = avkastningskrav[indeksAvkastningskrav]
			nåverdi = 0

			indeksKontantstrøm = 0
			while indeksKontantstrøm < len(kontantstrøm):
				beløp = kontantstrøm[indeksKontantstrøm]
				nåverdi += beløp / ((1+bestemtAvkastningskrav/100)**indeksKontantstrøm)
				indeksKontantstrøm += 1

			nåverdier.append(nåverdi)
			indeksAvkastningskrav += 1

		nåverdierForKontantstrømmer.append(nåverdier)

	# lag grafer
	indeks = 0
	while indeks < len(nåverdierForKontantstrømmer):
		plotlib.plot(avkastningskrav, nåverdierForKontantstrømmer[indeks], label="Prosjekt " + str(indeks+1)) # x, y, navn
		indeks += 1
	plotlib.axhline(linewidth=1, color='r')
	plotlib.xlabel("avkastningskrav %")
	plotlib.ylabel("nåverdi")
	plotlib.legend()
	plotlib.show()

# ---

def omløpsmidlerTilArbeidskapital(omløpsmidler, kortsiktigGjeld):
	return omløpsmidler - kortsiktigGjeld

# ---

def finnKapitalkostnad(lån, lånerente, egenkapital, avkastningskrav):
	totalkapital = lån + egenkapital
	gjeldsandel = lån / totalkapital
	egenkapitalandel = egenkapital / totalkapital

	kapitalkostnad = lånerente * gjeldsandel + avkastningskrav * egenkapitalandel
	return kapitalkostnad

def finnAvkastningskrav(risikofriRente, risikotillegg, inflasjonstillegg):
	avkastningskrav = risikofriRente + risikotillegg + inflasjonstillegg
	return avkastningskrav

def finnAvkastningsKravMedBeta(risikofriRente, markedsporteføljeAvkastning, beta):
	ekstraAvkastningForProsjekt = (markedsporteføljeAvkastning - risikofriRente) * beta
	avkastningskrav = risikofriRente + ekstraAvkastningForProsjekt
	return avkastningskrav
