import pygame
#Use pygame.math.Vector3 to create 3D vectors
vector = pygame.math.Vector3

#Initialize pygame
pygame.init()

SPRITE_WIDTH = 32
SPRITE_HEIGHT = 32
TRANSFORM_I_HAT = vector(0.5 * (SPRITE_WIDTH), 0.25 * (SPRITE_HEIGHT), 0)
TRANSFORM_J_HAT = vector(-0.5  * (SPRITE_WIDTH), 0.25 * (SPRITE_HEIGHT), 0)
DETERMENANT = (1 / ((TRANSFORM_I_HAT.x * TRANSFORM_J_HAT.y) - (TRANSFORM_I_HAT.y * TRANSFORM_J_HAT.x)))

#Set display surface
#Set display surface tile size is 32x32 so 960/32 = 30 tiles wide, 640/32 = 20 tiles high
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pixel Chef")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Define classes
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, group, sub_group=''):
        super().__init__()
        if sub_group:
            pass
        else:
            self.image  =pygame.image.load('pixel_chef\Tiles\\tile(0).png')
            self.tile_isometric_position = self.transform_cartesian_to_isometric(vector(x, y, 0))
        group.add(self)
        #Get the rect of the image and position within the grid
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
    
    def transform_cartesian_to_isometric(self, cartesian_coordinates):
        isometric_coordinates = vector(0, 0, 0)
        isometric_coordinates.x = cartesian_coordinates.x * TRANSFORM_I_HAT.x + cartesian_coordinates.y * TRANSFORM_J_HAT.x
        isometric_coordinates.y = cartesian_coordinates.x * TRANSFORM_I_HAT.y + cartesian_coordinates.y * TRANSFORM_J_HAT.y
        print("("+ str(cartesian_coordinates.x)+ ", "+ str(cartesian_coordinates.y) + ") ===> ("+ str(isometric_coordinates.x)+ ", "+ str(isometric_coordinates.y) + ")")
        return isometric_coordinates


    # def transform_isometric_to_cartesian(self, isometric_coordinates):
    #     cartesian_coordinates = vector(0, 0, 0)
    #     cartesian_coordinates.x = (isometric_coordinates.x - isometric_coordinates.y) / TRANSFORM_I_HAT.x
    #     cartesian_coordinates.y = (isometric_coordinates.x + isometric_coordinates.y) / TRANSFORM_I_HAT.y
    #     cartesian_coordinates.z = isometric_coordinates.z
    #     return cartesian_coordinates

main_tile_group = pygame.sprite.Group()
    
#Tile size is 32x32 so 960/32 = 30 tiles wide, 640/32 = 20 tiles high
tile_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#Create individual Tile objects from the tile map
# Loop through the 20 lists in tile map (i moves us down the map)
for i in range(len(tile_map)):
    for j in range(len(tile_map[0])):
        if tile_map[i][j] == 0:
            Tile(j*SPRITE_HEIGHT, i * SPRITE_WIDTH, main_tile_group)

#Main game loop()
running_game = True
while running_game:
    #Check to see if the player wants to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

    #Fill the screen
    display_surface.fill((0, 0, 0))

    #Draw tiles
    main_tile_group.draw(display_surface)
    main_tile_group.update()

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#Exit the game
pygame.quit()