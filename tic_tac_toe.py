import random

def print_board(board):
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n-------------")

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8:
                row, col = divmod(move, 3)
                if board[row][col] == " ":
                    return row, col
                else:
                    print("That position is already taken. Try again.")
            else:
                print("Invalid input. Please enter a number from 1 to 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("The board positions are numbered 1-9:")
    print_board([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])

    while True:
        print_board(board)
        if current_player == "X":
            row, col = get_player_move(board)
        else:
            print("Computer is thinking...")
            row, col = get_computer_move(board)
            print(f"Computer chooses position {row * 3 + col + 1}")

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            if current_player == "X":
                print("Congratulations! You won!")
            else:
                print("The computer won. Better luck next time!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()