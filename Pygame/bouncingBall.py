import os
import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [1, 1]
black = 0, 0, 0
gravity = 0.1

screen = pygame.display.set_mode(size)

image_file = os.path.expanduser("~/pybin/pygame_examples/data/ball.png")
ball = pygame.image.load(image_file)
ballrect = ball.get_rect()

def clip(val, minval, maxval):
    return min(max(val, minval), maxval)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    speed[1] += gravity

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # clip the position to remain in the window

    ballrect.left = clip(ballrect.left, 0, width)
    ballrect.right = clip(ballrect.right, 0, width)        
    ballrect.top = clip(ballrect.top, 0, height)
    ballrect.bottom = clip(ballrect.bottom, 0, height) 

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()