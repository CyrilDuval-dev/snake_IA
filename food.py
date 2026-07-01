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
            if Position(row, column) not in snake_body:
                return Position(row, column)

    def draw(self, screen):

        image = pygame.image.load("assets/images/apple.png").convert_alpha()
        screen.blit(pygame.transform.scale(image, (30 , 30)), (self.position.column * 30 + 20, self.position.row * 30 + 60))

        