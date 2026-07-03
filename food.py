from position import Position
import pygame
import random
class Food:

    def __init__(self,snake_body):
        self.position = self.random_position(snake_body)
        self.image_apple = pygame.image.load("assets/images/apple.png").convert_alpha()

    def random_position(self,snake_body):
        row = random.randint(0, 14)
        column = random.randint(0, 16)
        while Position(row, column) in snake_body:
            row = random.randint(0, 14)
            column = random.randint(0, 16)
        return Position(row, column)

    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.image_apple, (30 , 30)), (self.position.column * 30 + 20, self.position.row * 30 + 60))

        