def print_board(board):
    for row in board:
        print(" ".join(row))

def check_win(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

    player = 'X'
    while True:
        print(f"Player {player}, enter your move: ")
        move = input()
        x, y = map(int, move.split())

        if board[x][y] != ' ':
            print("Invalid move, try again.")
            continue

        board[x][y] = player
        print_board(board)

        if check_win(board):
            print(f"Player {player} wins!")
            break

        player = 'O' if player == 'X' else 'X'

tic_tac_toe()
