import pygame, sys
from pygame.locals import *

# Global variables
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500
SUB_SPEED = 1

# The submarine
x_sub = 400
y_sub = 250

# Window Init
pygame.init()

# Create Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the repetition rate of the key
pygame.key.set_repeat(10, 10)

# Window name
pygame.display.set_caption("Bubble Blaster")

# Background image
background_image = pygame.image.load("ressources/ocean.png")

# The submarine
sub = pygame.image.load("ressources/submarine.png")

# Quit the game
def leave_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

# Update the screen display
def update_screen():
    screen.blit(background_image, (0,0))
    screen.blit(sub, (x_sub, y_sub))
    pygame.display.flip()

# Move the submarine on the scene
def sub_control():
    global x_sub, y_sub
    
    key = pygame.key.get_pressed()

    if key[pygame.K_RIGHT]:
        x_sub += SUB_SPEED

    if key[pygame.K_LEFT]: 
      x_sub -= SUB_SPEED

    if key[pygame.K_UP]:
      y_sub -= SUB_SPEED

    if key[pygame.K_DOWN]:
      y_sub += SUB_SPEED

running = True
# Main loop
while running :

    update_screen()
    
    # Mail Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave_game()
    sub_control()

