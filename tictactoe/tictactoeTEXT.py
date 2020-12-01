# This file contains the text version of the game

positions = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
valid = True
winner = None
current_player = 'X'


def print_board():
    print("\n")
    print(f"{positions[0]} | {positions[1]} | {positions[2]}     1 | 2 | 3")
    print(f"{positions[3]} | {positions[4]} | {positions[5]}     4 | 5 | 6")
    print(f"{positions[6]} | {positions[7]} | {positions[8]}     7 | 8 | 9")
    print("\n")


def game():
    check_for_tie = 1
    while valid and check_for_tie <= 9:
        print_board()
        choice_logic()
        check_winner()
        change_player()
        check_for_tie += 1
    else:
        if not winner:
            print_board()
            print("Tie!")


def check_winner():
    global winner
    if check_rows():
        winner = check_rows()
    if check_columns():
        winner = check_columns()
    if check_diagonals():
        winner = check_diagonals()
    if winner:
        print_board()
        print(f"{winner} won!")


def choice_logic():
    global current_player
    global positions
    print(f"{current_player}'s turn: ")
    try:
        choice = int(
            input(f"{current_player}, choose a position 1-9: ")) - 1
        if choice < 0 or choice >= 9:
            print("Position must be between 1 and 9!")
            print_board()
            choice_logic()
        elif positions[choice] == '-':
            positions[choice] = current_player
        else:
            print("Can't choose this position!")
            print_board()
            choice_logic()
    except ValueError:
        print("Invalid value!")
        print_board()
        choice_logic()


def change_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


def check_rows():
    global valid
    row1 = positions[0] == positions[1] == positions[2] != '-'
    row2 = positions[3] == positions[4] == positions[5] != '-'
    row3 = positions[6] == positions[7] == positions[8] != '-'
    if row1 or row2 or row3:
        valid = False
    if row1:
        return positions[0]
    elif row2:
        return positions[3]
    elif row3:
        return positions[6]
    else:
        return None


def check_columns():
    global valid
    col1 = positions[0] == positions[3] == positions[6] != '-'
    col2 = positions[1] == positions[4] == positions[7] != '-'
    col3 = positions[2] == positions[5] == positions[8] != '-'
    if col1 or col2 or col3:
        valid = False
    if col1:
        return positions[0]
    elif col2:
        return positions[1]
    elif col3:
        return positions[2]
    else:
        return None


def check_diagonals():
    global valid
    diagonal1 = positions[0] == positions[4] == positions[8] != '-'
    diagonal2 = positions[2] == positions[4] == positions[6] != '-'
    if diagonal1 or diagonal2:
        valid = False
    if diagonal1:
        return positions[0]
    elif diagonal2:
        return positions[2]
    else:
        return None


game()
