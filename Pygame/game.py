import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
JDC = (100, 22, 200)
font = pygame.font.SysFont('Calibri', 25, True, False)
    
p = 0
x = 0
y = 0
m = 1
v = 0
size = (1000,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()
pygame.key.set_repeat(50,50)

left = False
right = False
up = False
down = False

while not done:
    for event in pygame.event.get():
        #key inputs
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            left = True
        if event.key == pygame.K_d:
            right = True
        if event.key == pygame.K_w:
            up = True
        if event.key == pygame.K_s:
            down = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            left = False
        if event.key == pygame.K_d:
            right = False
        if event.key == pygame.K_w:
            up = False
        if event.key == pygame.K_s:
            down = False
        
    if (left == True):
        x -= 5
    if (right == True):
        x += 5
    if (up == True):
        y -= 5
    if (down == True):
        y += 5

    #keeps square in bounds
    if x < 0:
        x = 0
    elif x > 950:
        x = 950
    elif y < 0:
        y = 0
    elif y > 450:
        y = 450

    #red square moving
    v += m
    if v > 470 or v < 0:
        m *= -1
    
    screen.fill(WHITE)
    pygame.draw.rect(screen,JDC,[x,y, 50,50])
    pygame.draw.rect(screen,RED,[100,v,30,30])
    pygame.draw.polygon(screen, BLACK, [[0,500], [25,475], [50,500]])
    pygame.draw.polygon(screen, BLACK, [[50,500], [75,475], [100,500]])
    pygame.display.flip()
    clock.tick(120)
pygame.quit()