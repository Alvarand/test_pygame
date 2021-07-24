from config import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.right = True
        self.step = 5
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.bottom = 200, 512

    def move(self):
        if self.step > 0:
            self.right = True
        else:
            self.right = False
        if self.right:
            self.image = pygame.transform.flip(enemy_img, True, False)
        else:
            self.image = enemy_img
        self.rect.x += self.step
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.step = -self.step

    def draw(self):
        self.move()
        self.image.set_colorkey(BLACK)
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.move = False
        self.left = False
        self.right = False
        self.is_jump = False
        self.jump_speed = 10
        self.anim_count = 0
        self.image = player_stay
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.bottom = (x, y)
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
                    self.rect.y -= (self.jump_speed ** 2) // 2
                else:
                    self.rect.y += (self.jump_speed ** 2) // 2
                self.jump_speed -= 1
            else:
                self.is_jump = False
                self.jump_speed = 10
        if keys[pygame.K_d]:
            self.left = False
            self.right = True
            self.anim_count += 3
            self.rect.x += 5
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
        elif keys[pygame.K_a]:
            self.left = True
            self.right = False
            self.anim_count += 3
            self.rect.x -= 5
            if self.rect.left < 0:
                self.rect.left = 0
        else:
            self.left = False
            self.right = False

    def check_enemy(self, enemy):
        self.get_keys()
        if self.rect.right > enemy.rect.left:
            self.rect.right = enemy.rect.left - 3
        # if self.rect.bottom < enemy.rect.top and self.rect.right < enemy.rect.left:
        #     self.rect.bottom = enemy.rect.top
        #     self.is_jump = False

    def draw(self):
        if self.anim_count >= 60:
            self.anim_count = 0
        if self.is_jump:
            if self.left:
                self.image = pygame.transform.flip(player_jump, True, False)
            else:
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
