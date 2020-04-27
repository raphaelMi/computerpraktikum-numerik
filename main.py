# Simulation of Flocking

import numpy as np
import pygame as pg

from cucker_smale import Flock

screen_x = 800
screen_y = 600

screen = pg.display.set_mode((screen_x, screen_y))

# Image by https://pixabay.com/illustrations/clipart-fish-sea-water-swim-3418189/
fish_image = pg.image.load('fish.png')
pg.display.set_icon(fish_image)

fish = Flock()
fish.positions = np.random.normal((screen_x/2, screen_y/2), 100, (fish.population, 2))
fish.velocities = np.random.normal((0, 0), 1, (fish.population, 2))
print(fish.positions)

running = True
while running:
    screen.fill((255, 255, 255,))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    fish.do_frame()
    for pos in fish.positions:
        pg.draw.circle(screen, (127, 127, 127), pos.astype(np.int32), 4)
        pg.draw.circle(screen, (0, 0, 0), pos.astype(np.int32), 3)

    pg.display.update()