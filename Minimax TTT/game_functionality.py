import random

class GameFunctionality:
    def __init__(self):
        '''
        Initialize some basic values like
            -The game board -> this table holds all the players pawns.
            -The players_turn which indicates whos turn it is.

            This method is also checking if the computer plays first. If it is then
            it calls the first minimax algorithm in order for the game to begin.
        '''
        self.player_turn = True if(random.randint(0, 1) == 0) else False
        self.board = [[-1 for _ in range(3)] for _ in range(3)]

        if(self.player_turn == False):
            self.best_move()

    def entry(self, row, col, player):
        '''
        This method is called whenever someone makes a move. It updates the players_turn
        and the board of the game. It also calls the minimax algorithm if it is the
        computer turn.

        param_1: row of the pawn --int
        param_2: column of the pawn --int
        param_3: the players --int 0, 1
        '''
        if(self.board[row][col] == -1):
            self.board[row][col] = player
            self.player_turn = not self.player_turn

        # Make the computer play again..
        if(self.player_turn == False and ((self.board[0].count(-1) + self.board[1].count(-1) + self.board[2].count(-1)) != 0)):
            self.best_move()

    def player_won(self):
        '''
        This function stop the hole program if any of the 
        players won the game.

        return: 1, 0, -1, -2
        '''
        # Rows and Columns
        for i in range(3):
            if(self.board[i][0] == 0 and self.board[i][1] == 0 and self.board[i][2] == 0):
                return 0
            elif(self.board[i][0] == 1 and self.board[i][1] == 1 and self.board[i][2] == 1):
                return 1

            if(self.board[0][i] == 0 and self.board[1][i] == 0 and self.board[2][i] == 0):
                return 0
            elif(self.board[0][i] == 1 and self.board[1][i] == 1 and self.board[2][i] == 1):
                return 1

        # Diagonaly
        if(self.board[0][0] == 0 and self.board[1][1] == 0 and self.board[2][2] == 0):
            return 0
        elif(self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1):
            return 1

        if(self.board[0][2] == 0 and self.board[1][1] == 0 and self.board[2][0] == 0):
            return 0
        elif(self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1):
            return 1

        # Tie
        if((self.board[0].count(-1) + self.board[1].count(-1) + self.board[2].count(-1)) == 0):
            return -2

        # No winner yet..
        return -1

    def best_move(self):
        '''
        This method just calls the minimax algorithm for every single move that there
        is in the board.
            -At the it calls the entry method in order to enter the best move on the
            game' board.
        '''
        best_score = -1000000
        x1, x2 = -1, -1
        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == -1):
                    self.board[i][j] = 0
                    score = self.minimax(0, False)
                    self.board[i][j] = -1
                    if(score > best_score):
                        best_score = score
                        x1 = i
                        x2 = j

        self.entry(x1, x2, 0)

    def minimax(self, depth, isMax):
        '''
        This method plays role of the computers brain. It is the minimax algorithm,
        whenever it find the best position to place its pawn it calls the entry method.
        '''
        scores = {
            1: -10,
            0: 10,
            -2: 0
        }

        response = self.player_won()
        if(response != -1):
            return scores[response]

        if(isMax == True):
            best_score = -1000000
            for i in range(3):
                for j in range(3):
                    if(self.board[i][j] == -1):
                        self.board[i][j] = 0
                        score = self.minimax(depth+1, False)
                        self.board[i][j] = -1
                        best_score = max(score, best_score)
            return best_score
        
        best_score = 1000000
        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == -1):
                    self.board[i][j] = 1
                    score = self.minimax(depth+1, True)
                    self.board[i][j] = -1
                    best_score = min(score, best_score)
        return best_score