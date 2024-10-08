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
y = 450
m = 1
v = 0
i = 300
j = 200
n = 1
speed = 10
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

    def j(y):
        y -= speed
        while y != 450:
            if speed <= 10 or speed >= -10:
                speed -= 0.1
        speed = abs(speed)
        return y

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
        if event.key == pygame.K_SPACE:
            jump = False
        
    if (left == True):
        x -= 5
    if (right == True):
        x += 5
    if (jump == True):
       y = j(y)

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
    pygame.draw.rect(screen,RED,[100,v,30,30])
    pygame.display.flip()
    clock.tick(120)
pygame.quit()