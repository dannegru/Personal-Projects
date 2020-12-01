# This file contains the GUI version of the game

import pygame
import sys


# Classes
class Const:
    # Sizes
    SQUARE = 200
    RADIUS = 70
    FONT_SIZE = 75
    ROW_COUNT = 3
    COLUMN_COUNT = 3
    MARGIN_WIDTH = 5
    PIECE_MARGIN_DISTANCE = 30
    O_WIDTH = 10
    X_WIDTH = 15

    # Colors
    BLACK = (0, 0, 0)
    GREEN = (0, 153, 0)
    BLUE = (150, 200, 200)
    RED = (220, 0, 0)
    VIOLET = (204, 153, 255)

    MARGIN_COLOR = BLUE
    RESULT_PRINTING_COLOR = VIOLET
    RESULT_SCREEN_COLOR = BLACK
    X_COLOR = GREEN
    O_COLOR = RED


class GameVars:
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    game_still_going = True
    winner = None
    current_player = 'X'
    check_for_tie = 1


class Graphics:
    WIN_PRINT_POSITION = (Const.SQUARE//2, Const.SQUARE + Const.SQUARE//4)
    TIE_PRINT_POSITION = (Const.SQUARE + Const.SQUARE//4,
                          Const.SQUARE + Const.SQUARE//4)
    DEFAULT_DELAY_TIME = 500
    HEIGHT = Const.ROW_COUNT * Const.SQUARE
    WIDTH = Const.COLUMN_COUNT * Const.SQUARE
    size = (WIDTH, HEIGHT)
    WHOLE_SCREEN_SIZE = ((0, 0), size)

    def draw_table(self):
        for row in range(Const.ROW_COUNT):
            for col in range(Const.COLUMN_COUNT):
                pygame.draw.rect(screen, Const.MARGIN_COLOR, (col * Const.SQUARE, row * Const.SQUARE, Const.SQUARE,
                                                              Const.SQUARE), Const.MARGIN_WIDTH)
        pygame.display.update()

    def draw_x(self, column, row):
        pygame.draw.line(screen, Const.X_COLOR, (column * Const.SQUARE + Const.PIECE_MARGIN_DISTANCE, row * Const.SQUARE + Const.SQUARE - Const.PIECE_MARGIN_DISTANCE),
                         (column * Const.SQUARE + Const.SQUARE - Const.PIECE_MARGIN_DISTANCE, row * Const.SQUARE + Const.PIECE_MARGIN_DISTANCE), Const.X_WIDTH)
        pygame.draw.line(screen, Const.X_COLOR, (column * Const.SQUARE + Const.PIECE_MARGIN_DISTANCE, row * Const.SQUARE + Const.PIECE_MARGIN_DISTANCE),
                         (column * Const.SQUARE + Const.SQUARE - Const.PIECE_MARGIN_DISTANCE, row * Const.SQUARE + Const.SQUARE - Const.PIECE_MARGIN_DISTANCE), Const.X_WIDTH)
        pygame.display.update()

    def draw_0(self, column, row):
        pygame.draw.circle(screen, Const.O_COLOR, (column * Const.SQUARE + Const.SQUARE // 2,
                                                   row * Const.SQUARE + Const.SQUARE // 2), Const.RADIUS, Const.O_WIDTH)
        pygame.display.update()


# Graphics Initialisation
graphics = Graphics()
pygame.init()
screen = pygame.display.set_mode(graphics.size)
pygame.display.set_caption("Tic Tac Toe Game")
myfont = pygame.font.SysFont('Arial', Const.FONT_SIZE)
graphics.draw_table()


# Functions
def check_for_winner():

    def change_player():
        if GameVars.current_player == 'X':
            GameVars.current_player = 'O'
        elif GameVars.current_player == 'O':
            GameVars.current_player = 'X'

    def check_rows():
        row1 = GameVars.board[0][0] == GameVars.board[0][1] == GameVars.board[0][2] != '-'
        row2 = GameVars.board[1][0] == GameVars.board[1][1] == GameVars.board[1][2] != '-'
        row3 = GameVars.board[2][0] == GameVars.board[2][1] == GameVars.board[2][2] != '-'
        if row1 or row2 or row3:
            GameVars.game_still_going = False
        if row1:
            return GameVars.board[0][0]
        elif row2:
            return GameVars.board[1][0]
        elif row3:
            return GameVars.board[2][0]
        else:
            return None

    def check_columns():
        column1 = GameVars.board[0][0] == GameVars.board[1][0] == GameVars.board[2][0] != '-'
        column2 = GameVars.board[0][1] == GameVars.board[1][1] == GameVars.board[2][1] != '-'
        column3 = GameVars.board[0][2] == GameVars.board[1][2] == GameVars.board[2][2] != '-'
        if column1 or column2 or column3:
            GameVars.game_still_going = False
        if column1:
            return GameVars.board[0][0]
        elif column2:
            return GameVars.board[0][1]
        elif column3:
            return GameVars.board[0][2]
        else:
            return None

    def check_diagonals():
        diagonal1 = GameVars.board[0][0] == GameVars.board[1][1] == GameVars.board[2][2] != '-'
        diagonal2 = GameVars.board[0][2] == GameVars.board[1][1] == GameVars.board[2][0] != '-'
        if diagonal1 or diagonal2:
            GameVars.game_still_going = False
        if diagonal1:
            return GameVars.board[0][0]
        elif diagonal2:
            return GameVars.board[0][2]
        else:
            return None

    if check_rows():
        GameVars.winner = check_rows()
    if check_columns():
        GameVars.winner = check_columns()
    if check_diagonals():
        GameVars.winner = check_diagonals()
    if not GameVars.winner:
        GameVars.check_for_tie += 1
    change_player()


def play_game(current_player):
    if event.type == pygame.MOUSEBUTTONDOWN:
        posx = event.pos[0]
        column = posx // Const.SQUARE
        posy = event.pos[1]
        row = posy // Const.SQUARE

        if GameVars.board[row][column] == '-':
            GameVars.board[row][column] = current_player
            if current_player == 'X':
                graphics.draw_x(column, row)
            elif current_player == 'O':
                graphics.draw_0(column, row)
            check_for_winner()


def results():
    if GameVars.winner or GameVars.check_for_tie == 10:
        pygame.time.delay(graphics.DEFAULT_DELAY_TIME)
        pygame.draw.rect(screen, Const.RESULT_SCREEN_COLOR,
                         graphics.WHOLE_SCREEN_SIZE)
        pygame.display.update()
        if GameVars.winner == 'X':
            label = myfont.render("Player X Won!", 0,
                                  Const.RESULT_PRINTING_COLOR, Const.BLACK)
            screen.blit(label, graphics.WIN_PRINT_POSITION)
        elif GameVars.winner == 'O':
            label = myfont.render("Player O Won!", 0,
                                  Const.RESULT_PRINTING_COLOR, Const.BLACK)
            screen.blit(label, graphics.WIN_PRINT_POSITION)
        elif GameVars.check_for_tie == 10:
            label = myfont.render(
                "TIE!", 0, Const.RESULT_PRINTING_COLOR, Const.BLACK)
            screen.blit(label, graphics.TIE_PRINT_POSITION)
        pygame.display.update()
        pygame.time.delay(graphics.DEFAULT_DELAY_TIME * 4)


# Main loop
while GameVars.game_still_going and GameVars.check_for_tie <= 9:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            play_game(GameVars.current_player)
results()
