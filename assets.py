import pygame


# loading assets
favicon = pygame.image.load('pipe.png')  # favicon
pygame.display.set_icon(favicon)
background = pygame.image.load('PlumrBGNew.png')
levelcomplete = pygame.image.load('lvlcomplete.png')
straight_pipe = pygame.image.load('StraightPipe.png')
t_pipe = pygame.image.load('TPipe.png')
plus_pipe = pygame.image.load('PlusPipe.png')
curve_pipe = pygame.image.load('CurvedPipe.png')
logo = pygame.image.load('Logo.png')

WIDTH, HEIGHT = 750, 450  # width: 900, height: 500
window = pygame.display.set_mode((WIDTH, HEIGHT))  # creating window
FPS = 60
COLOUR = (0, 0, 0)

#click_sound = pygame.mixer.Sound("Sound/M_Click.mp3")
