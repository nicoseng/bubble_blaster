import pygame, sys, operator, random, time
from pygame.locals import *

# Global variables
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500
SUB_SPEED = 1
BUBBLE_MAX_SPEED = 10

# Color of the text
BLACK = (0, 0, 0)
DARK_BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)

# Timer
TIME_LIMIT = 10

# Bonus score
BONUS_SCORE = 200

# The submarine
x_sub = 40
y_sub = 250

# The score
score = 0

# Game end
game_end = time.time() + TIME_LIMIT

# bonus
bonus = 0

# The bubbles
bubbles_pos = list()
bubbles_speed = list()
bubbles_size = list()
bubbles_state = list()

# Display colored text in position X and Y
def display_text(text, color, font, font_size, x, y):

    myfont = pygame.font.SysFont(font, font_size, True)
    message = myfont.render(text, True, color)

    screen.blit(message, (x,y))
    
# Game Over Screen
def game_over_message():

    pygame.mixer.stop()

    lose_sound.play(0)

    screen.fill(DARK_BLUE)

    display_text("GAME OVER !", RED, 'Calibri', 40, SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.2 )

    message = "Ton Score : " +  str(score)
    display_text(message, RED, 'Calibri', 40, SCREEN_WIDTH * 0.37, SCREEN_HEIGHT * 0.4 )

    display_text("Appuie sur R pour rejouer !", WHITE, 'Calibri', 30, SCREEN_WIDTH * 0.33, SCREEN_HEIGHT * 0.6)

# Initialize game variables when restart
def init_game():
   global score, x_sub, y_sub, game_end, bubbles_pos, bubbles_size, bubbles_speed, bubbles_state

   game_end = time.time() + TIME_LIMIT
   score = 0
   x_sub = 40
   y_sub = 250
   bonus = 0

   bubbles_pos = list()
   bubbles_size = list()
   bubbles_speed = list()
   bubbles_state = list()

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

# The red bubble
red_bubble = pygame.image.load("ressources/red_bubble.png")

# The pop sound
pop_sound = pygame.mixer.Sound("ressources/collect.wav")

# Ambient music
ambient_sound = pygame.mixer.Sound("ressources/ambient_music.wav")
ambient_sound.set_volume(0.05)
lose_sound = pygame.mixer.Sound("ressources/lose.wav")

# Quit the game
def leave_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

# Update the screen display
def update_screen():
    screen.blit(background_image, (0,0))
    screen.blit(sub, (x_sub, y_sub))

    for i in range(len(bubbles_pos) - 1, -1, -1):
        if bubbles_state[i] == "Good":
            screen.blit(pygame.transform.scale(blue_bubble, (bubbles_size[i], bubbles_size[i])), bubbles_pos[i])
        else:
            screen.blit(pygame.transform.scale(red_bubble, (bubbles_size[i], bubbles_size[i])), bubbles_pos[i])

    message = "Score : " +  str(score)
    display_text (message, BLACK, 'Calibri', 20, 10, 15)

    # print ("Time : ", int(game_end - time.time()))

    message = "Time : " +  str(int(game_end - time.time()))
    display_text (message, BLACK, 'Calibri', 20, 600, 15)

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
def create_bubbles(state) :

    x_bubble = SCREEN_WIDTH
    y_bubble = random.randint(0,SCREEN_HEIGHT)

    if state == "Good":
        size_bubble = random.randint(blue_bubble.get_width() / 3, blue_bubble.get_width() * 2)

    else:
        size_bubble = random.randint(red_bubble.get_width(), red_bubble.get_width() * 3)

    size_bubble = random.randint(blue_bubble.get_width() / 3, blue_bubble.get_width() * 2)
    bubbles_size.append(size_bubble)

    bubbles_pos.append((x_bubble, y_bubble))
    bubbles_speed.append(random.randint(1, BUBBLE_MAX_SPEED))
    bubbles_state.append(state)

# Move the bubble on the screen with the specified speed
def move_bubbles():
    for i in range (len(bubbles_pos) - 1, -1, -1):
        bubbles_pos[i] = tuple(map(operator.sub, bubbles_pos[i], (bubbles_speed[i], 0)))

# Update the game
def update_game():

    global bonus, game_end
    
    if (random.randint(1, 20) == 1):
        create_bubbles("Good")

    if (random.randint(1, 50) == 1):
        create_bubbles("Bad")

    collision()

    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        game_end += TIME_LIMIT

    move_bubbles()
    clean_bubbles()

# Collision between the sub and the bubbles
def collision():

    global score, game_end
    
    for bubble in range(len(bubbles_pos) -1, -1, -1):
              if (x_sub < bubbles_pos[bubble][0] + bubbles_size[bubble]
          and x_sub + sub.get_width() > bubbles_pos[bubble][0]
          and y_sub < bubbles_pos[bubble][1] + bubbles_size[bubble]
          and y_sub + sub.get_height() > bubbles_pos[bubble][1]) :
                  #print ("La bulle ", bubble, "touche le sous-marin.")
                if bubbles_state[bubble] == "Good":
                    score += bubbles_size[bubble] + bubbles_speed[bubble]
                else:
                    game_end -= 5
                # print ("Score : ", score)
                pop_sound.play(0)
                delete_bubbles(bubble)

# Delete Bubble when it collides with the submarine
def delete_bubbles (bubble):

    del bubbles_state[bubble]
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

    pygame.mixer.stop()

    ambient_sound.play(-1)
    
    # Time loop
    while time.time() < game_end:
        update_game()
        update_screen()
    
        # Main Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leave_game()
        sub_control()
    game_over_message()
    pygame.display.flip()

    restart = False

    while not restart:

        # Event Manager Loop
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                leave_game()
            if not hasattr (event, 'key'):
                continue
            if event.key == K_r:
                restart = True
                init_game()

                
