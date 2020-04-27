import numpy as np

BOUNCE = True


class Flock:
    def __init__(self, population=50):
        self.population = population

        self.positions = np.zeros((population, 2))
        self.velocities = np.zeros((population, 2))
        self.directions = np.zeros((population, 2))

        self.dimensions = (800, 600)

    def do_frame(self, millis=16.7):

        self.positions += millis/1000 * self.velocities
        self.directions = self.velocities / np.linalg.norm(self.velocities, axis=1, keepdims=True)

        if BOUNCE:
            for i, (x, y) in enumerate(self.positions):
                if x < 0 and self.velocities[i][0] < 0:
                    self.velocities[i][0] *= -1
                if y < 0 and self.velocities[i][1] < 0:
                    self.velocities[i][1] *= -1
                if x > self.dimensions[0] and self.velocities[i][0] > 0:
                    self.velocities[i][0] *= -1
                if y > self.dimensions[1] and self.velocities[i][1] > 0:
                    self.velocities[i][1] *= -1
