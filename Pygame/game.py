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
x = 475
y = 450
m = 1
i = 300
j = 200
n = 1
gravity = 10
size = (1000,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
done = False
clock = pygame.time.Clock()
pygame.key.set_repeat(50,50)

left = False
right = False
jump = False

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
        gravity -= 0.2
        if y > 450:
            jump = False
            y = 450
            gravity = 10

    #keeps square in bounds
    if x < 0:
        x = 0
    elif x > 950:
        x = 950
    elif y < 0:
        y = 0
    elif y > 450:
        y = 450

    #green square moving in square
    if i <= 475 and i >= 300:
        i += n
    else:
        j += n
        if j > 275 or j < 200:
            n *= -1
            i += n

    screen.fill(WHITE)
    pygame.draw.rect(screen,JDC,[x,y,50,50])
    pygame.draw.rect(screen,GREEN,[i,j,25,25])
    pygame.display.flip()
    clock.tick(120)
pygame.quit()