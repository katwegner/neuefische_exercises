class tictactoe:
    def __init__(self):
        self.board = []
        self.player = 1
        self.field = []
        self.winner = 0
        self.icons = ['X', 'O']


    # create empty 2d array
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row) # doesn't seem to work


    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def check_if_full(self):
        for row in self.board:
            for column in row:
                if column == '-': # if there is at least one empty field
                    return False
        return True

    def check_winner(self):
        winning_hlines = [[[i,j] for j in range(3)] for i in range(3)]
        winning_vlines = [[[j,i] for j in range(3)] for i in range(3)]
        winning_dlines = [[[i,i] for i in range(3)], [[i,2-i] for i in range(3)]]
        winning_lines = winning_hlines + winning_vlines + winning_dlines

        for w in winning_lines:
            line = []
            for field in w:
                item = self.board[field[0]][field[1]]
                if item != '-':
                    line.append(item)
                if (len(line) == 3) and (len(set(line)) == 1):
                    return True

    def move(self):
        self.field = input('Player ' + str(self.player) + ': Choose a field (row column)\n').split(' ')
        self.field = [int(i) for i in self.field]


    def switch_player(self):
        self.player = (self.player - 2)*(-1) + 1

    def welcome_message(self):
        print("TIC TAC TOE \n To make your move, you'll need to enter a row and column, \n both as a number between 1 and 3. Rows and columns are separated by a space. \n")

    def start_game(self):
        self.welcome_message()
        start = input("Press ENTER to start the game.\n\n\n")
        if start != '':
            start = input("Press ENTER to start the game.\n\n\n")
        else:
            self.board = self.create_board() # board is not created
            self.show_board()
        # play
        while self.winner == 0:
            player_icon = self.icons[self.player-1]
            validity_check = 0
            while validity_check == 0:
                self.field = self.move(self.player)
                if self.board[self.field[0]-1][self.field[1]-1]  == '-': # if valid
                    validity_check = 1
                    self.board[self.field[0]-1][self.field[1]-1] = player_icon
                    self.show_board(self.board)
                else:
                    print('Field already taken, try again!')

            # check if there is a winner
            if self.check_winner(self.board): 
                self.winner = 1
                self.show_board(self.board)
                print("Player " + str(self.player) + " won. Congratulations!")
            # check if it's full
            if self.check_if_full(self.board):
                self.winner = 1
                self.show_board(self.board)
                print("It's a tie. Try again.")
            #switch player
            self.player = self.switch_player(self.player)

game = tictactoe()
game.start_game()