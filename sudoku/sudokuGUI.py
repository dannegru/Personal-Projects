# This file contains the GUI version of the game

import pygame
import sys


# Pygame Init
pygame.init()
pygame.display.set_caption("Sudoku")


# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (52, 73, 150)
GREY = (212, 230, 241)

ROWS = 9
COLS = 9
CUBE_SIZE = 65
GAP = 5  # Grid Border Extra Width
THICK = 1  # Cube Border Width

SOLVING_SPEED = 10
WAITING_TIME = 1000 // SOLVING_SPEED

BOARD = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# Variables
width = ROWS * CUBE_SIZE + 2 * GAP
height = (COLS + 1) * CUBE_SIZE + 2 * GAP
size = width, height

fontB = pygame.font.SysFont('freesansbold.ttf', 65)  # B -> Big
fontS = pygame.font.SysFont('freesansbold.ttf', 40)  # S -> Small
fontSS = pygame.font.SysFont('freesansbold.ttf', 30)  # SS -> Very Small

window = pygame.display.set_mode(size)
window.fill(WHITE)


class Sudoku:
    def __init__(self):
        self.board = BOARD
        self.grid = dict()

        self.x_cor = None
        self.y_cor = None
        self.row = 0
        self.col = 0

        self.draw_grid()
        self.mainloop()

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                # Redirecting By Option
                if event.type == pygame.QUIT:
                    self.event_logic(event, 'QUIT')
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.event_logic(event, 'MOUSEBUTTONDOWN')
                elif event.type == pygame.KEYDOWN:
                    self.event_logic(event, 'KEYDOWN')

    def event_logic(self, event, option):
        if option == 'QUIT':
            sys.exit()

        elif option == 'MOUSEBUTTONDOWN':
            # If Present, Deselect The Last Cube
            if self.x_cor and self.y_cor:
                self.update_grid('DESELECT')

            # Then Update The Coords
            self.update_coords(event)

            # Then Show The Red Border Of The Selected Cube
            self.update_grid('SELECT')

        elif option == 'KEYDOWN':
            if event.key == pygame.K_ESCAPE:
                sys.exit()

            elif event.key == pygame.K_SPACE:
                # Clear The Placed Numbers
                self.reset_board()

                # Auto-Solve The Board
                self.solve()

            elif self.x_cor or self.y_cor:
                # Redirecting By The Pressed Key
                for number in range(1, 10):
                    if event.key in [eval(f'pygame.K_{number}'), eval(f'pygame.K_KP{number}')]:
                        self.display_input('NUMBER', number)

                if event.key == pygame.K_BACKSPACE:
                    self.display_input('BACKSPACE')

                if event.key == pygame.K_RETURN:
                    self.display_input('RETURN')

    def update_coords(self, event=None):
        if event:
            self.x_cor = event.pos[0]
            self.y_cor = event.pos[1]
            self.row = self.y_cor // CUBE_SIZE
            self.col = self.x_cor // CUBE_SIZE

        self.index = str(self.row) + str(self.col)
        self.cube_coords = (self.col * CUBE_SIZE + GAP,
                            self.row * CUBE_SIZE + GAP, CUBE_SIZE, CUBE_SIZE)
        self.numS_coords = (self.col * CUBE_SIZE + GAP + 40,
                            self.row * CUBE_SIZE + GAP + 5)
        self.numB_coords = (self.col * CUBE_SIZE + GAP + 22,
                            self.row * CUBE_SIZE + GAP + 12)

    def draw_grid(self):
        while True:
            if self.col == 9:
                self.col = 0
                self.row += 1
                if self.row == 9:
                    break

            self.update_coords()

            if self.board[self.row][self.col] == 0:
                # Draw The Empty Cube
                pygame.draw.rect(window, WHITE, self.cube_coords)
                pygame.draw.rect(window, BLACK, self.cube_coords, THICK)

                # Set The Cube Characteristics
                self.grid[self.index] = [0, 'SMALL', 'REMOVABLE']
            else:
                # Draw The Pre-Filled Cube
                pygame.draw.rect(window, GREY, self.cube_coords)
                pygame.draw.rect(window, BLACK, self.cube_coords, THICK)

                # Set The Cube Characteristics
                self.grid[self.index] = [self.board[self.row]
                                         [self.col], 'BIG', 'NOT REMOVABLE']

                # Print The Number In The Cube
                label = fontB.render(
                    str(self.board[self.row][self.col]), True, BLACK)
                window.blit(label, self.numB_coords)

            self.col += 1

        # Print The Help Text For Auto-Solving
        label = fontSS.render(
            'Press SPACE to auto-solve the puzzle.', True, BLACK)
        window.blit(label, (110, 615))

        self.update_grid()

    def reset_board(self):
        # Delete All Numbers Placed By The User
        for row in range(ROWS):
            for col in range(COLS):
                index = str(row) + str(col)
                if self.grid[index][2] == 'REMOVABLE':
                    self.board[row][col] = 0

    def update_grid(self, option=None):
        if option == 'SELECT':
            # Make The Cube Border Red
            pygame.draw.rect(window, RED, self.cube_coords, THICK)

        elif option == 'DESELECT':
            # Make The Cube Border Black
            pygame.draw.rect(window, BLACK, self.cube_coords, THICK)

        elif option == 'SOLVED':
            # The Auto-Solved Grid Has Only Green Borders -> Make Them Black
            for row in range(ROWS):
                for col in range(COLS):
                    coords = (col * CUBE_SIZE + GAP, row *
                              CUBE_SIZE + GAP, CUBE_SIZE, CUBE_SIZE)
                    pygame.draw.rect(window, BLACK, coords, THICK)

        # Draw The Thick Lines
        for row in range(4):
            pygame.draw.line(window, BLACK, (row*CUBE_SIZE*3 + GAP, 5),
                             (row*CUBE_SIZE*3 + GAP, height - CUBE_SIZE - 3), 5)
        for col in range(4):
            pygame.draw.line(window, BLACK, (3, col*CUBE_SIZE*3 + GAP),
                             (width - 3, col*CUBE_SIZE*3 + GAP), 5)
        pygame.display.update()

    def display_input(self, option, number=None):
        if option == 'NUMBER':
            if self.grid[self.index][1] == 'SMALL':
                # Empty The Cube
                pygame.draw.rect(window, WHITE, self.cube_coords)
                pygame.draw.rect(window, BLACK, self.cube_coords, THICK)

                # Update The Small Number
                self.grid[self.index][0] = number

                # Print The New Small Number
                label = fontS.render(str(number), True, BLUE)
                window.blit(label, self.numS_coords)

        elif option == 'RETURN':
            if self.grid[self.index][0] and self.grid[self.index][1] == 'SMALL':
                if self.validPlacement(self.row, self.col, self.grid[self.index][0]):
                    # Empty The Cube
                    pygame.draw.rect(window, WHITE, self.cube_coords)
                    pygame.draw.rect(window, BLACK, self.cube_coords, THICK)

                    # Update The Number's Size (Small -> Big)
                    self.grid[self.index][1] = 'BIG'

                    # Update The Board Position
                    self.board[self.row][self.col] = self.grid[self.index][0]

                    # Print The Big Number
                    label = fontB.render(
                        str(self.grid[self.index][0]), True, BLACK)
                    window.blit(label, self.numB_coords)
                else:
                    # Empty The Cube
                    pygame.draw.rect(window, WHITE, self.cube_coords)
                    pygame.draw.rect(window, BLACK, self.cube_coords, THICK)

                    # Show The Placement Is Not Valid
                    label = fontS.render('X', True, RED)
                    window.blit(label, self.numS_coords)

        elif option == 'BACKSPACE':
            if self.grid[self.index][0] and self.grid[self.index][2] == 'REMOVABLE':

                # Reset The Cube Characteristics
                self.grid[self.index] = [0, 'SMALL', 'REMOVABLE']

                # Update The Board Position
                self.board[self.row][self.col] = 0

                # Empty The Cube
                pygame.draw.rect(window, WHITE, self.cube_coords)
                pygame.draw.rect(window, BLACK, self.cube_coords, THICK)

        self.update_grid('SELECT')

    def solve(self, row=0, col=0):
        self.stop = False
        if col == 9:
            col = 0
            row += 1
            if row == 9:
                self.stop = True
                self.update_grid('SOLVED')
                return

        if self.board[row][col] == 0:
            for value in range(1, 10):
                if self.validPlacement(row, col, value):
                    self.board[row][col] = value
                    self.update_number('ADD', row, col)
                    self.solve(row, col + 1)
            else:
                if not self.stop:
                    self.board[row][col] = 0
                    self.update_number('REMOVE', row, col)
        else:
            self.solve(row, col + 1)

    def update_number(self, option, row, col):
        # Set The Coords
        index = str(row) + str(col)
        coords = (col * CUBE_SIZE + GAP, row *
                  CUBE_SIZE + GAP, CUBE_SIZE, CUBE_SIZE)

        # Empty The Cube For The New Number To Be Printed
        pygame.draw.rect(window, WHITE, coords)

        # Show The Cube Border Color
        if option == 'ADD':
            pygame.draw.rect(window, GREEN, coords, THICK)
        elif option == 'REMOVE':
            pygame.draw.rect(window, RED, coords, THICK)

        # Set The Cube Characteristics
        self.grid[index] = [self.board[row][col], 'BIG', 'NOT REMOVABLE']

        # Print The Number In The Cube
        label = fontB.render(str(self.board[row][col]), True, BLACK)
        window.blit(label, (col * CUBE_SIZE + GAP +
                            22, row * CUBE_SIZE + GAP + 12))

        # Update The Board, Then Wait
        self.update_grid()
        pygame.time.wait(WAITING_TIME)

    def validPlacement(self, row, col, value):
        # Check Validity For Row
        if value in self.board[row]:
            return False

        # Check Validity For Column
        column = []
        for board_row in self.board:
            column.append(board_row[col])

        if value in column:
            return False

        # Check Validity For The 3x3 Cube
        cube = []
        row_index = (row // 3) * 3
        col_index = (col // 3) * 3
        for row in range(row_index, row_index + 3):
            for col in range(col_index, col_index + 3):
                cube.append(self.board[row][col])

        if value in cube:
            return False

        return True


sudoku = Sudoku()
