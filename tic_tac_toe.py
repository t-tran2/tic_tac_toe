def check_board(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] != 0:
                print(f"Player {row[0]} wins from horizontal!")
                return False
    for col_num in range(3):
        if board[0][col_num] == board[1][col_num] == board[2][col_num]:
            if board[0][col_num] != 0:
                print(f"Player {board[0][col_num]} wins from vertical!")
                return False
    if board[0][0] == board [1][1] == board[2][2]:
        if board[0][0] != 0:
                print(f"Player {board[0][0]} wins from diagonal!")
                return False
    elif board[0][2] == board [1][1] == board[2][0]:
        if board[0][2] != 0:
                print(f"Player {board[0][2]} wins from diagonal!")
                return False
    elif 0 not in board[0] or 0 not in board[1] or 0 not in board[2]:
        print("Tie game")
        return False

game = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
for row in game:
    print(row)

while True:
    play_again = None
    for player in range(1,3):
        move = [(int(x) - 1) for x in
            input("What is your move (row, column)? ").split(", ")]
        if player == 1:
            game[move[0]][move[1]] = 'X'
        else:
            game[move[0]][move[1]] = 'O'
        for row in game:
            print(row)
        if check_board(game) == False:
            play_again = input("Play again (y/n)? ")
            if play_again == 'n':
                break
            else:
                game = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    if play_again == 'n':
        break
