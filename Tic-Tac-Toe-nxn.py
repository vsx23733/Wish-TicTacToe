import numpy as np
import time

class Game():
    def __init__(self, n, board):
        """Initialize the Game matrix values Different values so as to not have the winning game in the beginning"""
        self.n = n
        self.board = board
        rows = []
        for _ in range(self.n):
            rows.append([j for j in range(self.n)])

        self.game_matrix = np.array([rows], np.int32)
        self.flattened_game_matrix = self.game_matrix.flatten()
        self.win_state = False

    def get_player_move(self, player_line_input_id, player_column_input_id, player_symbol):
        """Function to get the player move"""

        i = int(player_line_input_id)
        j = int(player_column_input_id)
        player_move = player_symbol
        return i, j, player_move

    def apply_player_move(self, i, j, player_move):

        """Function which applies the player move to the game matrix"""

        self.game_matrix[i][j] = player_move

    def is_win(self, token):
        
        """Function which checks the winning condition."""

        for r in self.board.board:
            if all([t == token for t in r]):
                return True
        for c in range(self.board.n):
            col_array =  [row[c] for row in self.board.board]
            if all([t == token for t in col_array]):
                return True
            
        diag = [self.board.board[i][j] for i in range(self.board.n) for j in range(self.board.n) if i == j]

        if all(t == token for t in diag):
            return True
        
        return False


    def going_through_the_game(self):

        """Going through the game"""

        mes_1 = '''Welcome to the Wish TIC-TAC-TOE!\n'''
        mes_2 = '''Enjoy this shitty game 😂😂\n'''

        for letter in mes_1:
            print(letter, end='', flush=True)
            time.sleep(0.1)

        for letter in mes_2:
            print(letter, end='', flush=True)
            time.sleep(0.1)

        player_1 = Player(symbol="O")
        player_2 = Player(symbol="X")
        game_board = self.board

        game_board.view()
        current_player = player_1

        while True:

            current_player_line_input, current_player_column_input, current_player_move = current_player.move(game_board)
            i, j, move = self.get_player_move(current_player_line_input, current_player_column_input, current_player_move)
            game_board.update(i, j, move)
            game_board.view()

            if self.is_win(current_player.symbol):
                mes = f'''Game's over!! {current_player.name} is the winner!\n'''
                for letter in mes:
                    print(letter, end='', flush=True)
                    time.sleep(0.1)

                game_board.view()
                break

            if game_board.is_full():
                print("This is a draw! No winner.")
                break

            current_player = player_2 if current_player == player_1 else player_1


class Player():

    id = 0

    def __init__(self, symbol):

        """Initializing player"""

        Player.id += 1
        self.name = self.get_input_player_id()
        self.symbol = symbol

    def get_input_player_id(self):
        name = input(f"Enter your name, Player {self.get_instance_count()} : ")
        return name

    def move(self, board):
        
        """Function which allows the player to move"""
        
        while True:
            try:
                line_input = int(input(f"{self.name} Enter the row number (0-{board.n - 1}) : "))
                column_input = int(input(f"{self.name}Enter the column number (0-{board.n - 1}) : "))

                if line_input in range(board.n) and column_input in range(board.n):
                    if board.is_empty(line_input, column_input):
                        return line_input, column_input, self.symbol
                    else:
                        print("Position already occupied. Try again.")
                else:
                    print("Invalid input. Please enter numbers between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

    @classmethod
    def get_instance_count(cls):
        return cls.id

class Board():
    def __init__(self, n):
        self.n = n
        self.board = [["-" for _ in range(self.n)] for _ in range(self.n)]

    def view(self):

        for i in range(self.n):
            print(f"{i} | ", end='')
            print(*self.board[i], sep=' | ', end=f"")
            print(" |\n")
        
        print("   ", end="")
        print('   '.join([str(i) for i in range(self.n)]))
        pass

        """for row in self.board:
            print(' '.join(row))"""

    def update(self, i, j, symbol):
        if self.board[i][j] == '-':
            self.board[i][j] = symbol
        else:
            print("Position already occupied. You can't do that.")

    def is_full(self):
        for row in self.board:
            if '-' in row:
                return False
        return True

    def is_empty(self, i, j):
        return self.board[i][j] == '-'

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.board])

def main():

    class InputRowError(Exception):
        def __init__(self, n):
            self.n = n
            self.message = f"Invalid dimensions: n = {n}. Rows, Columns must be > 3."
            super().__init__(self.message)

    try:
        n = int(input("Enter the number of rows (n > 3): "))

        if n <= 3 :
            raise InputRowError(n)

    except InputRowError as e:
        print(e.message)
        exit()
    except Exception as i:
        print("An error occured")
        exit()

    BOARD = Board(n)
    TIC_TAC_TOE = Game(n, BOARD)
    TIC_TAC_TOE.going_through_the_game()


if __name__ == "__main__":
    main()
