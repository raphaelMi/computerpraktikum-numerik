import pygame as pg

from cucker_smale import *

pg.font.init()  # Init font module so we can create a font here

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS_CAP = 60
BACKGROUND_COLOR = (255, 255, 255,)

MOUSE_FISH = False  # makes the mouse cursor behave like a fish

# Image by https://pixabay.com/illustrations/clipart-fish-sea-water-swim-3418189/
fish_image = pg.image.load('fish.png')

APP_ICON = fish_image
APP_TITLE = "Flocking Simulation ({:}x{:})".format(SCREEN_WIDTH, SCREEN_HEIGHT)
APP_FONT = pg.font.SysFont('Comic Sans MS', 20)

flock = Flock(50)
flock.positions = np.random.normal((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 50, (flock.population, 2))
flock.velocities = np.random.normal((0, 0), 100, (flock.population, 2))
flock.dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)
