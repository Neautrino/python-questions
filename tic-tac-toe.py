# Tic-Tac-Toe

# Initialize the board
board = [" " for _ in range(9)]

# Function to display the board
def display_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Function to check for a win
def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check for a draw
def check_draw(board):
    return " " not in board

# Main game loop
current_player = "X"
while True:
    display_board(board)
    print(f"Player {current_player}'s turn. Enter a position (1-9): ")

    try:
        position = int(input()) - 1
        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid move. Try again.")
            continue

        board[position] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"
    
    except ValueError:
        print("Invalid input. Enter a number (1-9) for the position.")
    except KeyboardInterrupt:
        print("\nGame aborted.")
        break
