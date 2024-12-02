import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
JDC = (100, 22, 200)

x, xV = 500, 3
y, yV = 250, 3

Ly = 200
Ry = 200

ScoreLeft, ScoreRight = 0, 0

size = (1000,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Square")
sans_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = sans_font.render("Score:    -",1, BLACK)

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

    #moving platforms
    if (LUp == True):
        Ly -= 5
    if (LDown == True):
        Ly += 5
    if (RUp == True):
        Ry -= 5
    if (RDown == True):
        Ry += 5
    #platform borders
    if Ly < 5:
        Ly = 5
    elif Ly > 390:
        Ly = 390
    if Ry < 5:
        Ry = 5
    elif Ry > 390:
        Ry = 390

    #out of bounds
    if x >= 1050:
        x = 485
        ScoreLeft += 1
        pygame.time.delay(1000)

    if x <= -50:
        x = 485
        ScoreRight += 1
        pygame.time.delay(1000)

    #bouncing square
    x += xV
    y += yV
    if x >= 955 and (Ry < (y + 15) < (Ry + 100)):
        xV *= -1
    if x <= 15 and (Ly < (y + 15) < (Ly + 100)):
        xV *= -1
    if y >= 470 or y <= 0:
        yV *= -1

    screen.fill(WHITE)
    pygame.draw.rect(screen,RED,[x,y,30,30])
    pygame.draw.rect(screen,BLACK,[5,Ly,10,100])
    pygame.draw.rect(screen,BLACK,[985,Ry,10,100])
    screen.blit(text_surface, (0,0))
    scoreL = sans_font.render(str(ScoreLeft),1,RED)
    scoreR = sans_font.render(str(ScoreRight),1,BLUE)
    screen.blit(scoreL, (100,0))
    screen.blit(scoreR, (150,0))
    pygame.display.flip()
    clock.tick(120)
pygame.quit()