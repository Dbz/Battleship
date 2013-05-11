from random import randint

TURNS = 4
OCEAN = "O"
FIRE = "X"
HIT = "*"
board = []
ai_board = []
is_vertical = -1 # Determines the verticality in makeShip()

def print_board():
    for row in range(board_size):
        print " ".join(board[row]), "||" , " ".join(my_board[row])

def random_row(board):
    if is_vertical:
        return randint(0, board_size - ship_size - 1)
    else:
        return randint(0, board_size -1)
def random_col(board):
    if is_vertical:
        return randint(0, board_size - 1)
    else:
        return randint(ship_size, board_size -1)
def makeShip():
    temp_board = []
    is_vertical = randint(0, 1) # vertical ship if true
    for x in range(board_size):
        temp_board.append([OCEAN] * board_size)
    ship_row = random_row(board)
    ship_col = random_col(board)

    if is_vertical:
        temp_board[ship_row][ship_col] = "^"
        temp_board[ship_row+ship_size-1][ship_col] = "v"
        for p in range(ship_size -2):
            temp_board[ship_row+p+1][ship_col] = "+"
    else:
        temp_board[ship_row][ship_col] = ">"
        temp_board[ship_row][ship_col-ship_size+1] = "<"
        for p in range(ship_size -2):
            temp_board[ship_row][ship_col-p-1] = "="
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

def find_shot():
    if(vert == -1):
        if exists(ai_hit_row+1, ai_hit_col, my_board):
            ai_guess_row = ai_hit_row+1
            ai_guess_col = ai_hit_col
        elif exists(ai_hit_row-1, ai_hit_col, my_board):
            ai_guess_row = ai_hit_row-1
            ai_guess_col = ai_hit_col
        elif exists(ai_hit_row, ai_hit_col-1, my_board):
            ai_guess_row = ai_hit_row
            ai_guess_col = ai_hit_col-1
        else:
            ai_guess_row = ai_hit_row
            ai_guess_col = ai_hit_col+1
    elif vert:
        if exists(ai_hit_row+1, ai_hit_col, my_board):
            ai_guess_row = ai_hit_row+1
            ai_guess_col = ai_hit_col
        else:
            ai_guess_row = ai_hit_row-1
            ai_guess_col = ai_hit_col
    else:
        if exists(ai_guess_row, ai_hit_col-1, my_board):
            ai_guess_row = ai_hit_row
            ai_guess_col = ai_hit_col-1
        else:
            ai_guess_row = ai_hit_row
            ai_guess_col = ai_hit_col+1
    # Update board on shot
    if my_board[ai_guess_row][ai_guess_col] != OCEAN:
                if ai_guess_col != ai_hit_col:
                    vert_ship = 0
                my_board[ai_guess_row][ai_guess_col] = HIT
                enemy_board[ai_guess_row][ai_guess_col] = HIT
    else:
        my_board[ai_guess_row][ai_guess_col] = FIRE
        enemy_board[ai_guess_row][ai_guess_col] = FIRE
#
#
#

# Make the boards (and set ship_size)
board_size = int(raw_input("Please input a board size"))
for x in range(board_size):
        board.append([OCEAN] * int(board_size))
        ai_board.append([OCEAN] * int(board_size))
ship_size = -1
while ship_size > board_size or ship_size < 0:
    ship_size = int(raw_input("Please input a ship size"))

enemy_board = makeShip()
enemy_ship_alive = ship_size;
#
#for row in range(board_size):
#    print " ".join(enemy_board[row])
my_board = makeShip();
my_ship_alive = ship_size;

ai_hit = 0 #has the ai hit me?
vert_ship = -1 #ai var is_my_ship_vertical

print "Let's play Battleship!"
print_board()

while my_ship_alive and enemy_ship_alive:
    #First my turn
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    while not exists(guess_row, guess_col, board):
        print "Sorry, that is not a valid shot"
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))
    # Legal Guess
    if enemy_board[guess_row][guess_col] != OCEAN:
        enemy_ship_alive -= 1;
        if enemy_ship_alive:
            print "Admiral, we've hit the enemy ship!"
            board[guess_row][guess_col] = HIT
        else:
            print "Congratulations! You sunk my battleship!"
            break
    else:
        print "Admiral, we've missed the enemy battleship!"
        board[guess_row][guess_col] = FIRE
    # Now ai's turn
    ai_guess_row = randint(0, board_size-1)
    ai_guess_col = randint(0, board_size-1)
    while board[ai_guess_row][ai_guess_col] != OCEAN:
        ai_guess_row = randint(0, board_size-1)
        ai_guess_col = randint(0, board_size-1)
    # Legal Guess
    if my_board[ai_guess_row][ai_guess_col] != OCEAN: # ai-hit
        my_ship_alive -= 1
        if not ai_hit: # First hit
            ai_hit =1
            vert = -1
            ai_hit_row = ai_guess_row
            ai_hit_col = ai_guess_col
        else:
            find_shot()

        if my_ship_alive:
            print "Attenton Admiral! You have been hit!"
            board[guess_row][guess_col] = HIT
        else:
            print "I'm sorry sir, but we're going down"
            break
    else: #ai-miss
        my_board[ai_guess_row][ai_guess_col] = FIRE
        print "Good news! They've missed!"
    print_board()

