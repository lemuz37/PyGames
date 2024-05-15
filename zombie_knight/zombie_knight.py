import pygame, random

#Use 2d vectors
vector = pygame.math.Vector2

#Initialize pygame
pygame.init()

#Set display surface (tile size 32x32 = 40 tiles wide, 736/32 = 23 tiles tall)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Knight")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#The main game loop
running_game = True
while running_game:
    #Check to see if player wants to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

    #Fill screen
    display_surface.fill((0, 0, 0))

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS) 
#Exit game
pygame.quit()