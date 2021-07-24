import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    def __init__(self, x_c, y_c, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x_c, y_c)

    def update(self):

        self.rect.x += self.x
        self.rect.y += self.y
        if self.rect.right > WIDTH:
            self.x = -self.x
        if self.rect.left < 0:
            self.x = -self.x
        if self.rect.bottom > HEIGHT:
            self.y = -self.y
        if self.rect.top < 0:
            self.y = -self.y


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player1 = Player(100, 400, WHITE)
player2 = Player(200, 300, RED)
all_sprites.add(player1, player2)
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
