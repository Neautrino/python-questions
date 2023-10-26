import random

# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the game is over
def is_game_over(board):
    return (" " not in board) or check_winner(board, "X") or check_winner(board, "O")

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True

    return False

# Function to make the AI's move
def ai_move(board):
    # Try to win or block the opponent from winning
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner(board, "O"):
                return i
            board[i] = " "

    # Choose the center if available
    if board[4] == " ":
        return 4

    # Choose a random corner if available
    corners = [0, 2, 6, 8]
    available_corners = [corner for corner in corners if board[corner] == " "]
    if available_corners:
        return random.choice(available_corners)

    # Choose a random available spot
    empty_spots = [i for i in range(9) if board[i] == " "]
    return random.choice(empty_spots)

# Main game loop
while not is_game_over(board):
    display_board(board)

    # Player's move
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] == " ":
        board[player_move] = "X"
    else:
        print("Invalid move. Try again.")
        continue

    if is_game_over(board):
        break

    # AI's move
    ai_move_index = ai_move(board)
    board[ai_move_index] = "O"

display_board(board)

if check_winner(board, "X"):
    print("You win!")
elif check_winner(board, "O"):
    print("AI wins!")
else:
    print("It's a draw!")
