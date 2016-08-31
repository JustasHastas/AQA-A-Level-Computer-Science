
board_x=[]

for x in range(8):
    board_y =[]
    for y in range(8):

        board_y.append('.')

    board_x.append(board_y)
board_x[7][4] = 'K'
board_x[7][3] = 'Q'
board_x[7][2] = 'B'
board_x[7][1] = 'N'
board_x[7][0] = 'R'
board_x[7][5] = 'B'
board_x[7][6] = 'N'
board_x[7][7] = 'R'

for x in range(0,8):
    board_x[6][x] = 'P'


def p_judejimas(x, y, kiek_juda):
    if board_x[x][y] == 'P':
        board_x[x][y] = '.'
        board_x[x - kiek_juda][y] = 'P'
    else:
        print('Ne PESKA')

#75 24

def patikrinti_ar_geras_ejimas(lenta, figura, starta, tiksla):
    return True

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

    else:
        print("There is no Bishop")

p_judejimas(6, 4, 2)
#b_judejimas(7, 5, 4, 2) #turi parasyti "This move is not allowed: impossible move"
b_judejimas(7, 5, 6, 4) # turi perkelti figura.
#b_judejimas(7, 5, 2, 4) # turi perkelti figura.
for x in board_x:
    print(x)


