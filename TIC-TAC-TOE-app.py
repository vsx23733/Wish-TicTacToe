import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox
from PyQt5.QtCore import QSize

class TicTacToeApp(QWidget):
    def __init__(self, n=3):
        super().__init__()

        self.n = n  
        self.board = [["-" for _ in range(self.n)] for _ in range(self.n)]
        self.current_player = "X"  

        self.init_ui()

    def init_ui(self):

        """Initialize the UI with a grid of buttons."""

        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 400, 400)

        self.setStyleSheet(r"""
            QWidget {
                background-repeat: no-repeat;
                background-position: center;
            }
        """)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        # Creating buttons for each cell in the grid
        self.buttons = [[None for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                button = QPushButton("")
                button.setFixedSize(QSize(100, 100))
                button.setStyleSheet(r"""
                    QPushButton {
                        font-size: 24px; 
                        font-weight: bold; 
                        color: #333; 
                        background-color: rgba(255, 255, 255, 0.8);  /* semi-transparent */
                        border: 2px solid #888;
                        border-radius: 10px;
                    }
                    QPushButton:hover {
                        background-color: #ADD8E6;
                    }
                """)
                button.clicked.connect(lambda _, x=i, y=j: self.on_button_click(x, y))
                self.grid_layout.addWidget(button, i, j)
                self.buttons[i][j] = button

        self.show()

    def on_button_click(self, i, j):

        """Handle button click event."""

        if self.board[i][j] == "-":

            self.board[i][j] = self.current_player
            self.buttons[i][j].setText(self.current_player)

            # Check for a win or draw
            if self.check_win(self.current_player):
                self.show_message(f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                self.show_message("It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            self.show_message("This position is already occupied!")

    def check_win(self, token):

        """Check if the current player has won."""

        for row in self.board:
            if all([cell == token for cell in row]):
                return True

        for col in range(self.n):
            if all([self.board[row][col] == token for row in range(self.n)]):
                return True

        if all([self.board[i][i] == token for i in range(self.n)]):
            return True
        
        if all([self.board[i][self.n - i - 1] == token for i in range(self.n)]):
            return True
        
        return False

    def is_draw(self):

        """Check if the board is full and the game is a draw."""

        return all(self.board[i][j] != "-" for i in range(self.n) for j in range(self.n))

    def show_message(self, message):

        """Show a message box to display game results."""

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(" IMPORTANT ")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def reset_board(self):

        """Reset the board for a new game."""

        self.board = [["-" for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                self.buttons[i][j].setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToeApp(n=5)
    sys.exit(app.exec_())
