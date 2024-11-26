import random

class Connect4:
    def __init__(self, width, height):
        ''' Create a new Connect4 board with the given size '''
        
        # configure the basics
        self.width = width
        self.height = height
        self.board = []
        
        # Note: We take row 0 to be the top of the board
        # actually create the board
        for row in range(self.height):
            boardRow = []
            for col in range(self.width):
                boardRow.append(' ')
            self.board.append(boardRow)
        
    def __str__(self):
        ''' Returns a representation of the current state of the board'''
        
        # output contents of rows and columns
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # row begins with column separator
            for col in range( self.width ):
                s += self.board[row][col] + '|' # add this cell and a separator
            s += '\n' # end of the row

        # add the column labels under the columns
        s += '--'*self.width + '-\n'
        for col in range(self.width):
            s += ' ' + str(col % 10)
        s += '\n'
        return s

    def is_legal_move(self, col):
        ''' Returns True if col exists and has space, otherwise False '''
        try: # Checks if col is accessed correctly, if not, returns False
            if self.board[0][col] == " " and col >= 0: # Checks for if the col has space
                return True
        except IndexError:
            print("Index Out of Range")
        return False

    def add_move(self, col, player):
        ''' Makes a move in column col for designated player, 
            returning True if move was legal, or False otherwise '''
        if self.is_legal_move(col) is True:
            for i in range((self.height - 1), -1, -1): # Starts from highest index, goes to bottom
                if self.board[i][col] == " ": # If it passes this statement, adds players token, otherwise False
                    self.board[i][col] = player
                    return True
        return False
 
    def del_move(self, col):
        ''' Removes the top token in specified column. 
            If column is empty or nonexistent, do nothing. '''
        for i in range(self.height): # Loops from lowest index and changes top token to space if any
            if self.board[i][col] != " ":
                self.board[i][col] = " "
                break
    
    def clear(self):
        ''' Clears the game board '''
        for i in range(self.height): # Loops through each row
            for j in range(self.width): # Loops through each column
                if self.board[i][j] != " ":
                    self.board[i][j] = " "
    
    def is_full(self):
        ''' Return True if all spaces in the board are occupied, otherwise False '''
        for i in range(self.width): # Will return True if everything in top row is full
            if self.is_legal_move(i) is True:
                return False
        return True

    def is_win_for(self, player):
        ''' Return True if the designated player has won, otherwise False '''
        # check for horizontal wins
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.board[row][col] == player and \
                   self.board[row][col+1] == player and \
                   self.board[row][col+2] == player and \
                   self.board[row][col+3] == player:
                    return True
        
        # Check for other winning conditions
        
        # A Check for vertical wins
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.board[row][col] == player and \
                   self.board[row+1][col] == player and \
                   self.board[row+2][col] == player and \
                   self.board[row+3][col] == player:
                    return True
        
        # A check for diagonal wins
        
        # Checks diagonal win from left to right
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.board[row+3][col] == player and \
                   self.board[row+2][col+1] == player and \
                   self.board[row+1][col+2] == player and \
                   self.board[row][col+3] == player:
                    return True
        
        # Checks diagonal win from right to left
        for row in range(self.height - 3):
            for col in range((self.width - 3), -1, -1):
                if self.board[row+3][col+2] == player and \
                   self.board[row+2][col+1] == player and \
                   self.board[row+1][col] == player and \
                   self.board[row][col-1] == player:
                    return True
                    # (row), (col-1), (row+1), (col), (row+2), (col+1), (row+3), (col+2)
        return False
    
    def play_game(self):
        ''' plays a game of connect four by asking for player moves, 
            checking for wins, etc '''
        players_turn = "X" # We can import random to make X or O go first randomly
        n = 0 # Using this value as a way to break out of the loop when theres a win or board is full
        while n == 0:
            print(str(self))
            player_move_col = input("Input Column: ")
            player_move_col = int(player_move_col)
            if self.is_legal_move(player_move_col) == True:
                self.add_move(player_move_col, players_turn)
                if self.is_win_for(players_turn) == True:
                    print(str(self))
                    print(players_turn + " has won!\n")
                    n += 1
                elif self.is_full() == True:
                    print(str(self))
                    print("Tied")
                    n += 1
                else:
                    if players_turn == "X":
                        players_turn = "O"
                    else:
                        players_turn = "X"
        
        while n == 1:
            replay_game = input("Another game? (Yes or no): ").strip().lower()
            if replay_game == "yes":
                self.clear()
                self.play_game()
            elif replay_game == "no":
                break
    
    def play_game_with(self, AI):
        ''' Plays a game of Connect 4 with the AI that was created
            in the Player class'''
        players_turn = "X"
        
        n = 0 # Using this value as a way to break out of the loop when theres a win or board is full
        while n == 0:
            print(str(self))
            if players_turn == "X":
                player_move_col = input("Input Column: ")
                player_move_col = int(player_move_col)
            elif players_turn == "O":
                player_move_col = AI.next_move(self)
                print(f"AI picked: {player_move_col}")
                
            if self.is_legal_move(player_move_col) == True:
                self.add_move(player_move_col, players_turn)
                if self.is_win_for(players_turn) == True:
                    print(str(self))
                    print(players_turn + " has won!\n")
                    n += 1
                elif self.is_full() == True:
                    print(str(self))
                    print("Tied")
                    n += 1
                else:
                    if players_turn == "X":
                        players_turn = "O"
                    else:
                        players_turn = "X"

class Player:
    def __init__(self, player, tiebreaker, ply):
        self.player = player # O
        self.tiebreaker = tiebreaker
        self.ply = ply
    
    def __str__(self):
        return f"AI Token: {self.player} using {self.tiebreaker}" + \
            f" tiebreaking at {self.ply} ply"
    
    def next_move(self, board: Connect4):
        ''' Gets the list of column scores, and decides the best
            move based off the tiebreaker variable '''
        check_score = self._scores_for(board, self.player, self.ply) # Fix
        print(check_score)
        highest_score_checker = max(check_score)
        high_scores = []
        
        for column in range(len(check_score)):
            if check_score[column] == highest_score_checker:
                high_scores.append(column)
        
        if self.tiebreaker == "Left":
            return high_scores[0]
        elif self.tiebreaker == "Right":
            return high_scores[-1]
        elif self.tiebreaker == "Random":
            return random.choice(high_scores)

    def _scores_for(self, board: Connect4, player, ply):
        ''' Returns a list of column scores for player,
            examining board with depth ply'''
        
        scorred_columns = [0] * board.width # Creates a list to store values # Fix
        if player == "O": # Switching to our opponent, odd is AI, even is opponent
            opponent = "X"
        else:
            opponent = "O"

        for column in range(board.width):
            
            if board.is_legal_move(column) == True:
                
                board.add_move(column, player)
                
                if board.is_win_for(player) == True: 
                        scorred_columns[column] = 100
                elif ply > 1:    
                    opponents_score = self._scores_for(board, opponent, (ply - 1))
                    # if 100 in opponents_score:
                    #     scorred_columns[column] = 0
                    # elif 0 in opponents_score:
                    #     scorred_columns[column] = 100
                    # else:
                    #     scorred_columns[column] = 50
                    best_opponent_score = max(opponents_score)  # Get the best score for the opponent
                    scorred_columns[column] = 100 - best_opponent_score
                
                else:
                    scorred_columns[column] = 50
            
                board.del_move(column)

            else:
                scorred_columns[column] = -1

            
        #print(scorred_columns)
        return scorred_columns

def main():
    board = Connect4(7,6)
    my_player = Player("O", "Random", 6)
    board.play_game_with(my_player)

if __name__ == '__main__':
    main()
