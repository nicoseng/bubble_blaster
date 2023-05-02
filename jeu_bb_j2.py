import pygame, sys, operator, random
from pygame.locals import *

# Global variables
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500
SUB_SPEED = 1
BUBBLE_MAX_SPEED = 10

# The submarine
x_sub = 40
y_sub = 250

# The bubbles
bubbles_pos = list()
bubbles_speed = list()

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

# The blue bubble
blue_bubble = pygame.image.load("ressources/blue_bubble.png")

# Quit the game
def leave_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

# Update the screen display
def update_screen():
    screen.blit(background_image, (0,0))
    screen.blit(sub, (x_sub, y_sub))

    for i in range(len(bubbles_pos) -1, -1, -1):
        screen.blit(blue_bubble, bubbles_pos[i])

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

    sub_in_scene()

# Check if the sub is still on the visible part of the screen
def sub_in_scene():
    global x_sub, y_sub
    
    # Left limit
    if x_sub < 0:
        x_sub = 0

    # Right limit
    if x_sub + sub.get_width() > SCREEN_WIDTH:
        x_sub = SCREEN_WIDTH - sub.get_width()

    # Up limit
    if y_sub < 0:
        y_sub = 0

    # Down limit
    if y_sub + sub.get_height() > SCREEN_HEIGHT:
        y_sub = SCREEN_HEIGHT - sub.get_height()

# Create many bubbles
def create_bubbles() :

    x_bubble = SCREEN_WIDTH / 2
    y_bubble = random.randint(0,SCREEN_HEIGHT)

    bubbles_pos.append((x_bubble, y_bubble))
    bubbles_speed.append(random.randint(1, BUBBLE_MAX_SPEED))

# Move the bubble on the screen with the specified speed
def move_bubbles():
    for i in range (len(bubbles_pos) - 1, -1, -1):
        bubbles_pos[i] = tuple(map(operator.sub, bubbles_pos[i], (bubbles_speed[i], 0)))

def update_game():
    create_bubbles()
    move_bubbles()

running = True
# Main loop
while running :
    update_game()
    update_screen()
    
    # Mail Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave_game()
    sub_control()

