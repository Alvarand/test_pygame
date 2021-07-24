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
        self.move = False
        self.left = False
        self.right = False
        self.is_jump = False
        self.jump_speed = 10
        self.anim_count = 0
        self.image = player_stay
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x_c, y_c)
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

    def get_keys(self):
        keys = pygame.key.get_pressed()
        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
        else:
            if self.jump_speed >= -10:
                if self.jump_speed > 0:
                    self.rect.y -= (self.jump_speed ** 2) // 3
                else:
                    self.rect.y += (self.jump_speed ** 2) // 3
                self.jump_speed -= 1
            else:
                self.is_jump = False
                self.jump_speed = 10
        if keys[pygame.K_d]:
            self.left = False
            self.right = True
            self.anim_count += 3
            player1.rect.x += 5
            if player1.rect.right > WIDTH:
                player1.rect.right = WIDTH
        elif keys[pygame.K_a]:
            self.left = True
            self.right = False
            self.anim_count += 3
            player1.rect.x -= 5
            if player1.rect.left < 0:
                player1.rect.left = 0
        else:
            self.left = False
            self.right = False

    def draw(self):
        if self.anim_count >= 60:
            self.anim_count = 0
        if self.is_jump:
            self.image = player_jump
        elif self.left:
            self.image = pygame.transform.flip(player_walk[self.anim_count // 6], True, False)
        elif self.right:
            self.image = player_walk[self.anim_count // 6]
        else:
            self.image = player_stay
        screen.blit(bg_img, (0, 0))
        self.image.set_colorkey(BLACK)
        screen.blit(self.image, (self.rect.x, self.rect.y))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()
bg_img = pygame.image.load(os.path.join(img_folder, 'bg_shroom.png'))
player_stay = pygame.image.load(os.path.join(img_folder, 'p1_front.png')).convert()
player_jump = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()
player_walk = [pygame.image.load(os.path.join(img_folder, 'p1_walk01.png')).convert(),
               pygame.image.load(os.path.join(img_folder, 'p1_walk02.png')).convert(),
               pygame.image.load(os.path.join(img_folder, 'p1_walk03.png')).convert(),
               pygame.image.load(os.path.join(img_folder, 'p1_walk04.png')).convert(),
               pygame.image.load(os.path.join(img_folder, 'p1_walk05.png')).convert(),
               pygame.image.load(os.path.join(img_folder, 'p1_walk06.png')).convert(),
               pygame.image.load(os.path.join(img_folder, 'p1_walk07.png')).convert(),
               pygame.image.load(os.path.join(img_folder, 'p1_walk08.png')).convert(),
               pygame.image.load(os.path.join(img_folder, 'p1_walk09.png')).convert(),
               pygame.image.load(os.path.join(img_folder, 'p1_walk10.png')).convert()
               ]
player1 = Player(0, 420)
# player2 = Player(200, 300)

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    player1.get_keys()
    player1.draw()
    pygame.display.flip()

pygame.quit()
