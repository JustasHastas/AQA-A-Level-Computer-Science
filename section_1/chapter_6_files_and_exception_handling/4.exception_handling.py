class Failo_atidarymo_klauda(Exception):
	pass 

try:
	abc = open("greita_masina.txt")
except:
	raise Failo_atidarymo_klauda('klaida')
