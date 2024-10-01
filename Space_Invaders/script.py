import pygame
from pygame import mixer
from pygame.locals import *
import random


pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

#define fps
clock = pygame.time.Clock()
fps = 60


screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

#define fonts
font30 = pygame.font.SysFont('Constantia', 30)
font40 = pygame.font.SysFont('Constantia', 40)



#load sounds
mixer.music.load("img/bensound_summer_bg.ogg")
mixer.music.set_volume(0.30)
mixer.music.play()

explosion_fx = pygame.mixer.Sound("img/explosion.wav")
explosion_fx.set_volume(0.25)

explosion2_fx = pygame.mixer.Sound("img/explosion2.wav")
explosion2_fx.set_volume(0.25)

laser_fx = pygame.mixer.Sound("img/laser.wav")
laser_fx.set_volume(0.25)

#define game variables
rows = 5
cols = 5
alien_cooldown = 1000 #bullet cooldown in milliseconds
last_alien_shot = pygame.time.get_ticks()
countdown = 3
last_count = pygame.time.get_ticks()
game_over = 0 #0 is no game over, 1 means player has won, -1 means player has lost


#define colors
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)


#load image
bg = pygame.image.load("img/bg.png")

def draw_bg():
    screen.blit(bg, (0, 0))

#define function for creating text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))