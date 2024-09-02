import pygame
import random

pygame.init()

width, height = 400, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

aqua = (52, 133, 189)
black = (0, 0, 0)
red = ( 255, 0, 0)

bird_width, bird_height = 40, 40
pipe_width = 70
pipe_height = 500
gap = 200

bird = pygame.Rect(100, height//2, bird_width, bird_height)
pipe1 = pygame.Rect(width, random.randint(-pipe_height + gap, 0), pipe_width, pipe_height)
pipe2 = pygame.Rect(width, pipe1.bottom + gap, pipe_width, pipe_height)

clock = pygame.time.Clock()
fps = 60

gravity = 0.5
bird_movement = 0
pipe_speed = 5
score = 0

def draw_window():
    win.fill(aqua)
    pygame.draw.rect(win, black, bird)
    pygame.draw.rect(win, red, pipe1)
    pygame.draw.rect(win, red, pipe2)
    score_text = pygame.font.SysFont('comicsans', 40).render(f"Score: {score}", 1, black)
    win.blit(score_text, (10, 10))
    pygame.display.update()

def handle_pipes():
    global score
    pipe1.x -= pipe_speed
    pipe2.x -= pipe_speed
    if pipe1.right < 0:
        pipe1.x = width
        pipe1.y = random.randint(-pipe_height + gap, 0)
        pipe2.y = pipe1.bottom + gap
        score += 1

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -10

    bird_movement += gravity
    bird.y += bird_movement

    handle_pipes()

    if bird.colliderect(pipe1) or bird.colliderect(pipe2) or bird.top <= 0 or bird.bottom >= height:
        run = False

    draw_window()

pygame.quit()