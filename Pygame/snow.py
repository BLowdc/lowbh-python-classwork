import pygame
import random
pygame.init()

#colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#record
class Flake:
    def __init__(self,x_pos,y_pos,velocity,size) -> None:
        self.x = x_pos
        self.y = y_pos
        self.vel = velocity
        self.size = size

#default    
size = (800,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")
done = False
clock = pygame.time.Clock()
pygame.key.set_repeat(50,50)

# sway = 0.05
rows = 200
arr = [None for j in range(rows)]
for row in range(rows):
        velocity = round(random.random(),2)
        flake = Flake(random.randint(0,size[0]-3),
                      random.randint(0,size[1]-3),
                      velocity,
                      velocity * 3 + 3)
        arr[row] = flake

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #game logic
    for j in range(rows):
        #gravity
        arr[j].y += arr[j].vel
        #sway
        # arr[j][0] += sway
        #LEFT RIGHT SWAY--------------
        # k = arr[j][2]
        # if arr[j][0] >= (k+10) or arr[j][0] <= (k-10):
        #     sway *= -1
        #snow generation on top
        if arr[j].y >= (size[1]+3):
            velocity = round(random.random(),2)
            flake = Flake(random.randint(0,size[0]-3),
                          -5,
                          velocity,
                          velocity * 3 + 3)
            arr[j] = flake

    screen.fill(BLACK)
    #drawing
    for f in range(rows):
        pygame.draw.rect(screen,WHITE,[arr[f].x,
                                       arr[f].y,
                                       arr[f].size,
                                       arr[f].size])
    pygame.display.flip()
    clock.tick(120)
pygame.quit()