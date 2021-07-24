import pygame
import random
import os

WIDTH = 1024
HEIGHT = 512
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


class Player(pygame.sprite.Sprite):

    def __init__(self, x_c, y_c):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x_c, y_c)
        self.step_x = random.randint(1, 10)
        self.step_y = random.randint(1, 10)

    def update(self):
        self.rect.x += self.step_x
        self.rect.y += self.step_y
        if self.rect.right > WIDTH:
            self.step_x = -self.step_x
        if self.rect.left < 0:
            self.step_x = -self.step_x
        if self.rect.bottom > HEIGHT:
            self.step_y = -self.step_y
        if self.rect.top < 0:
            self.step_y = -self.step_y


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()
bg_img = pygame.image.load(os.path.join(img_folder, 'bg_shroom.png'))
player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()
all_sprites = pygame.sprite.Group()
player1 = Player(100, 400)
# player2 = Player(200, 300)
all_sprites.add(player1)

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.rect.y -= 3
        if player1.rect.top < 0:
            player1.rect.top = 0
    if keys[pygame.K_d]:
        player1.rect.x += 3
        if player1.rect.right > WIDTH:
            player1.rect.right = WIDTH
    if keys[pygame.K_s]:
        player1.rect.y += 3
        if player1.rect.bottom > HEIGHT:
            player1.rect.bottom = HEIGHT
    if keys[pygame.K_a]:
        player1.rect.x -= 3
        if player1.rect.left < 0:
            player1.rect.left = 0
    if keys[pygame.K_SPACE]:
        y = player1.rect.y

        # all_sprites.update()
    # screen.fill(BLUE)
    screen.blit(bg_img, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
