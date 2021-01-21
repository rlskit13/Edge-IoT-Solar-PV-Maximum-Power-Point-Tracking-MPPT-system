import json
import os


def PO(Vpv, Ipv, Ppv):
	deltaD = 0.01
	Pprev = 0
	Vprev = 0
	Vref = 0
	if not os.path.exists("Pprev.txt"):
		f = open("Pprev.txt", "w+")
		f.write(str(Ppv))
		f.close()
		f = open("Vprev.txt", "w+")
		f.write(str(Vprev))
		f.close()
	else:
		f = open("Pprev.txt", "r")
		Pprev = f.read()
		f.close()
		if Ppv-float(Pprev) == 0:
			Pprev = Ppv
			Vref = Vpv
		elif Ppv-float(Pprev) != 0:
			f = open("Vprev.txt", "r")
			Vprev = f.read()
			f.close()
			if Ppv-float(Pprev) > 0:
				if Vpv-float(Vprev) > 0:
					Vref = Vpv + deltaD
				elif Vpv-float(Vprev) < 0:
					Vref = Vpv - deltaD
			elif Ppv-float(Pprev) < 0:
				if Vpv-float(Vprev) > 0:
					Vref = Vpv - deltaD
				elif Vpv-float(Vprev) < 0:
					Vref = Vpv + deltaD

	Pprev = Ppv
	Vprev = Vpv
	f = open("Pprev.txt", "w")
	f.write(str(Pprev))
	f.close()
	f = open("Vprev.txt", "w")
	f.write(str(Vprev))
	f.close()
	return Vref
		
def Incond(Vpv, Ipv, Ppv):
	deltaD = 0.01
	Pprev = 0
	Vprev = 0
	Iprev =0
	Vd = 0
	Id = 0

	Vref = 0
	if not os.path.exists("PprevIC.txt"):
		f = open("PprevIC.txt", "w+")
		f.write(str(Ppv))
		f.close()
		f = open("VprevIC.txt", "w+")
		f.write(str(Vprev))
		f.close()
		f = open("IprevIC.txt", "w+")
		f.write(str(Iprev))
		f.close()
	else:
		f = open("VprevIC.txt", "r")
		Vprev = f.read()
		f.close()
		f = open("IprevIC.txt", "r")
		Iprev = f.read()
		f.close()
		Vd = float(Vpv)-float(Vprev)
		Id = float(Ipv)-float(Iprev)
		if Vd == 0:
			if Id == 0:
				Pprev = Ppv
				Vref = Vpv
				Vprev = Vpv
				Iprev = Ipv
			else:
				if Id > 0:
					Vref = Vpv - deltaD
				elif Id < 0:
					Vref = Vpv + deltaD
		
		elif Vd != 0:
			if Ipv + (Id/Vd)*Vpv == 0:
				Pprev = Ppv
				Vref = Vpv
				Vprev = Vpv
				Iprev = Ipv
			else:
				if Ipv + (Id/Vd)*Vpv > 0:
					Vref = Vpv + deltaD
				elif Ipv + (Id/Vd)*Vpv < 0:
					Vref = Vpv - deltaD
			

		Pprev = Ppv
		Vprev = Vpv
		Iprev = Ipv

	f = open("PprevIC.txt", "w")
	f.write(str(Pprev))
	f.close()
	f = open("VprevIC.txt", "w")
	f.write(str(Vprev))
	f.close()
	f = open("IprevIC.txt", "w")
	f.write(str(Iprev))
	f.close()
	return Vref
	
	