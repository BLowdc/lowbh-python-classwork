import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# class Bullet:
#     def __init__(self, x, y, colour) -> None:
#         self.x = x
#         self.y = y
#         self.colour = colour
#     #end constructor

#     def __repr__(self) -> str:
#         return f'x:{self.x},y:{self.y},colour:{self.colour}'
#     #end function
# #end class

class Block(pygame.sprite.Sprite):
    def __init__(self, colour, height, width) -> None:
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
    #end constructor

    def update(self):
        # Move the block down one pixel
        self.rect.y += 1
        if self.rect.y > size[1]:
            self.reset_pos()
        #end if
    #end method

    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, size[0])
    #end method
#end class

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([4, 4])
        self.image.fill(GOLD)
 
        self.rect = self.image.get_rect()
    #end constructor
 
    def update(self):
        self.rect.y -= 3
    #end method
#end class


pygame.display.set_caption("Space Invaders")
score = 0
sans_font = pygame.font.SysFont('Comic Sans MS', 30)

# Loop until the user clicks the close button.
done = False

block_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

for i in range(50):
    block = Block(WHITE, 15, 15)
    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(size[1])

    block_list.add(block)
    all_sprite_list.add(block)
#next i

player = Block(BLUE, 15, 15)
all_sprite_list.add(player)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprite_list.add(bullet)
                bullet_list.add(bullet)
            #end if
        #end if
    #next event

    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    
    all_sprite_list.update()
 
    player.rect.x = pos[0]
    player.rect.y = pos[1] 

    for bullet in bullet_list:
        blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, False)

        for block in blocks_hit_list:
            bullet_list.remove(bullet)
            all_sprite_list.remove(bullet)
            score += 1
            block.reset_pos()
        #next block

        if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprite_list.remove(bullet)
        #end if
    #next bullet

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    all_sprite_list.draw(screen)
    blockDestroyed = sans_font.render(str(score),1,GREEN)
    screen.blit(blockDestroyed, (335,0))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()