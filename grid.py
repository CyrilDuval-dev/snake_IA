import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 15
        self.num_cols = 17
        self.cell_size = 30
        self.grid = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()
    

    def is_inside(self, row, col):
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols

    def draw(self, screen):
        color = Colors.get_cell_colors()

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (row + col) % 2 == 0:
                    cell_color = color[1]
                else:
                    cell_color = color[0]
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col * self.cell_size +20, row * self.cell_size+60, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, cell_color, cell_rect)