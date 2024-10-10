import pygame
import time
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (100, 22, 200)
YELLOW = (255,255,0)

x = 1000

size = (1000,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rising sun")
done = False
clock = pygame.time.Clock()
pygame.key.set_repeat(50,50)

while not done:
    for event in pygame.event.get():
        #key inputs
        if event.type == pygame.QUIT:
            done = True
    
    x -= 1
    if x < -100:
        x = 1050

    y = 0.0005 * ((x-500) ** 2) + 100

    screen.fill(BLACK)

    pygame.draw.circle(screen,YELLOW,[x,y],50)
    pygame.draw.rect(screen,GREEN,[0,350,1000,150])
    pygame.display.flip()
    clock.tick(120)
pygame.quit()