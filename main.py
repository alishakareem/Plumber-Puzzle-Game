import pygame
import tkinter as tk
import sys
from assets import *
from coordSetup import *
from controllers import *

pygame.init()  # initializing pygame

pygame.display.set_caption('Plumr')  # creating title of game


def main():
    pipe = curve_pipe
    CLOCK = pygame.time.Clock()
    # game loop
    running = True
    while running:
        CLOCK.tick(FPS)
        init_tiles()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if map_tile(pos) is not None:
                    tile_coordinates = map_tile(pos)
                    rotate_tile(tile_coordinates)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
