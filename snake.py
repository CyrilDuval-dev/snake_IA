from colors import Colors
from position import Position
import pygame

class Snake:

    def __init__(self):
        self.body = [Position(7, 5), Position(7, 4), Position(7, 3)]
        self.direction = "RIGHT"
        self.color = Colors.blue

    def move(self):
        head = self.body[0]
        if self.direction == "UP":
            new_head = Position(head.row - 1, head.column)
        elif self.direction == "DOWN":
            new_head = Position(head.row + 1, head.column)
        elif self.direction == "LEFT":
            new_head = Position(head.row, head.column - 1)
        elif self.direction == "RIGHT":
            new_head = Position(head.row, head.column + 1)

        self.body.insert(0, new_head)
        self.body.pop()
    
    def eating(self,apple_position):
        head = self.body[0]
        return head.row == apple_position.row and head.column == apple_position.column


    def grow(self):
        tail = self.body[-1]
        self.body.append(Position(tail.row, tail.column)) 

    def draw(self, screen):
        for segment in self.body:
            if segment == self.body[0]:
                cell_rect = pygame.Rect(segment.column * 30 +20, segment.row * 30+60, 30, 30)
                pygame.draw.rect(screen, self.color, cell_rect, border_radius=5)
                if self.direction == "UP":
                    eye1 = (segment.column * 30 + 30, segment.row * 30 + 70)
                    eye2 = (segment.column * 30 + 50, segment.row * 30 + 70)
                elif self.direction == "DOWN":
                    eye1 = (segment.column * 30 + 30, segment.row * 30 + 90)
                    eye2 = (segment.column * 30 + 50, segment.row * 30 + 90)
                elif self.direction == "LEFT":
                    eye1 = (segment.column * 30 + 25, segment.row * 30 + 70)
                    eye2 = (segment.column * 30 + 25, segment.row * 30 + 90)
                elif self.direction == "RIGHT":
                    eye1 = (segment.column * 30 + 55, segment.row * 30 + 70)
                    eye2 = (segment.column * 30 + 55, segment.row * 30 + 90)
                pygame.draw.circle(screen, Colors.white, eye1, 5)
                pygame.draw.circle(screen, Colors.white, eye2, 5)
            else:
                cell_rect = pygame.Rect(segment.column * 30 +20, segment.row * 30+60, 30, 30)
                pygame.draw.rect(screen, self.color, cell_rect, border_radius=0)