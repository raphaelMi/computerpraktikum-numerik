import cv2
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


def render_debug_information(tick_time, frame_time, event_time, video_time):
    fps = clock.get_fps()

    fps_surface = init.APP_FONT.render("FPS: {:.2}/{:}".format(fps, init.FPS_CAP), False, (0, 0, 0))
    tick_time_surface = init.APP_FONT.render("Tick time: {:} ms".format(tick_time), False, (0, 0, 0))
    frame_time_surface = init.APP_FONT.render("Frame time: {:} ms".format(frame_time), False, (0, 0, 0))
    event_time_surface = init.APP_FONT.render("Event time: {:} ms".format(event_time), False, (0, 0, 0))
    if not init.REALTIME:
        video_process_time_surface = init.APP_FONT.render("Video process time: {:} ms".format(video_time), False,
                                                          (0, 0, 0))
        rendered_video_frames_surface = init.APP_FONT.render(
            "Rendered video frames: {:} (equals {:.2f} s)".format(rendered_video_frames,
                                                                  init.FPS_CAP ** -1 * rendered_video_frames), False,
            (0, 0, 0))
    fish_count_surface = init.APP_FONT.render("Fish count: {:}".format(init.flock.population), False, (0, 0, 0))

    y = 0

    screen.blit(fps_surface, (0, y))
    y += 25

    screen.blit(tick_time_surface, (0, y))
    y += 25

    screen.blit(frame_time_surface, (0, y))
    y += 25

    screen.blit(event_time_surface, (0, y))
    y += 25

    if not init.REALTIME:
        screen.blit(video_process_time_surface, (0, y))
        y += 25
        screen.blit(rendered_video_frames_surface, (0, y))
        y += 25

    screen.blit(fish_count_surface, (0, y))
    y += 25


def frame():
    global running
    global pretty_render
    global display_debug_screen
    global display_bounding_boxes
    global rendered_video_frames

    clock.tick(init.FPS_CAP)

    event_time_start = pg.time.get_ticks()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_m:
                pretty_render = not pretty_render
            elif event.key == pg.K_d:
                display_debug_screen = not display_debug_screen
            elif event.key == pg.K_b:
                display_bounding_boxes = not display_bounding_boxes

    event_time = pg.time.get_ticks() - event_time_start

    tick_time_start = pg.time.get_ticks()

    delta = clock.get_time()

    if not init.REALTIME:
        delta = 1000.0 / init.FPS_CAP

    init.flock.do_frame(delta)

    if init.MOUSE_FISH:
        init.flock.positions[0] = np.array(pg.mouse.get_pos())
        init.flock.velocities[0] = clock.get_fps() * (init.flock.positions[0] - last_pos)
        # print(fish.positions[0], fish.velocities[0])
        last_pos[0] = init.flock.positions[0][0]
        last_pos[1] = init.flock.positions[0][1]

    tick_time = pg.time.get_ticks() - tick_time_start

    frame_time_start = pg.time.get_ticks()

    screen.fill(init.BACKGROUND_COLOR)

    for pos, dir in zip(init.flock.positions, init.flock.directions):

        # Compute those only when needed, improves performance a lot
        if not pretty_render or display_bounding_boxes:
            perp3d = np.cross((dir[0], dir[1], 0), (0, 0, 1))  # Perpendicular to direction vector
            perp2d = (perp3d[0], perp3d[1]) / np.linalg.norm(perp3d)  # 2d version of that one

            # Vertices of rectangle representing fish boundaries
            r_1 = pos - dir * init.FISH_WIDTH / 2 - perp2d * init.FISH_HEIGHT / 2
            r_2 = r_1 + perp2d * init.FISH_HEIGHT
            r_3 = r_2 + dir * init.FISH_WIDTH
            r_4 = r_1 + dir * init.FISH_WIDTH

        if pretty_render:
            angle_deg = np.rad2deg(np.arctan2(np.dot((1, 0), dir), dir[1])) + 90
            screen.blit(pg.transform.rotate(pg.transform.flip(init.FISH_SPRITE, True, abs(angle_deg) > 90), angle_deg),
                        pos + (-init.FISH_WIDTH / 2))
        else:
            pg.draw.polygon(screen, init.FISH_COLOR, (r_1, r_2, r_3, r_4))  # PyGame doesn't support non AA rectangles
            pg.draw.line(screen, init.FISH_DIRECTION_COLOR, pos.astype(np.int32),
                         pos.astype(np.int32) + dir * init.FISH_WIDTH, 2)

        if display_bounding_boxes:
            pg.draw.line(screen, init.FISH_BOUNDING_BOX_COLOR, r_1, r_2)
            pg.draw.line(screen, init.FISH_BOUNDING_BOX_COLOR, r_2, r_3)
            pg.draw.line(screen, init.FISH_BOUNDING_BOX_COLOR, r_1, r_4)
            pg.draw.line(screen, init.FISH_BOUNDING_BOX_COLOR, r_3, r_4)
            pg.draw.circle(screen, init.FISH_CENTER_POINT_COLOR, pos.astype(np.int32), 1)

    frame_time = pg.time.get_ticks() - frame_time_start

    video_process_time = 0

    if not init.REALTIME:
        video_process_time_start = pg.time.get_ticks()

        video.write(np.frombuffer(pg.image.tostring(screen.copy(), "RGB"), np.uint8).reshape(init.SCREEN_HEIGHT,
                                                                                             init.SCREEN_WIDTH, 3))
        rendered_video_frames += 1

        video_process_time = pg.time.get_ticks() - video_process_time_start

    if display_debug_screen:
        render_debug_information(tick_time, frame_time, event_time, video_process_time)

    pg.display.update()


if __name__ == "__main__":
    global running
    global pretty_render
    global display_debug_screen
    global display_bounding_boxes
    global video
    global rendered_video_frames

    initialize()

    running = True
    pretty_render = True
    display_debug_screen = True
    display_bounding_boxes = False
    rendered_video_frames = 0

    if not init.REALTIME:
        video = cv2.VideoWriter(init.EXPORTED_VIDEO_NAME, cv2.VideoWriter_fourcc('Y', 'V', '1', '2'), init.FPS_CAP,
                                (init.SCREEN_WIDTH, init.SCREEN_HEIGHT))

    while running:
        frame()

    # Save video
    cv2.destroyAllWindows()
    video.release()
