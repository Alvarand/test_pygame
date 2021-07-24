import os
import pygame
import random

running = True
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
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()
bg_img = pygame.image.load(os.path.join(img_folder, 'bg_shroom.png')).convert()
enemy_img = pygame.image.load(os.path.join(img_folder, 'pokerMad.png')).convert()
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
