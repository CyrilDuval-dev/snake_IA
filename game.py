from grid import Grid
from snake import Snake
from food import Food
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.snake = Snake()
        self.food = Food(snake_body=self.snake.body)
        self.game_over = False
        self.score = 0
    
    def game_over_check(self):
        head = self.snake.body[0]
        if not self.grid.is_inside(head.row, head.column):
            self.game_over = True
        for segment in self.snake.body[1:]:
            if head.row == segment.row and head.column == segment.column:
                self.game_over = True

    def reset(self):
        self.__init__()

    def draw(self, screen):
        self.grid.draw(screen)
        self.snake.draw(screen)
        self.food.draw(screen)
        if self.game_over:
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
            text_rect = text.get_rect(center=(275, 250))
            screen.blit(text, text_rect)
        
