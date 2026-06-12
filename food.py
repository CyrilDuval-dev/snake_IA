from colors import Colors
from position import Position
import pygame
import random

class Food:
    def __init__(self,snake_body):
        self.position = self.random_position(snake_body)
        self.color = Colors.red

    def random_position(self,snake_body):
        while True:
            row = random.randint(0, 14)
            column = random.randint(0, 16)
            position = Position(row, column)
            if position not in snake_body:
                return position

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.column * 30 + 35, self.position.row * 30 + 75), 15)
        