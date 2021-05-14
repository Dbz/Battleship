from random import randint
import copy
#Constants and globals
OCEAN = "O"
FIRE = "X"
HIT = "*"
SIZE = 10
SHIPS = [5, 4, 3, 3, 2]
#globals
orientation = -1 # Stores the hit ship orientation. Determined on second hit
total_hits = [] # Stores the ship number every time AI hits a ship while ship is afloat
miss = 1 # Stores whether last AI shot was a miss
# Player variables
player_alive = 17 # -1 every time a ship is hit
player_radar = []
player_board = []
# AI variables
ai_alive = 17
ai_radar = []
ai_board = []
ship_position = [] # Stores the first hit of ships which will be eliminated [row, col]
ship_length = [] # Stores the length of ship on first hit

#Set up variables
SEA = [] # Blank Board
for x in range(SIZE):
    SEA.append([OCEAN] * SIZE)

#Functions
def print_board():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #print(numbers.join(""))
    print("  0 1 2 3 4 5 6 7 8 9 || 0 1 2 3 4 5 6 7 8 9")
    i = 0
    for row in range(SIZE):
        print(i, " ".join(player_radar[row]), "||" , " ".join(player_board[row]))
        i += 1

def random_row(is_vertical, size):
    if is_vertical:
        return randint(0, SIZE - size)
    else:
        return randint(0, SIZE -1)

def random_col(is_vertical, size):
    if is_vertical:
        return randint(0, SIZE - 1)
    else:
        return randint(size-1, SIZE -1)

def is_ocean(row, col, b): # true if ocean
    if row < 0 or row >= SIZE:
        return 0
    elif col < 0 or col >= SIZE:
        return 0
    if b[row][col] == OCEAN:
        return 1
    else:
        return 0

def is_oceanin(row,col,b):
    if type(row) is not int or type(col) is not int:
        return 0
    if row < 0 or row >= SIZE:
        return 0
    elif col < 0 or col >= SIZE:
        return 0
    if b[row][col] == OCEAN:
        return 1
    else:
        return 0


def make_ship(size, board, set_ship = None):
    # Find an unoccupied spot, then place ship on board
    # Put set_ship on ship_number_board if set_ship
    is_vertical = randint(0, 1) # vertical ship if true
    occupied = True
    while(occupied):
        occupied = False
        ship_row = random_row(is_vertical, size)
        ship_col = random_col(is_vertical, size)
        if is_vertical:
            for p in range(size):
                if not is_ocean(ship_row+p, ship_col, board):
                    occupied = True
        else:
            for p in range(size):
                if not is_ocean(ship_row, ship_col-p, board):
                    occupied = True
    #Place ship on boards
    if is_vertical:
        board[ship_row][ship_col] = "^"
        board[ship_row+size-1][ship_col] = "v"
        if set_ship != None:
            number_board[ship_row][ship_col] = set_ship
            number_board[ship_row+size-1][ship_col] = set_ship
        for p in range(size -2):
            board[ship_row+p+1][ship_col] = "+"
            if set_ship != None:
                number_board[ship_row+p+1][ship_col] = set_ship
    else:
        board[ship_row][ship_col] = ">"
        board[ship_row][ship_col-size+1] = "<"
        if set_ship != None:
            number_board[ship_row][ship_col] = set_ship
            number_board[ship_row][ship_col-size+1] = set_ship
        for p in range(size -2):
            board[ship_row][ship_col-p-1] = "+"
            if set_ship != None:
                number_board[ship_row][ship_col-p-1] = set_ship
    return board
def ship_number(r, c):
    # Returns -1 if not found
    if is_ocean(r, c, number_board):
        return -1
    #print("ship_number() returning: ", str(SHIPS[number_board[r][c]]))
    return SHIPS[number_board[r][c]]
def ship_sunk(): # true if ship sunk
    #print("Total Hits: ", str(total_hits.count(ship_length[0]), ":", str(ship_length[2]))
    #for item in number_board:
    #    print(item[0], ' '.join(map(str, item[1:])))
    if total_hits.count(total_hits[0]) == ship_length[0]:
        return 1
    return 0


# Make the boards
player_radar = copy.deepcopy(SEA)
player_board = copy.deepcopy(SEA)
ai_radar = copy.deepcopy(SEA)
ai_board = copy.deepcopy(SEA)
number_board = copy.deepcopy(SEA)

for x in range(len(SHIPS)):
    player_board = make_ship(SHIPS[x], player_board, x)
    ai_board = make_ship(SHIPS[x], ai_board)

print("Let's play Battleship!")
print_board()
while player_alive and ai_alive:
    # player turn
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    while not is_oceanin(guess_row, guess_col, player_radar):
        print("Sorry, that is not a valid shot")
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))
    # Legal Guess
    if ai_board[guess_row][guess_col] != OCEAN:
        ai_alive -= 1
        if ai_alive:
            print("Admiral, we've hit the enemy ship!")
            player_radar[guess_row][guess_col] = HIT
        else:
            player_radar[guess_row][guess_col] = HIT
            print("Congratulations! You sunk my battleship!")
            break
    else:
        print("Admiral, we've missed the enemy battleship!")
        player_radar[guess_row][guess_col] = FIRE
    # AI turn
    print("target orientation: ", orientation)
    if not len(ship_length): # No current targets
        #print("No Current Targets")
        second_shot = 0
        ai_guess_row = randint(0, SIZE-1)
        ai_guess_col = randint(0, SIZE-1)
        while not is_ocean(ai_guess_row, ai_guess_col, ai_radar):
            ai_guess_row = randint(0, SIZE-1)
            ai_guess_col = randint(0, SIZE-1)
        if not is_ocean(ai_guess_row, ai_guess_col, player_board): # AI hit
            miss = 0
            player_alive -= 1
            #print("Hit ship length: ", ship_number(ai_guess_row, ai_guess_col))
            ship_length.append((ship_number(ai_guess_row, ai_guess_col)))
            #print("ship_position length: ", str(len(ship_position)))
            ship_position.extend([ai_guess_row, ai_guess_col])
            #print("ship_position length: ", str(len(ship_position)))
            orientation = -1
            player_board[ai_guess_row][ai_guess_col] = HIT
            ai_radar[ai_guess_row][ai_guess_col] = HIT
            total_hits.append(number_board[ai_guess_row][ai_guess_col])
            print(("Attenton Admiral! You have been hit!"))
        else:
            miss = 1
            player_board[ai_guess_row][ai_guess_col] = FIRE
            ai_radar[ai_guess_row][ai_guess_col] = FIRE
            print("Good news! They've missed!")
    else: # Find next spot to shoot on ship
        #print("Current Targets: ", " ".join(map(str, ship_length)),":", " ".join(map(str,total_hits)))
        #print("Last shot was a miss: ", miss)
        if orientation == -1: # shot-test for orientation of hit ship
            #ship_position[ swapped for ai_hit_
            print("Ship has no orientation")
            if is_ocean(ship_position[0]+1, ship_position[1], ai_radar):
                ai_guess_row = ship_position[0]+1
                ai_guess_col = ship_position[1]
            elif is_ocean(ship_position[0]-1, ship_position[1], ai_radar):
                ai_guess_row = ship_position[0]-1
                ai_guess_col = ship_position[1]
            elif is_ocean(ship_position[0], ship_position[1]-1, ai_radar):
                ai_guess_row = ship_position[0]
                ai_guess_col = ship_position[1]-1
            else:
                ai_guess_row = ship_position[0]
                ai_guess_col = ship_position[1]+1
        elif orientation: # Shoot at verticle ship
            #print("Previous Guess: ", ai_guess_row, ":", ai_guess_col)
            for item in ai_radar:
                print(item[0], ' '.join(map(str, item[1:])))
            if is_ocean(ai_guess_row+1, ai_guess_col, ai_radar) and not miss:
                ai_guess_row += 1
            else:
                #print("Adjusting guess to lower row number")
                ai_guess_row -= 1

                while not is_ocean(ai_guess_row, ai_guess_col, ai_radar): # not is important here
                    ai_guess_row -= 1
                #print("New Guess: ", ai_guess_row, ":", ai_guess_col)
        else: # Shoot at horizontal ship
            #print("Previous Guess: ", ai_guess_row, ":", ai_guess_col)
            for item in ai_radar:
                print(item[0], ' '.join(map(str, item[1:])))
            if is_ocean(ai_guess_row, ai_guess_col-1, ai_radar) and not miss:
                ai_guess_col = ai_guess_col-1
            else:
                #print("Adjusting guess to higher col number")
                ai_guess_col = ai_guess_col+1
                while not is_ocean(ai_guess_row, ai_guess_col, ai_radar):
                    ai_guess_col += 1
                #print("New Guess: ", ai_guess_row, ":", ai_guess_col)
        # Set boards after shots
        if not is_ocean(ai_guess_row, ai_guess_col, player_board):

            #number_board[ai_guess_row][ai_guess_col] = OCEAN
            #print("Setting Board: ", ai_guess_row, ":", ai_guess_col)
            player_board[ai_guess_row][ai_guess_col] = HIT
            ai_radar[ai_guess_row][ai_guess_col] = HIT
            total_hits.append(number_board[ai_guess_row][ai_guess_col])
            #ship_position.extend([ai_guess_row, ai_guess_col])
            player_alive -= 1

            #if second_shot: # set orientation
            #print("DEBUG: ", total_hits.count(total_hits[0]), ship_number(ai_guess_row, ai_guess_col), ship_number(ship_position[0], ship_position[1]))
            if total_hits.count(total_hits[0]) == 2 and ship_number(ai_guess_row, ai_guess_col) == ship_number(ship_position[0], ship_position[1]):
                if ai_guess_col != ship_position[1]:
                    orientation = 0
                else:
                    orientation = 1
                print("New Orientation: ", orientation)
            elif total_hits[0] != number_board[ai_guess_row][ai_guess_col]: # Other ship was shot
                ship_length.append((ship_number(ai_guess_row, ai_guess_col)))
                ship_position.extend([ai_guess_row, ai_guess_col])
            if player_alive:
                miss = 0
                print("Attenton Admiral! You have been hit!")
            else:
                print("I'm sorry sir, but we're going down")
                print_board()
                break
        else: # AI missed
            #print("DEBUG: r,c: ", ai_guess_row, ", ", ai_guess_col)
            miss = 1
            player_board[ai_guess_row][ai_guess_col] = FIRE
            ai_radar[ai_guess_row][ai_guess_col] = FIRE
            print("Good news! They've missed!")
        if ship_sunk(): # Reset variables
                #print("Ship sunk")
                orientation = -1
                ship_position.pop(0)
                ship_position.pop(0)
                ship_length.pop(0)

                t = total_hits[0]
                for x in range(total_hits.count(t)):
                    total_hits.remove(t)

                #print("Targets after sinking: ", " ".join(map(str, ship_length)),":", " ".join(map(str,total_hits)))
                if len(ship_length) != 0:
                    miss = 0
                else:
                    miss = 1
                #print("ship_position list: ", " ".join(map(str, ship_position)))
    print_board()
