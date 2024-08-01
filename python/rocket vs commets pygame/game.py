import pygame
import random

pygame.init()

window_width = 900
window_height = 700
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rocket vs Commets")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

font = pygame.font.SysFont(None, 30)

background_image = pygame.image.load("python/rocket vs commets pygame/space.png").convert()
background_image = pygame.transform.scale(background_image, (window_width, window_height))
game_over_background = pygame.image.load("python/rocket vs commets pygame/game_over.png").convert()
commet_image = pygame.image.load("python/rocket vs commets pygame/commets.png").convert_alpha()
commet_image = pygame.transform.scale(commet_image, (200, 100))
player_image = pygame.image.load("python/rocket vs commets pygame/rocket.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (150, 150))

game_over_screen = pygame.Surface((window_width, window_height))
game_over_screen.blit(game_over_background, (0, 0))

game_over_sound = pygame.mixer.Sound("python/rocket vs commets pygame/explosion.mp3")

clock = pygame.time.Clock()

player_x = 400
player_y = 750
player_speed = 10
lose_list = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - commet_image.get_width():
        player_x += player_speed

    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < window_width - commet_image.get_width():
        player_y += player_speed

    if random.randint(1, 200) == 1:
        lose_list.append(pygame.Rect(random.randint(0, window_width - commet_image.get_width()), -
                         commet_image.get_height(), commet_image.get_width(), commet_image.get_height()))

    for lose in lose_list:
        lose.move_ip(0, 5)

    for lose in lose_list[:]:
        if lose.colliderect(pygame.Rect(player_x, player_y, commet_image.get_width(), commet_image.get_height())):
            game_over_sound.play()
            pygame.mixer.music.stop()
            running = False

    window.blit(background_image, (0, 0))
    for lose in lose_list:
        window.blit(commet_image, lose)
    window.blit(player_image, (player_x, player_y))
    pygame.display.update()

    clock.tick(60)

game_over_screen = pygame.Surface((window_width, window_height))
game_over_screen.blit(game_over_background, (0, 0))
window.blit(game_over_screen, (0, 0))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()