# Simulation of Flocking

import numpy as np
import pygame as pg

from cucker_smale import Flock

screen_x = 800
screen_y = 600

MOUSE_FISH = False  # makes the mouse cursor behave like a fish

screen = pg.display.set_mode((screen_x, screen_y))

# Image by https://pixabay.com/illustrations/clipart-fish-sea-water-swim-3418189/
fish_image = pg.image.load('fish.png')
pg.display.set_icon(fish_image)
pg.display.set_caption("Flocking simulator")

fish = Flock(50)
fish.positions = np.random.normal((screen_x/2, screen_y/2), 50, (fish.population, 2))
fish.velocities = np.random.normal((0, 0), 100, (fish.population, 2))
fish.dimensions = (screen_x, screen_y)

if MOUSE_FISH:
    last_pos = np.array(pg.mouse.get_pos())

running = True
clock = pg.time.Clock()
while running:
    clock.tick(120)
    screen.fill((255, 255, 255,))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    fish.do_frame(clock.get_time())
    # print(clock.get_fps())

    if MOUSE_FISH:
        fish.positions[0] = np.array(pg.mouse.get_pos())
        fish.velocities[0] = clock.get_fps() * (fish.positions[0] - last_pos)
        # print(fish.positions[0], fish.velocities[0])
        last_pos[0] = fish.positions[0][0]
        last_pos[1] = fish.positions[0][1]

    for pos, vec in zip(fish.positions, fish.directions):
        pos1 = (pos + 10 * vec).astype(np.int32)
        pos2 = pos.astype(np.int32)
        pg.draw.line(screen, (0, 0, 0), pos1, pos2, 5)

    pg.display.update()
