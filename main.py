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


def render_debug_information(tick_time, frame_time):
    fps = clock.get_fps()

    fps_surface = init.APP_FONT.render("FPS: {:.2}/{:}".format(fps, init.FPS_CAP), False, (0, 0, 0))
    tick_time_surface = init.APP_FONT.render("Tick time: {:} ms".format(tick_time), False, (0, 0, 0))
    frame_time_surface = init.APP_FONT.render("Frame time: {:} ms".format(frame_time), False, (0, 0, 0))
    fish_count_surface = init.APP_FONT.render("Fish count: {:}".format(init.flock.population), False, (0, 0, 0))

    screen.blit(fps_surface, (0, 0))
    screen.blit(tick_time_surface, (0, 25))
    screen.blit(frame_time_surface, (0, 50))
    screen.blit(fish_count_surface, (0, 75))


def frame():
    global running

    clock.tick(init.FPS_CAP)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    tick_time_start = pg.time.get_ticks()

    screen.fill(init.BACKGROUND_COLOR)

    init.flock.do_frame(clock.get_time())

    if init.MOUSE_FISH:
        init.flock.positions[0] = np.array(pg.mouse.get_pos())
        init.flock.velocities[0] = clock.get_fps() * (init.flock.positions[0] - last_pos)
        # print(fish.positions[0], fish.velocities[0])
        last_pos[0] = init.flock.positions[0][0]
        last_pos[1] = init.flock.positions[0][1]

    tick_time = pg.time.get_ticks() - tick_time_start

    frame_time_start = pg.time.get_ticks()

    for pos, vec in zip(init.flock.positions, init.flock.directions):
        pos1 = (pos + 10 * vec).astype(np.int32)
        pos2 = pos.astype(np.int32)
        pg.draw.line(screen, (0, 0, 0), pos1, pos2, 5)

    frame_time = pg.time.get_ticks() - frame_time_start

    render_debug_information(tick_time, frame_time)

    pg.display.update()


if __name__ == "__main__":
    global running

    initialize()

    running = True

    while running:
        frame()
