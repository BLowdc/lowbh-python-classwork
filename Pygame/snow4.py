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
    def __init__(self) -> None:
        self.x = random.randint(0,size[0]-3)
        self.y = random.randint(0,size[1]-3)
        self.vel = round(random.random(),2)
        self.size = self.vel * 3 + 3
    #end fields

    def fall(self) -> float:
        if self.y >= (size[1]+3):
            self.y = -5
            self.x = random.randint(0,size[0]-3)
        else:
            self.y += self.vel
    #end method
    
    def draw(self):
        pygame.draw.circle(screen,WHITE,[self.x, self.y], self.size)
    #end method
#end class

#default    
size = (800,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")
done = False
clock = pygame.time.Clock()
pygame.key.set_repeat(50,50)

rows = 250
flakes = [None for j in range(rows)]
for row in range(rows):
        flake = Flake()
        flakes[row] = flake

print(list(flakes))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for flake in flakes:
        flake.fall()

    screen.fill(BLACK)

    for flake in flakes:
        flake.draw()

    pygame.display.flip()
    clock.tick(120)
pygame.quit()