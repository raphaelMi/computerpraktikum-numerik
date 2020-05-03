import numpy as np
import pygame as pg
import init

def initialize():
    global screen
    global last_pos
    global clock

    screen = pg.display.set_mode((init.SCREEN_WIDTH, init.SCREEN_HEIGHT))
    pg.display.set_icon(init.APP_ICON)
    pg.display.set_caption(init.APP_TITLE)

    clock = pg.time.Clock()

    if init.MOUSE_FISH:
        last_pos = np.array(pg.mouse.get_pos())

def frame():
    global running

    clock.tick(init.FPS_CAP)
    screen.fill(init.BACKGROUND_COLOR)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    init.flock.do_frame(clock.get_time())

    if init.MOUSE_FISH:
        init.flock.positions[0] = np.array(pg.mouse.get_pos())
        init.flock.velocities[0] = clock.get_fps() * (init.flock.positions[0] - last_pos)
        # print(fish.positions[0], fish.velocities[0])
        last_pos[0] = init.flock.positions[0][0]
        last_pos[1] = init.flock.positions[0][1]

    for pos, vec in zip(init.flock.positions, init.flock.directions):
        pos1 = (pos + 10 * vec).astype(np.int32)
        pos2 = pos.astype(np.int32)
        pg.draw.line(screen, (0, 0, 0), pos1, pos2, 5)

    pg.display.update()

if __name__ == "__main__":
    global running

    initialize()

    running = True

    while running:
        frame()

