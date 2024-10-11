import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
JDC = (100, 22, 200)

x, xV = 0, 3
y, yV = 250, 3

Ly = 200
Ry = 200

size = (1000,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Square")

done = False
clock = pygame.time.Clock()
pygame.key.set_repeat(50,50)

LUp, LDown = False, False
RUp, RDown = False, False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #key inputs
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            LUp = True
        if event.key == pygame.K_s:
            LDown = True
        if event.key == pygame.K_UP:
            RUp = True
        if event.key == pygame.K_DOWN:
            RDown = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            LUp = False
        if event.key == pygame.K_s:
            LDown = False
        if event.key == pygame.K_UP:
            RUp = False
        if event.key == pygame.K_DOWN:
            RDown = False

    if (LUp == True):
        Ly -= 5
    if (LDown == True):
        Ly += 5
    if (RUp == True):
        Ry -= 5
    if (RDown == True):
        Ry += 5

    if Ly < 5:
        Ly = 5
    elif Ly > 390:
        Ly = 390
    if Ry < 5:
        Ry = 5
    elif Ry > 390:
        Ry = 390

    #bouncing square
    x += xV
    y += yV
    if x >= 970 or x <= 0:
        xV *= -1
    if y >= 470 or y <= 0:
        yV *= -1

    screen.fill(WHITE)
    pygame.draw.rect(screen,RED,[x,y,30,30])
    pygame.draw.rect(screen,BLACK,[5,Ly,10,100])
    pygame.draw.rect(screen,BLACK,[985,Ry,10,100])
    pygame.display.flip()
    clock.tick(120)
pygame.quit()