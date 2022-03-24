
# create empty 2d array
def create_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)
    return board

def check_if_full(board):
    for row in board:
        for column in row:
            if column == '-': # if there is at least one empty field
                return False
    return True


# Write a function to check whether a player has won or not.
def check_winner(board):
    winning_hlines = [[[i,j] for j in range(3)] for i in range(3)]
    winning_vlines = [[[j,i] for j in range(3)] for i in range(3)]
    winning_dlines = [[[i,i] for i in range(3)], [[i,2-i] for i in range(3)]]
    winning_lines = winning_hlines + winning_vlines + winning_dlines

    for w in winning_lines:
        line = []
        for field in w:
            item = board[field[0]][field[1]]
            if item != '-':
                line.append(item)
            if (len(line) == 3) and (len(set(line)) == 1):
                return True

def show_board(board):
    for row in board:
        for item in row:
            print(item, end=" ")
        print()

def move(player):
    field = input('Player ' + str(player) + ': Choose a field (row column)\n').split(' ')
    field = [int(i) for i in field]
    return field

def switch_player(player):
    return (player - 2)*(-1) + 1

def welcome_message():
    print("TIC TAC TOE \n To make your move, you'll need to enter a row and column, \n both as a number between 1 and 3. Rows and columns are separated by a space. \n")


def start_game():
    # random selection of starting sign

    # initiate player
    icons = ['X', 'O']
    winner = 0
    player = 1

    # start the game
    welcome_message()
    start = input("Press ENTER to start the game.\n\n\n")
    if start != '':
        start = input("Press ENTER to start the game.\n\n\n")
    else:
        board = create_board()
        show_board(board)

    # play
    while winner == 0:
        player_icon = icons[player-1]
        validity_check = 0
        while validity_check == 0:
            field = move(player)
            if board[field[0]-1][field[1]-1]  == '-': # if valid
                validity_check = 1
                board[field[0]-1][field[1]-1] = player_icon
                show_board(board)
            else:
                print('Field already taken, try again!')

        # check if there is a winner
        if check_winner(board): 
            winner = 1
            show_board(board)
            print("Player " + str(player) + " won. Congratulations!")
        # check if it's full
        if check_if_full(board):
            winner = 1
            show_board(board)
            print("It's a tie. Try again.")
        #switch player
        player = switch_player(player)

start_game()