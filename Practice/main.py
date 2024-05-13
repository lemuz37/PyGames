import pygame, random

#Initialize pygame
pygame.init()

#Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello World!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 5

#Load sound effects
# sound_1 = pygame.mixer.Sound('sound_1.wav')
# sound_2 = pygame.mixer.Sound('sound_2.wav')

# #Play the sound effects
# sound_1.play()
# pygame.time.delay(2000)
# sound_2.play()
# pygame.time.delay(2000)

# #Change the volume of a soud effect
# sound_1.set_volume(.50)
# sound_1.play()

# #Load background music
# pygame.mixer.music.load('music.wav')

# #Play and stop the music
# pygame.mixer.music.play(-1, 0.0)
# pygame.time.delay(1000)
# sound_2.play()
# pygame.time.delay(5000)
# pygame.mixer.music.stop()

# Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50 , 10)
BLUE = (0, 0 , 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0 , 255)

#See all available fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

# #Define fonts
# system_font = pygame.font.SysFont('calibri', 32)
# custom_font = pygame.font.Font('AttackGraffiti.ttf', 32)

# #Define text
# system_text = system_font.render("Dragons Rule!", True, GREEN, DARKGREEN)
# system_text_rect = system_text.get_rect()
# system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# custom_text = custom_font.render("Move the dragon soon!", True, GREEN)
# custom_text_rect = custom_text.get_rect()
# custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

# #Create images... returns a Surface object with the image drawn on it.
# #We can then get the rect of the surface and use the rect to position the image.
# dragon_left_image = pygame.image.load("dragon_left.png")
# dragon_left_rect = dragon_left_image.get_rect()
# dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

coin_image = pygame.image.load('coin.png')
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH//2 - 200, WINDOW_HEIGHT//2)

# #Give a background color to the display
# display_surface.fill(BLUE)

# #Draw various shapes on our display
# #Line(surface, color, starting point, ending point, thickness)
# pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
# pygame.draw.line(display_surface, GREEN, (200, 300), (100, 100), 1)

# #Circle(surface, color, center, radius, thickness...0 for fill)
# pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
# pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 50, 6)

# #Rectangle(surface, color, (top-left x, top-left y, width, height))
# pygame.draw.rect(display_surface, MAGENTA, (500, 0, 100, 100))
# pygame.draw.rect(display_surface, CYAN, (500, 100, 50, 100))

#The main game loop
running = True
while running:
    #Loop through a list of Event objects that have occured
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get a list of all keys currently being pressed on
    keys = pygame.key.get_pressed()

    #Move the dragon continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_right_rect.left > 0:
        dragon_right_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_right_rect.right < WINDOW_WIDTH:
        dragon_right_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_right_rect.top > 0:
        dragon_right_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_right_rect.bottom < WINDOW_HEIGHT:
        dragon_right_rect.y += VELOCITY

        # #Move based on mouse clicks
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print(event)
        #     mouse_x = event.pos[0]
        #     mouse_y = event.pos[1]
        #     dragon_right_rect.centerx = mouse_x
        #     dragon_right_rect.centery = mouse_y

        # #Drag the object when the mouse button is clicked
        # if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
        #     print(event)
        #     mouse_x = event.pos[0]
        #     mouse_y = event.pos[1]
        #     dragon_right_rect.centerx = mouse_x
        #     dragon_right_rect.centery = mouse_y

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         dragon_right_rect.x -= VELOCITY 
        #     if event.key == pygame.K_RIGHT:
        #         dragon_right_rect.x += VELOCITY
        #     if event.key == pygame.K_UP:
        #         dragon_right_rect.y -= VELOCITY
        #     if event.key == pygame.K_DOWN:
        #         dragon_right_rect.y += VELOCITY

    if dragon_right_rect.colliderect(coin_rect):
        print('Hit!')
        coin_rect.x = random.randint(0, WINDOW_WIDTH - 48)
        coin_rect.y = random.randint(0, WINDOW_HEIGHT - 48)


    #Fill the display to cover old images
    display_surface.fill((0, 0, 0))

    #Draw rectangles to represent the rects of each object
    pygame.draw.rect(display_surface, (GREEN), dragon_right_rect, 1)
    pygame.draw.rect(display_surface, (YELLOW), coin_rect, 1)



    # display_surface.blit(system_text, system_text_rect)
    # display_surface.blit(custom_text, custom_text_rect)

    # #Blit a surface object at the given coordinates to our display
    # display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    display_surface.blit(coin_image, coin_rect)


    # pygame.draw.line(display_surface, (255, 255, 255),(0, 75), (WINDOW_WIDTH, 75), 4)

    #Update the display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)

#End the game
pygame.quit()