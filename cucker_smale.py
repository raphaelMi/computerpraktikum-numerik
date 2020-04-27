import numpy as np


class Flock:
    def __init__(self, population=50):
        self.population = population

        self.positions = np.zeros((population, 2), dtype=np.int32)
        self.velocities = np.zeros((population, 2))

    def do_frame(self, millis=16.7):
        self.positions += millis/1000 * self.velocities
