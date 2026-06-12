import pygame
from food import Food
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((550,540))

clock = pygame.time.Clock()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.reset()
            elif event.key == pygame.K_UP and game.snake.direction != "DOWN":
                game.snake.direction = "UP"
            elif event.key == pygame.K_DOWN and game.snake.direction != "UP":
                game.snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and game.snake.direction != "RIGHT":
                game.snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and game.snake.direction != "LEFT":
                game.snake.direction = "RIGHT"
        elif event.type == GAME_UPDATE and not game.game_over:
            game.snake.move()
            if game.snake.eating(game.food.position):
                game.snake.grow()
                game.food = Food(game.snake.body[:-1])
                game.score += 1
            game.game_over_check()

    screen.fill(Colors.dark_green)
    game.draw(screen)
    pygame.draw.circle(screen, Colors.red, (50,30), 15)
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.blit(score_value_surface, (80, 17))
    pygame.display.update()
    clock.tick(60)