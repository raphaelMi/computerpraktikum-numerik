# Readme file for the flock simulator
## Keybinds:
* M: Switch between pretty and primitive display mode
* D: Toggle the debug screen visibility
* G: Toggle plot visibility
* B: Toggle center point and bounding box visibility
* F: Toggle cursor treated as fish
* S: Toggle cursor treated as shark
* K: Show plot of deviation in velocity, not usable with G.

## Modes:
* Realtime: Set it to false to export the rendered scene to a video with stable FPS, it'll be saved at `rendered_scene.avi` (by default)

## Configuration
* Via init.py you can customize the whole program
* If you have problems with matplotlib, try to increase the `PLOT_PAUSE_TIME`

## Conflicting configuration options:
* Cursor as fish and as shark at the same time can cause glitches
* Don't show the deviation plot while the velocity plot is open

## Dependencies:
* pygame (window and game loop)
* numpy
* matplotlib (plotting)
* open_cv (for video rendering)
