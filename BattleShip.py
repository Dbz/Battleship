from random import randint

OCEAN = "O"
FIRE = "X"
HIT = "*"
player_radar = []
player_board = []
ai_radar = []
ai_board = []

ai_hit = 0 #has the ai hit me?
vert_ship = -1 #ai var is_my_ship_vertical

def print_board():
    for row in range(board_size):
        print (" ".join(player_radar[row]), "||" , " ".join(player_board[row]))

def random_row(is_vertical):
    if is_vertical:
        return randint(0, board_size - ship_size)
    else:
        return randint(0, board_size -1)
    
def random_col(is_vertical):
    if is_vertical:
        return randint(0, board_size - 1)
    else:
        return randint(ship_size-1, board_size -1)
    
def makeShip():
    temp_board = []
    for _ in range(board_size):
            temp_board.append([OCEAN] * board_size)
    ships_added = 0
    while (ships_added < num_ships): # make multiple ships
        is_vertical = randint(0, 1) # vertical ship if true
        ship_row = random_row(is_vertical)
        ship_col = random_col(is_vertical)

        # check if location is occupied. if so, retry making ship.
        unoccupied = True
        if (temp_board[ship_row][ship_col] != OCEAN): 
            unoccupied = False
        if is_vertical:
            if (temp_board[ship_row+ship_size-ships_added-1][ship_col] != OCEAN): 
                unoccupied = False
            for p in range(ship_size-ships_added -2):    
                if(temp_board[ship_row+p+1][ship_col]!=OCEAN): 
                    unoccupied = False
        else:
            if (temp_board[ship_row][ship_col-ship_size+ships_added+1] != OCEAN): 
                unoccupied = False
            for p in range(ship_size-ships_added -2):
                if(temp_board[ship_row][ship_col-p-1]!=OCEAN): 
                    unoccupied = False
                
        if unoccupied:
            if (ship_size - ships_added == 1):
                temp_board[ship_row][ship_col] = "+" # ship of size 1
            elif is_vertical:
                temp_board[ship_row][ship_col] = "^"
                temp_board[ship_row+ship_size-ships_added-1][ship_col] = "v"
                for p in range(ship_size-ships_added -2):
                    temp_board[ship_row+p+1][ship_col] = "+"
            else:
                temp_board[ship_row][ship_col] = ">"
                temp_board[ship_row][ship_col-ship_size+ships_added+1] = "<"
                for p in range(ship_size-ships_added -2):
                    temp_board[ship_row][ship_col-p-1] = "+"
            ships_added = ships_added+1
    return temp_board

def exists(row, col, b): # true if ocean
    if row < 0 or row >= board_size:
        return 0
    elif col < 0 or col >= board_size:
        return 0
    if b[row][col] == OCEAN:
        return 1
    else:
        return 0

# Make the boards (and set ship_size)
board_size = int(input("Please input a board size: "))
for x in range(board_size):
        player_radar.append([OCEAN] * int(board_size))
        ai_radar.append([OCEAN] * int(board_size))
ship_size = -1
while ship_size > board_size or ship_size < 0:
    ship_size = int(input("Please input a ship size: "))
num_ships = -1
while num_ships > ship_size or num_ships < 0:
    num_ships = int(input("Please input the number of ships: "))

ai_board = makeShip()
ai_ship_alive = ship_size
for i in range(0, num_ships):
    ai_ship_alive += (ship_size-i)

#for row in range(board_size):
#    print " ".join(ai_board[row])
player_board = makeShip()
my_ship_alive = ship_size
for i in range(0, num_ships):
    my_ship_alive += (ship_size-i)

print ("Let's play Battleship!")
print_board()

while my_ship_alive and ai_ship_alive:
    #First my turn
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    while not exists(guess_row, guess_col, player_radar):
        print ("Sorry, that is not a valid shot")
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))
    # Legal Guess
    if ai_board[guess_row][guess_col] != OCEAN:
        ai_ship_alive -= 1
        if ai_ship_alive:
            print ("Admiral, we've hit the enemy ship!")
            player_radar[guess_row][guess_col] = HIT
        else:
            player_radar[guess_row][guess_col] = HIT
            print ("Congratulations! You sunk my battleship!")
            break
    else:
        print ("Admiral, we've missed the enemy battleship!")
        player_radar[guess_row][guess_col] = FIRE
    # Now ai's turn
    if not ai_hit:
        ai_guess_row = randint(0, board_size-1)
        ai_guess_col = randint(0, board_size-1)
        while ai_radar[ai_guess_row][ai_guess_col] != OCEAN:
            ai_guess_row = randint(0, board_size-1)
            ai_guess_col = randint(0, board_size-1)
        if player_board[ai_guess_row][ai_guess_col] != OCEAN: # ai-hit
            my_ship_alive -= 1
            ai_hit =1
            vert_ship = -1
            ai_hit_row = ai_guess_row
            ai_hit_col = ai_guess_col
            player_board[ai_hit_row][ai_hit_col] = HIT
            ai_radar[ai_hit_row][ai_hit_col] = HIT
            print ("Attenton Admiral! You have been hit!")
        else:
            player_board[ai_guess_row][ai_guess_col] = FIRE
            ai_radar[ai_guess_row][ai_guess_col] = FIRE
            print ("Good news! They've missed!")
    else: # ai_hit >=1, find next spot to shoot
        if vert_ship == -1:
            if exists(ai_hit_row+1, ai_hit_col, ai_radar):
                ai_guess_row = ai_hit_row+1
                ai_guess_col = ai_hit_col
            elif exists(ai_hit_row-1, ai_hit_col, ai_radar):
                ai_guess_row = ai_hit_row-1
                ai_guess_col = ai_hit_col
            elif exists(ai_hit_row, ai_hit_col-1, ai_radar):
                ai_guess_row = ai_hit_row
                ai_guess_col = ai_hit_col-1
            else:
                ai_guess_row = ai_hit_row
                ai_guess_col = ai_hit_col+1
        elif vert_ship:
            if exists(ai_hit_row+1, ai_hit_col, ai_radar):
                ai_guess_row = ai_hit_row+1
                ai_guess_col = ai_hit_col
            else:
                ai_guess_row = ai_hit_row-1
                ai_guess_col = ai_hit_col
                while not exists(ai_guess_row, ai_guess_col, ai_radar):
                    ai_guess_row += 1

        else:
            if exists(ai_guess_row, ai_hit_col-1, ai_radar):
                ai_guess_row = ai_hit_row
                ai_guess_col = ai_hit_col-1
            else:
                ai_guess_row = ai_hit_row
                ai_guess_col = ai_hit_col+1
                while not exists(ai_guess_row, ai_guess_col, ai_radar):
                    ai_guess_col -= 1

        # Update board on shot
        if player_board[ai_guess_row][ai_guess_col] != OCEAN:
            ai_hit += 1
            if ai_hit == 2:
                if ai_guess_col != ai_hit_col:
                        vert_ship = 0
                        print ("vert_ship:"), vert_ship
                else:
                    vert_ship = 1
                    print ("vert_ship:"), vert_ship
            player_board[ai_guess_row][ai_guess_col] = HIT
            ai_radar[ai_guess_row][ai_guess_col] = HIT
            my_ship_alive -= 1
            if my_ship_alive:
                print ("Attenton Admiral! You have been hit!")
            else:
                print ("I'm sorry sir, but we're going down")
                print_board()
                break
        else: # ai missed
            player_board[ai_guess_row][ai_guess_col] = FIRE
            ai_radar[ai_guess_row][ai_guess_col] = FIRE
            print ("Good news! They've missed!")

    print_board()
