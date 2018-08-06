from random import randint

def print_board(board):
    for row in board:
        print(" ".join(row))
        
def arrange_ships(ship, ship_class):
    ship_row = randint(0, 9)
    ship_col = randint(0, 9)

    ship_class[ship][0]=[ship_row,ship_col]
    fix_row_or_col = randint(0, 1)

    ship_size = len(ship_class[ship])

    for j in range(1,ship_size):                        
        if fix_row_or_col:
            if all(ship_elem[1]<9 for ship_elem in ship_class[ship]):
                ship_col+=1
            else:
                ship_col=min(ship_class[ship][0:j], key = lambda t: t[1])[1]-1
            ship_class[ship][j]=[ship_row,ship_col]
        else:
            if all(ship_elem[0]<9 for ship_elem in ship_class[ship]):
                ship_row+=1
            else:
                ship_row=min(ship_class[ship][0:j], key = lambda t: t[0])[0]-1
            ship_class[ship][j]=[ship_row,ship_col]
    return ship_class[ship]


board = [["O"]*10 for i in range(10)]
defence_board = [["O"]*10 for i in range(10)]

ship_class = [[[0]*2 for i in range(5)],
              [[0]*2 for i in range(4)],
              [[0]*2 for i in range(3)],
              [[0]*2 for i in range(3)],
              [[0]*2 for i in range(2)]]

print("Let's play Battleship!")

for i in board:
    print(i)

for ship in range(0, len(ship_class)):    
    flag=True
    while flag:
        ship_class[ship]=arrange_ships(ship, ship_class)
        if all(item not in i for i in ship_class[0:ship] for item in ship_class[ship]):
            flag=False
            break
        else:
            flag=True

           
for ship in ship_class:
	for ship_ordinates in ship:
		defence_board[ship_ordinates[0]][ship_ordinates[1]]=ship_class.index(ship)

carrier = 5
battleship = 4
cruiser = 3
submarine = 3
destroyer = 2
   
while defence_board != board:
    while True:
        while True:
            try:
                guess_row = int(input("Guess Row:"))-1
            except:
                print("Please provide valid row")
                continue

            if guess_row<0 or guess_row>9:
                print("It is not a valid row")
                continue
            else:
                break
        while True:
            try:
                guess_col = int(input("Guess Col:"))-1
            except:
                print("Please provide valid column")
                continue
            
            if guess_col<0 or guess_col>9:
                print("It is not a valid column")
                continue
            else:
                break
        if board[guess_row][guess_col] == "X":
            print("You've already guessed that earlier")
            continue
        else:
            break
    board[guess_row][guess_col] = "X"    
    if defence_board[guess_row][guess_col] != "O":                     
        for i in ship_class:
            if [guess_row, guess_col] in i:
                if ship_class.index(i)==0:
                    carrier-=1
                    print("Carrier Hit" if carrier!=0 else "Carrier Down")                     
                elif ship_class.index(i)==1:
                    battleship-=1
                    print("Battleship Hit"  if battleship!=0 else "Battleship Down")
                elif ship_class.index(i)==2:
                    cruiser-=1
                    print("Cruiser Hit" if cruiser!=0 else "Cruiser Down")
                elif ship_class.index(i)==3:
                    submarine-=1
                    print("Submarine Hit" if submarine!=0 else "Submarine Down")
                else:
                    destroyer-=1
                    print("Destroyer Hit" if destroyer!=0 else "Destroyer Down")

    defence_board[guess_row][guess_col] = "X"         
    for i in defence_board:
        print(i)

if carrier==0 and battleship==0 and cruiser==0 and submarine==0 and destroyer==0:
    print("You Won!! Hurray!!!")
