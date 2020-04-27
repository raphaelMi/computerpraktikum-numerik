# Simulation of Flocking

import numpy as np
import pygame as pg

screen = pg.display.set_mode((800,800))

# Image by https://pixabay.com/illustrations/clipart-fish-sea-water-swim-3418189/
fish_image = pg.image.load('fish.png')
pg.display.set_icon(fish_image)

running = True
while running:
    screen.fill((255, 255, 255,))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    pg.display.update()