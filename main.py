import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

black = (0, 0, 0)
white = (255, 255, 255)

ball_radius = 20
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 1.2
ball_speed_y = 1.2

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_speed_y = -ball_speed_y

    screen.fill(black)
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(240) # framerate cap at 240, speed for 60 fps is 5

pygame.quit()
sys.exit()