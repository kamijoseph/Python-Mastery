
# Simple Tic Tac Toe Game
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("_" * 5)
        
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check for a tie
    if all(cell != " " for row in board for cell in row):
        return "Tie"
    
    return None

def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player} enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError
            return move
        except ValueError:
            print("invalid input. enter a number between 1 and 9 please")

def update_board(board, move, player):
    row = (move - 1) // 3
    col = (move - 1) % 3
    if board[row][col] == " ":
        board[row][col] = player
        return True
    print('invalid move. cell already occupied.')
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    print("Welcome to Tic-Tac-Toe!")
    print("Player X and Player O will take turns.")
    print("Enter a number between 1 and 9 to place your mark.")
    print("The positions are as follows:")
    print("1 | 2 | 3")
    print("-" * 5)
    print("4 | 5 | 6")
    print("-" * 5)
    print("7 | 8 | 9")
    
    #start the game loop
    current_player = "X"
    while True:
        print_board(board)
        move = get_move(current_player)
        if update_board(board, move, current_player):
            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == "Tie":
                    print("its a tie.")
                else:
                    print(f"player {winner} wins.")
                break
            #switch players
            current_player = "O" if current_player == "X" else "X"
    
if __name__ == "__main__":
    main()