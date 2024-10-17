import pygame
import random
pygame.init()

#colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#default    
size = (1000,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")
done = False
clock = pygame.time.Clock()
pygame.key.set_repeat(50,50)

sway = 0.05
col = 4
rows = 100
arr = [[0 for i in range(col)]for j in range(rows)]
for row in range(rows):  
        arr[row][0] = random.randint(0,size[0]-3) # x-coord
        arr[row][1] = random.randint(0,size[1]-3) # y-coord
        arr[row][2] = arr[row][0] # x-coord constant for swaying
        arr[row][3] = round(random.random(),2) # fall speed

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #game logic
    for j in range(rows):
        #gravity
        arr[j][1] += arr[j][3]
        #sway
        arr[j][0] += sway
        #LEFT RIGHT SWAY--------------
        k = arr[j][2]
        if arr[j][0] >= (k+10) or arr[j][0] <= (k-10):
            sway *= -1
        #snow generation on top
        if arr[j][1] >= (size[1]+3):
            arr[j][0] = random.randint(0,size[0]-3)
            arr[j][3] = round(random.random(),2)
            arr[j][2] = arr[j][0]
            arr[j][1] = -5              

    screen.fill(BLACK)
    #drawing
    for flake in range(rows):
        pygame.draw.rect(screen,WHITE,[arr[flake][0],arr[flake][1],3,3])
    pygame.display.flip()
    clock.tick(120)
pygame.quit()