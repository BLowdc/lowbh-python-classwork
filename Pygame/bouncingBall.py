import os
import sys, pygame
pygame.init()

size = width, height = 500,500
x = 25
y = 475
black = 0, 0, 0
red = 255, 0, 0
gravity = 10
jump = False

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            jump = True
    
    if y == 475:
        gravity = 10

    while (jump == True):
        y -= gravity
        while gravity > -10:
            gravity -= 0.2
        if y < 475:
            jump = False
        
    print(jump)
        
    screen.fill(black)
    pygame.draw.circle(screen,red,[x,y],20)
    pygame.display.flip()
    clock.tick(120)