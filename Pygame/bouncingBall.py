import os
import sys, pygame
pygame.init()

size = width, height = 500,500

x = 25
y = 475
black = 0, 0, 0
red = 255, 0, 0

gravity = 10

done = False

clock = pygame.time.Clock()
pygame.key.set_repeat(50,50)

screen = pygame.display.set_mode(size)

jump = False
left = False
right = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            left = True
        if event.key == pygame.K_d:
            right = True
        if event.key == pygame.K_SPACE:
            jump = True
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            left = False
        if event.key == pygame.K_d:
            right = False

    if (left == True):
        x -= 5
    if (right == True):
        x += 5
    if (jump == True):
        y -= gravity
        gravity -= 0.3
        if y > 475:
            jump = False
            y = 475
            gravity = 10

    if x < 25:
        x = 25
    elif x > 475:
        x = 475

    print(jump,left,right)
        
    screen.fill(black)
    pygame.draw.circle(screen,red,[x,y],20)
    pygame.display.flip()
    clock.tick(120)
pygame.quit()