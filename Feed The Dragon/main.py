import pygame, random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

#Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50 , 10)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0 , 255)

#Set fonts
font = pygame.font.Font("Feed The Dragon\AttackGraffiti.ttf", 32)

#Set text
score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed The Dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.center = ((WINDOW_WIDTH//2, 30))

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAME OVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, (WINDOW_HEIGHT//2 + 32))

#Set sound and music
coin_sound = pygame.mixer.Sound("Feed The Dragon\coin_sound.wav")
miss_sound = pygame.mixer.Sound("Feed The Dragon\miss_sound.wav")
miss_sound.set_volume(.2)
pygame.mixer.music.load('Feed The Dragon\music.wav')

#Set images
player_image = pygame.image.load("Feed The Dragon\dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2

coin_image = pygame.image.load("Feed The Dragon\coin.png")
coin_rect = player_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)


#The main loop
pygame.mixer.music.play(-1, 0.0)
running = True

while running:

    #Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Get a list of all keys currently being pressed on
    keys = pygame.key.get_pressed()

    #Move the dragon continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_rect.left > 0:
        player_rect.x -= PLAYER_VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_rect.right < WINDOW_WIDTH:
        player_rect.x += PLAYER_VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_rect.top > 64:
        player_rect.y -= PLAYER_VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY

    #Move the coin
    if coin_rect.x < 0:
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        #Move the coin
        coin_rect.x -= coin_velocity

    #Check for collisions
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

    #Update HUD
    score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
    lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)

    #Check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #Pause the game until the player presses a key, then reset game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
                #Check to see if user wants to quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT//2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #Fill the display
    display_surface.fill(BLACK)

    #Blit the HUD to screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0, 64), (WINDOW_WIDTH, 64), 2)

    #Blit assets to screen
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)

    #Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#Quit the game
pygame.quit()