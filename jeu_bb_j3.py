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
bubbles_size = list()

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
        screen.blit(pygame.transform.scale(blue_bubble, (bubbles_size[i], bubbles_size[i])), bubbles_pos[i])
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

    size_bubble = random.randint(blue_bubble.get_width() / 3, blue_bubble.get_width() * 2)
    bubbles_size.append(size_bubble)

    bubbles_pos.append((x_bubble, y_bubble))
    bubbles_speed.append(random.randint(1, BUBBLE_MAX_SPEED))

# Move the bubble on the screen with the specified speed
def move_bubbles():
    for i in range (len(bubbles_pos) - 1, -1, -1):
        bubbles_pos[i] = tuple(map(operator.sub, bubbles_pos[i], (bubbles_speed[i], 0)))

# Update the game
def update_game():

    if (random.randint(1, 20) == 1):
        create_bubbles()

    collision()
    move_bubbles()
    clean_bubbles()

# Collision between the sub and the bubbles
def collision():
    for bubble in range(len(bubbles_pos) -1, -1, -1):
              if (x_sub < bubbles_pos[bubble][0] + bubbles_size[bubble]
          and x_sub + sub.get_width() > bubbles_pos[bubble][0]
          and y_sub < bubbles_pos[bubble][1] + bubbles_size[bubble]
          and y_sub + sub.get_height() > bubbles_pos[bubble][1]) :
                  #print ("La bulle ", bubble, "touche le sous-marin.")
                delete_bubbles(bubble)

# Delete Bubble when it collides with the submarine
def delete_bubbles (bubble):
    
    del bubbles_speed[bubble]
    del bubbles_pos[bubble]

# Remove bubbles who leave the screen
def clean_bubbles ():
    for i in range (len(bubbles_pos) - 1, -1, -1) :
        if (bubbles_pos[i][0] + blue_bubble.get_width() < 0) :
            delete_bubbles(i)

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

