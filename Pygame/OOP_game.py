import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

class Bullet:
    def __init__(self, x, y, colour) -> None:
        self.x = x
        self.y = y
        self.colour = colour
    #end constructor

    def __repr__(self) -> str:
        return f'x:{self.x},y:{self.y},colour:{self.colour}'
    #end function

class Block(pygame.sprite.Sprite):
    def __init__(self, colour, height, width) -> None:
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
    #end constructor

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")
score = 0
sans_font = pygame.font.SysFont('Comic Sans MS', 30)

# Loop until the user clicks the close button.
done = False

block_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 15, 15)
    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(size[1])

    block_list.add(block)
    all_sprite_list.add(block)
#next i

player = Block(RED, 15, 15)
all_sprite_list.add(player)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
 
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in blocks_hit_list:
        score += 1
    #next block

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    all_sprite_list.draw(screen)
    blockDestroyed = sans_font.render(str(score),1,RED)
    screen.blit(blockDestroyed, (335,0))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            pygame.draw.rect(screen,GREEN,[player.rect.x,player.rect.y,5,5])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()