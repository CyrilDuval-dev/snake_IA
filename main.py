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

apple_image = pygame.image.load("assets/images/apple.png").convert_alpha()

game_start = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if game_start:
            if event.type == pygame.KEYDOWN:
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
            elif event.type == GAME_UPDATE and game.game_over:
                game_start = False


    screen.fill(Colors.dark_green)
    game.draw(screen)
    screen.blit(pygame.transform.scale(apple_image, (30, 30)), (20, 15))
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.blit(score_value_surface, (80, 17))
    
    if game_start == False:
        overlay = pygame.Surface((550, 540), pygame.SRCALPHA)  
        pygame.draw.rect(overlay, (0, 0, 0, 180), (0, 0, 550, 540))
        pygame.draw.rect(overlay, Colors.blue, (150, 40, 250, 300), border_radius=10)
        title_surface = title_font.render("Snake Game", True, Colors.white)
        game_start_surface = title_font.render("Press any key to start", True, Colors.white)
        screen.blit(title_surface, (200, 100))
        screen.blit(game_start_surface, (150, 250))
        screen.blit(overlay, (0, 0))
        
        if event.type == pygame.KEYDOWN:
            game_start = True
            game.reset()

    pygame.display.update()
    clock.tick(60)