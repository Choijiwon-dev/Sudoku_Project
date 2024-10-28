def print_board(board):
    for row in board:
        print(" ".join(map(str, row)), end="\n")

board = initialize_board()
print_board(board)