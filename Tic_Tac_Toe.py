from os import system

# creates board
def init_board():
    board = [ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]
    return board

# validates the input and return the coordonates
def get_move(board, player):
    valid_input = False
    while valid_input == False:
        coordinates = input("Player " + player + " turn: ")
        if coordinates.lower() == "quit":
            system("clear")
            input("Player " + player + " has quit.")
            system("clear")
            exit()
        if len(coordinates) == 2:
            row = list(coordinates)[0].upper()
            col = list(coordinates)[1]
            valid_input = True
        else:
            input("Invalid format. The move consists of a letter and a number i.e. \"A1\",\"B2\", etc.")
            valid_input = False
            print_board(board)
        if valid_input and (row not in "ABC" or col not in "123"):                                 
            valid_input = False
            input("Invalid coordinates, please restate move.")
            print_board(board)
        if valid_input:
            row = ord(row.upper())-65
            col = int(col)-1      
        if valid_input and board[row][col] in ("X","O"):
            valid_input = False
            input("Illegal move, please choose an empty square.")
            print_board(board)           
        if valid_input:
            return row, col

# marks the coordonates with X or O
def mark(board, player, row, col):
        board[row][col] = player
        print_board(board)

# checks if the player has won the game
def has_won(board, player):
    for i in [
        [board[0][0],board[0][1],board[0][2]],
        [board[1][0],board[1][1],board[1][2]],    
        [board[2][0],board[2][1],board[2][2]],
        [board[0][0],board[1][0],board[2][0]],
        [board[0][1],board[1][1],board[2][1]],
        [board[0][2],board[1][2],board[2][2]],
        [board[0][0],board[1][1],board[2][2]],
        [board[0][2],board[1][1],board[2][0]]]:
        if i == [player,player,player]:
            return True
    return False

# checks if the board is full
def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                return False
    return True

# prints the styled board
def print_board(board):
    print("    1   2   3\n")
    print("A   ",end="",flush=True)
    print(*board[0],sep=" | ")
    print("   ---+---+---")
    print("B   ",end="",flush=True)
    print(*board[1],sep=" | ")
    print("   ---+---+---")
    print("C   ",end="",flush=True)
    print(*board[2],sep=" | ")
    print("\n")

# prints the winner
def print_result(winner):
    if winner == "X":
        return input ("Player X wins!")
    elif winner == "O":
        return input ("Player O wins!")
    elif winner == "":
        return input("The game ended in a tie...")


def tictactoe_game():
        board = init_board()
        print_board(board)
        player = ""
        while player == '' or player.upper() not in ("X","O"):
            player = input("Choose your mark [X/O]: ")
            if player.upper() not in ("X","O") and player != '':
                input("Unavailable mark. Please choose between O and X. [OK]")
            print_board(board)
        player = player.upper()
        winner = ""
        while not is_full(board) and not has_won(board, "X") and not has_won(board, "O"):
            print_board(board)
            row, col = get_move(board, player)
            mark(board, player, row, col)
            if not has_won(board, player):
                player = "OX".replace(player, "")            
            else: 
                winner = player
        print_result(winner)


def main_menu():
    choose = input('\n TicTacToe \n Press any key to start the game or type quit to end the game. ')
    if choose.lower() == 'quit':
        quit()
    else: 
        tictactoe_game()


if __name__ == '__main__':
    main_menu()