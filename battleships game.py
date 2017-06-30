# add multiple ships horizontally and vertically and ensure that they don't overlap (4 singles, 3 doubles, 2 triples, 1 quadruple)
# make it two-player game, which will require 2 boards

from random import randint

player = "User"
board = []
board_size = 10

ships = {"Aircraft Carrier":5,
            "Battleship":4,
            "Submarine":3,
            "Destroyer":3,
            "Patrol Boat":2}

def print_board(player, board): # to print joined board
    print("Here is " + player + "'s board")
    for row in board:
        print(" ".join(row))

def switch_user(player): # to switch users
    if player == "User":
        player = "Computer"
    elif player == "Computer":
        player = "User"
    else:
        print("Error with user switching")

for x in range(0, board_size): # to create a board
    board.append(["O"] * board_size)

print_board(player,board)

def random_row(board): # generate random row
    return randint(0, len(board) - 1)

def random_col(board): # generate random column
    return randint(0, len(board[0]) - 1)

def user_places_ships(board, ships): # user choses to place its ships by providing starting co-ordinate and direction. There a BUG!!! If you don't put right co-ordinates first time round, the code will generate an error.
    for ship in ships:
        valid = False
        while(not valid):
            user_input_coordinates = input("Please enter row & column number for your " + str(ship) + ", which is " + str(ships[ship]) + "-cells long (row, column).")
            ship_row, ship_col = user_input_coordinates.split(",")
            ship_row = int(ship_row)
            ship_col = int(ship_col)
            user_input_dir = input("Please enter direction for your " + str(ship) + ", which is " + str(ships[ship]) + "-cells long (h for horizontal or v for vertical).")
            valid = validate_coordinates(board, ships[ship], ship_row, ship_col, user_input_dir)
            if not valid:
                print("The ship coordinates either outside of" , board_size, "X" , board_size, "range, overlap with or too close to another ship.")
        place_ship(board, ships[ship], ship_row, ship_col, user_input_dir)
    print("You have finished placing all your ships.")

def validate_coordinates(board, ship_len, row, col, dir): # validates if the co-ordinates entered by a player are within the board and don't overlap with other ships
    if dir == "h" or dir == "H":
        for x in range(ship_len):
            if row-1 > board_size or col-1+x > board_size:
                return False
            elif row-1 < 0 or col-1+x < 0:
                return False
            elif board[row-1][col-1+x] == "S":
                return False
    elif dir == "v" or dir == "V":
        for x in range(ship_len):
            if row-1+x > board_size or col-1 > board_size:
                return False
            elif row-1+x < 0 or col-1 < 0:
                return False
            elif board[row-1+x][col-1] == "S":
                return False
    return True

def place_ship(board, ship_len, row, col, dir): # to actually place ships and mark them as "S"
    if dir == "h" or dir == "H":
        for x in range(ship_len):
            board[row-1][col-1+x] = "S"
    elif dir == "v" or dir == "V":
        for x in range(ship_len):
            board[row-1+x][col-1] = "S"
    else:
        print("Error with direction.")
    print_board(player,board)

user_places_ships(board,ships)






# def player_turn(a): # to identify which player should go
#     if a % 2 == 0:
#         print("Player 2 turn")
#     else:
#         print("Player 1 turn")
#         print(player)
#
#
# ship_row = random_row(board) # PC picks random row & column for single-cell ship. Then prints it
# ship_col = random_col(board)
# print(ship_row + 1)
# print(ship_col + 1)
#
# gameover = "N" # used to end the game
# turn = 1 # used to track player turns
#
# while gameover == "N": # loop statement for turns.
#
#     player_turn(turn) # used to track player turns
#
#     guess_row = int(input("Guess Row:")) - 1 # human to guess a row & column
#     guess_col = int(input("Guess Col:")) - 1
#
#     if guess_row == ship_row and guess_col == ship_col: # checks if you guessed cell correctly
#         print("Congratulations! You sank my battleship!")
#         gameover = "Y"
#         break
#     else:
#         if guess_row not in range(5) or guess_col not in range(5): # checks if selected cell is within the board
#             print("Oops, that's not even in the ocean.")
#         elif board[guess_row][guess_col] == "X":
#             print("You guessed that one already.")
#         else:
#             print("You missed my battleship!")
#             board[guess_row][guess_col] = "X"
#
#         print_board(board)
#
#     turn = turn + 1 # used to track player turns
#
#     if gameover == "Y":
#         print("Game over!")
