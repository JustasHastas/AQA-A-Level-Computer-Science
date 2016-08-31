programos_pavadinimas = 'dictionary programa'

dictionary = {
	'mouse':{'definition':'Mouse is an animal very small and fast', 'weight': '10-100g'},   # Consists of two things - key and value, e.g. 'mouse' and 'cat'
	'car': {'definition':'A means of transporation', 'weight': '10-100t'}, 
	'marsas':{'definition':'A big body of universe', 'weight': '10-100ttttt'}}

if __name__ == '__main__':
	slaptas_kintamasis_kuris_leidziamas_tik_kai_sis_dokumentas_yra_pagr_programa = 'Taip'
	print(slaptas_kintamasis_kuris_leidziamas_tik_kai_sis_dokumentas_yra_pagr_programa)
	computer = input("The computer has information about 3 objects - mouse, car, marsas. Pick one to know more about.")
	print(dictionary[computer])