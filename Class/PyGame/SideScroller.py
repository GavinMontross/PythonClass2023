import pygame
import math
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
fps = 60

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        self.index = 0
        self.counter = 0
        self.direction = 1
        self.jumped = False

        for num in range(1, 6):
            image = pygame.image.load(f'Python/PyGame/Assets/run{num}.png')
            image = pygame.transform.scale(image, (100, 160))
            self.images.append(image)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel_y = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100

    def update(self):
        dy = 0
        key = pygame.key.get_pressed()

        # Reset self.jumped when player is on the ground
        if self.rect.bottom == 700:  # Assuming 300 is the ground level
            self.jumped = False

        if key[pygame.K_SPACE] and not self.jumped:
            self.vel_y = -20
            self.jumped = True

        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.index += 1
            self.last_update = current_time
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

        # Apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        if self.rect.bottom + dy > 700:
            dy = 700 - self.rect.bottom

        self.rect.y += dy

        screen.blit(self.image, self.rect)

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sidescroller")

# Load background image
bg = pygame.image.load('Python/PyGame/Assets/city.png').convert()
bg_width = bg.get_width()
bg_height = bg.get_height()

# Define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
player = Player(100, SCREEN_HEIGHT - 300)
run = True
last_update = pygame.time.get_ticks()
animation_cooldown = 100
GRAVITY = 0.75
while run:
    clock.tick(fps)

    # Draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    # Scroll background
    scroll -= 5

    # Show Player
    player.update()
    pygame.display.update()
    # Reset Scroll
    if abs(scroll) > bg_width:
        scroll = 0

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
