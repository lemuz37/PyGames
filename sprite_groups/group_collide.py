import pygame, random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Group Collide!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Define classes
class Game():
    def __init__(self, monster_group, knight_group):
        self.monster_group = monster_group
        self.knight_group = knight_group

    def update(self):
        self.check_collisions()
    
    def check_collisions(self):
        pygame.sprite.groupcollide(self.monster_group, self.knight_group, True, False)


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprite_groups\Blue_Monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        self.rect.y += self.velocity

class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprite_groups\Knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        self.rect.y -= self.velocity

#Create a monster group
my_monster_group = pygame.sprite.Group()
for i in range(12):
    monster = Monster(i* 64, 10)
    my_monster_group.add(monster)

my_knight_group = pygame.sprite.Group()
for i in range(12):
    knight = Knight(i*64, WINDOW_HEIGHT - 64)
    my_knight_group.add(knight)

my_game = Game(my_monster_group, my_knight_group)

#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill screen
    display_surface.fill((0, 0, 0))

    #Update and draw sprite groups
    my_monster_group.update()
    my_monster_group.draw(display_surface)

    my_knight_group.update()
    my_knight_group.draw(display_surface)

    #Update the game
    my_game.update()
    
    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End game
pygame.quit()