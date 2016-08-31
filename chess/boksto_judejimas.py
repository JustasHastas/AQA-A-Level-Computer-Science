lentos_dydis = [8, 8]
boksto_pozicija = (4, 4)
karaliaus_pozicija = (4, 7)
arklio_pozicija = (1, 7)
karalienes_pozicija = (3, 7)
galimi_ejimai = []

# Rook moves
for x in range(0, lentos_dydis[0]):
	galimi_ejimai.append((4, x))

for y in range(0, lentos_dydis[1]):
	galimi_ejimai.append((y, 4) )
galimi_ejimai.remove((4, 4))
galimi_ejimai.remove((4, 4))
print(galimi_ejimai)

# kNight move

def duok_knighto_ejimus(start_x, start_y):
	'''
	kryptys = 'vdak'
	judejimas = []
	# Pasirenkame judejimo krypti, viso ju yra keturios
	for kryptis in kryptys:
		if kryptis in 'va':
			judejimas.append(kryptis * 2 + 'd')
			judejimas.append(kryptis * 2 + 'k')
		elif kryptis in 'dk':
			judejimas.append(kryptis * 2 + 'v')
			judejimas.append(kryptis * 2 + 'a')
	print(judejimas)
	'''
	knighto_ejimai = []
	### sudedamas knighto ejimu sarasas
	return knighto_ejimai  # [(-1, -2), (1, 2)]

knighto = duok_knighto_ejimus(0, 0)

print(knighto)

def test_duok_knighto_ejimus():
	pass


# King move
def duok_king_ejimus(x, y):
	galimi_ejimai = []
	for x1, y1 in [(1, 1), (-1, -1),(1, 0)]:
		galimas_ejimas = (x + x1, y + y1)
		galimi_ejimai.append(galimas_ejimas)
	return galimi_ejimai

king_ejimai = duok_king_ejimus(999, 0)
print('Karaliaus', king_ejimai)

# Bishop
def b_judejimas(x, y, target_x, target_y): 
    # patikrinam, ar langelyje yra rikis
    if board_x[x][y] == 'B':
        while True: 
            # Patikrinam ar yra laisvas langelis musu kelyje.
            next_cell = board_x[x - 1][y - 1]
            if next_cell == ".":
                if next_cell == board_x[target_x][target_y]:
                    board_x[target_x][target_y] = "B"
                    board_x[x][y] = '.'
                    print(galimi_ejimai)

# Queen
for x in range(0, lentos_dydis[0]):
	galimi_ejimai.append((3, x + 1))
	galimi_ejimai.append((3, x - 1))

for y in range(0, lentos_dydis[1]):
	galimi_ejimai.append((3, y))
galimi_ejimai.remove((3, 7))
print(galimi_ejimai)

# Turedamas taisykles, patikrini, ar toks ejimas galimas konkrecioje lentoje

koord = (0, 0)
def ar_galimas_ejimas(start_koord, target_koord):
	s_x, s_y = start_koord
	t_x, t_y = target_koord
	piece_type = board_x[s_x][s_y]
	if piece_type == 'B':
		pass #....
	elif piece_type == 'N':
		pass #....
	elif piece_type == 'K':
		pass #
	# print('Si figura negali daryti tokio ejimo')
	# print('Si figura ejimo negali daryti, nes kita figura blokuoja pereinama langeli')

def gauti_galimus_ejimus(figura, x, y):
	if figura == 'K':
		return duok_king_ejimus(x, y):
	elif figura == 'P':
		return duok_paw_ejimus(x, y):


#player_move = input("iveskite figoros, kuria noresite judinti koordinates") 
galimi_ejimai = gauti_galimus_ejimus('K', 1, 5)
print(galimi_ejimai)
#player_move = input("Langelio i kuri pajudinti figura koordinates")




# ['B', '.', '.']
# ['P', '.', '.']
# ['.', '.', '.']
