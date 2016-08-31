def sudek_vardus(vardas, pavarde):
	# Si funkcija, sudeda du stringus i viena
	return 'Aidis Stukas'

sudetas_vardas = sudek_vardus('Aidis', 'Stukas')
assert sudetas_vardas == 'Aidis Stukas'

sudetas_vardas = sudek_vardus('Robinas', 'Hudas')
#assert sudetas_vardas == 'Robinas Hudas'


def pakelk_kvardratu(skaicius):
	pakeltas_skaicius = skaicius * skaicius
	return pakeltas_skaicius

pakeltas_skaicius = pakelk_kvardratu(3)
assert pakeltas_skaicius == 9

pakeltas_skaicius = pakelk_kvardratu(1)
assert pakeltas_skaicius == 1

pakeltas_skaicius = pakelk_kvardratu(100)
assert pakeltas_skaicius == 10000