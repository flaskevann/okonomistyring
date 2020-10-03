
from funksjoner import *
import unittest

class TestØkonomistyring(unittest.TestCase):

	def test_nåverdiTilFremtidsverdi(self):
		fremtidsverdi = nåverdiTilFremtidsverdi(100, 0.1, 10)
		fremtidsverdi = round(fremtidsverdi, 2)
		self.assertEqual(fremtidsverdi, 259.37)

	def test_fremtidsverdiTilNåverdi(self):
		nåverdi = fremtidsverdiTilNåverdi(259.37, 0.1, 10)
		nåverdi = round(nåverdi, 2)
		self.assertEqual(nåverdi, 100)

	def test_nåverdiOgFremtidsverdiTilRentefot(self):
		avkastningskrav = nåverdiOgFremtidsverdiTilAvkastningskrav(100, 200, 5)
		avkastningskrav *= 100
		self.assertEqual(avkastningskrav, 14.87)

# ---

	def test_finnAnnuitet(self):
		annuitet = finnAnnuitet(100, None, 0.1, 10)
		annuitet = round(annuitet, 2)
		self.assertEqual(annuitet, 16.27)

		annuitet = finnAnnuitet(None, 200, 0.1, 10)
		annuitet = round(annuitet, 2)
		self.assertEqual(annuitet, 12.55)

	def test_annuitetTilNåverdi(self):
		nåverdi = annuitetTilNåverdi(16.27, 0.1, 10)
		nåverdi = round(nåverdi)
		self.assertEqual(nåverdi, 100)

	def test_annuitetTilFremtidsverdi(self):
		fremtidsverdi = annuitetTilFremtidsverdi(12.55, 0.1, 10)
		fremtidsverdi = round(fremtidsverdi)
		self.assertEqual(fremtidsverdi, 200)

	def test_finnAvkastningskravForAnnuitet(self):
		avkastningskrav = finnAvkastningskravForAnnuitet(16132, 240000, None, 20)
		self.assertEqual(avkastningskrav, 0.03)

		avkastningskrav = finnAvkastningskravForAnnuitet(10000, None, 242974, 4*5)
		self.assertEqual(avkastningskrav, 0.02)

	def test_finnPerioderForAnnuitet(self):
		perioder = finnPerioderForAnnuitet(2866.56, None, 200000, 0.005)
		perioder = round(perioder)
		self.assertEqual(perioder, 60)

		perioder = finnPerioderForAnnuitet(20000, 307449, None, 0.05)
		self.assertEqual(perioder, 30)

	def test_økendeAnnuitetTilNåverdi(self):
		nåverdi = økendeAnnuitetTilNåverdi(200000, 0.02, 0.07, 25)
		nåverdi = round(nåverdi)
		self.assertEqual(nåverdi, 2790879)

	def test_evigØkendeAnnuitetTilNåverdi(self):
		nåverdi = evigØkendeAnnuitetTilNåverdi(97200, 0, 0.09)
		nåverdi = round(nåverdi)
		self.assertEqual(nåverdi, 1080000)

# ---

	def test_nåverdiTilNåverdiindeks(self):
		nåverdiindeks = nåverdiTilNåverdiindeks(100, 200)
		self.assertEqual(nåverdiindeks, 0.5)

	def test_kontantstrømTilInternrente(self):
		internrente = kontantstrømTilInternrente([-99.99123, 203.1345])
		internrente = round(internrente * 100, 2)
		self.assertEqual(internrente, 103.15)

	def test_omløpsmidlerTilArbeidskapital(self):
		arbeidskapital = omløpsmidlerTilArbeidskapital(200, 100)
		self.assertEqual(arbeidskapital, 100)

	def test_finnKapitalkostnad(self):
		kapitalkostnad = finnKapitalkostnad(1000, 0.09, 500, 0.21)
		self.assertEqual(kapitalkostnad, 0.13)

	def test_finnAvkastningskrav(self):
		avkastningskrav = finnAvkastningskrav(0.05, 0.1, 0.02)
		self.assertEqual(avkastningskrav, 0.17)

	def test_finnAvkastningsKravMedBeta(self):
		forventetProsjektAvkastning = finnAvkastningsKravMedBeta(0.05, 0.16, 0.8)
		self.assertEqual(forventetProsjektAvkastning, 0.138)

if __name__ == '__main__':
	unittest.main()
