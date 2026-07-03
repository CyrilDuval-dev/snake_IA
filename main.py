import pygame
from food import Food
from game import Game
from colors import Colors
from ai import SnakeAI

pygame.init()

title_font = pygame.font.Font(None, 40)
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((550,540))

clock = pygame.time.Clock()
game = Game()
ai = SnakeAI(game.grid)
ai_mode = False

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

image_snake = pygame.image.load("assets/images/snake_menu.png").convert_alpha()
image_trophy = pygame.image.load("assets/images/trophy.png").convert_alpha()
icon_play = pygame.image.load("assets/images/play_icon.png").convert_alpha()
icon_ai = pygame.image.load("assets/images/robot.png").convert_alpha()


game_start = False
can_move = False
high_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if game_start:
            if can_move:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset()
                    if event.key == pygame.K_UP and game.snake.direction != "DOWN":
                        if game.snake.direction != "UP":
                            game.snake.sound_rotation.play()
                        game.snake.direction = "UP"
                    if event.key == pygame.K_DOWN and game.snake.direction != "UP":
                        if game.snake.direction != "DOWN":
                            game.snake.sound_rotation.play()
                        game.snake.direction = "DOWN"
                    if event.key == pygame.K_LEFT and game.snake.direction != "RIGHT":
                        if game.snake.direction != "LEFT":
                            game.snake.sound_rotation.play()
                        game.snake.direction = "LEFT"
                    if event.key == pygame.K_RIGHT and game.snake.direction != "LEFT":
                        if game.snake.direction != "RIGHT":
                            game.snake.sound_rotation.play()
                        game.snake.direction = "RIGHT"
                elif event.type == GAME_UPDATE and not game.game_over:
                    if ai_mode:
                        new_direction = ai.get_next_direction(game.snake, game.food)
                        if new_direction and new_direction != game.snake.direction:
                            game.snake.sound_rotation.play()
                            game.snake.direction = new_direction
                    game.snake.move()
                    if game.snake.eating(game.food.position):
                        game.snake.grow()
                        game.food = Food(game.snake.body[:-1])
                        game.score += 1
                    game.game_over_check()
                elif event.type == GAME_UPDATE and game.game_over:
                    if game.score > high_score:
                        high_score = game.score
                    game_start = False
                    can_move = False
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and game.snake.direction != "DOWN":
                        game.snake.direction = "UP"
                    if event.key == pygame.K_DOWN and game.snake.direction != "UP":
                        game.snake.direction = "DOWN"
                    if event.key == pygame.K_RIGHT and game.snake.direction != "LEFT":
                        game.snake.direction = "RIGHT"
                    can_move = True



    screen.fill(Colors.dark_green)
    game.draw(screen)
    screen.blit(pygame.transform.scale(game.food.image_apple, (30, 30)), (20, 15))
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.blit(score_value_surface, (80, 17))

    if not can_move and game_start:
        text_move = title_font.render("Utiliser les flèches pour bouger", True, Colors.white)
        screen.blit(text_move, (50, 200))
    
    if game_start == False:
        overlay = pygame.Surface((550, 540), pygame.SRCALPHA)  
        pygame.draw.rect(overlay, (0, 0, 0, 180), (0, 0, 550, 540))
        pygame.draw.rect(overlay, Colors.blue_sky, (150, 40, 250, 300), border_radius=10)
        screen.blit(overlay, (0, 0))
        screen.blit(pygame.transform.scale(image_snake, (250, 300)), (150, 40))
        screen.blit(pygame.transform.scale(game.food.image_apple, (40,40)), (200, 80))
        score_apple_surface = title_font.render(str(game.score), True, Colors.white)
        screen.blit(score_apple_surface, (210, 140))
        screen.blit(pygame.transform.scale(image_trophy, (50,50)), (320, 80))
        score_trophy_surface = title_font.render(str(high_score), True, Colors.white)
        screen.blit(score_trophy_surface, (340, 140))

        btn_play = pygame.draw.rect(screen, Colors.blue, (150, 360, 250, 50), border_radius=10)
        screen.blit(pygame.transform.scale(icon_play, (30, 30)), (180, 370))
        btn_play_text = title_font.render("Jouer", True, Colors.white)
        screen.blit(btn_play_text, (250, 370))

        btn_ai = pygame.draw.rect(screen, Colors.dark_purple, (150, 420, 250, 50), border_radius=10)
        screen.blit(pygame.transform.scale(icon_ai, (30, 30)), (180, 430))
        btn_ai_text = title_font.render("IA", True, Colors.white)
        btn_ai_text_rect = btn_ai_text.get_rect(center=btn_ai.center)
        screen.blit(btn_ai_text, btn_ai_text_rect)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and btn_play.collidepoint(event.pos):
            game_start = True
            ai_mode = False
            game.reset()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and btn_ai.collidepoint(event.pos):
            game_start = True
            ai_mode = True
            can_move = True
            game.reset()

    pygame.display.update()
    clock.tick(60)