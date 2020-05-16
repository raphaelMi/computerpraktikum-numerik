import pygame as pg

from cucker_smale import *

pg.font.init()  # Init font module so we can create a font here

# Image by https://pixabay.com/illustrations/clipart-fish-sea-water-swim-3418189/
fish_icon = pg.image.load('fish_icon.png')
fish_sprite = pg.image.load('fish_sprite.png')  # Scaled, and cut out

# General display properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS_CAP = 60

REALTIME = True  # If false, the rendered frames will be saved and merged into a video with constant FPS_CAP framerate

EXPORTED_VIDEO_NAME = "rendered_scene.avi"

APP_ICON = fish_icon
APP_TITLE = "Flocking Simulation ({:}x{:})".format(SCREEN_WIDTH, SCREEN_HEIGHT)
APP_FONT = pg.font.SysFont('Comic Sans MS', 20)

BACKGROUND_COLOR = (255, 255, 255,)

SHOW_PLOTS_INITIALLY = True # Open plot window with program start

PLOT_WINDOW_TITLE = "Plots of simulation data"

# Fish-specific settings
FISH_WIDTH = 28
FISH_HEIGHT = 10

# Fish boundary colors
FISH_CENTER_POINT_COLOR = (255, 0, 0)
FISH_BOUNDING_BOX_COLOR = (0, 255, 0)

# Primitive fish rendering
FISH_COLOR = (84, 84, 84)
FISH_DIRECTION_COLOR = (0, 0, 255)

# Pretty fish rendering
FISH_SPRITE = pg.transform.smoothscale(fish_sprite, (FISH_WIDTH, FISH_HEIGHT))

# Flock settings

FLOCKS = []

flock1 = Flock(15)
flock1.positions = np.random.normal((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 25, (flock1.population, 2))
flock1.velocities = np.random.normal((0, 0), 45, (flock1.population, 2))
flock1.dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)

flock2 = Flock(30)
flock2.positions = np.random.normal((SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2 + 100), 45, (flock2.population, 2))
flock2.velocities = np.random.normal((0, 0), 56, (flock2.population, 2))
flock2.dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)
flock2.color = (150, 0, 0, 255)

flock3 = Flock(15)
flock3.positions = np.random.normal((SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 100), 53, (flock3.population, 2))
flock3.velocities = np.random.normal((0, 0), 76, (flock3.population, 2))
flock3.dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)
flock3.color = (46, 23, 0, 121)

FLOCKS.append(flock1)
FLOCKS.append(flock2)
FLOCKS.append(flock3)

MOUSE_FISH = True  # makes the mouse cursor behave like a fish
MOUSE_FISH_FLOCK = flock1  # The flock influenced by the mouse
