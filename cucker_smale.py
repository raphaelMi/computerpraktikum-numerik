import numpy as np

TORUS_WORLD = True
LAMBDA = 10
LENGTH_FACTOR = 25


class Flock:
    def __init__(self, population=50):
        self.population = population

        self.positions = np.zeros((population, 2))
        self.velocities = np.zeros((population, 2))
        self.directions = np.zeros((population, 2))

        self.dimensions = (800, 600)
        self.color = (0, 0, 0, 255)

    def do_frame(self, millis=16.7):
        psi = np.array([[(vel_i - vel_j) / (1 + 1 / LENGTH_FACTOR ** 2 * np.linalg.norm(pos_i - pos_j) ** 2)
                         for pos_i, vel_i in zip(self.positions, self.velocities)]
                        for pos_j, vel_j in zip(self.positions, self.velocities)])

        self.velocities += millis / 1000 * LAMBDA / self.population * np.sum(psi, axis=1)

        self.positions += millis / 1000 * self.velocities
        self.directions = self.velocities / np.linalg.norm(self.velocities, axis=1, keepdims=True)

        if TORUS_WORLD:
            for pos, vel in zip(self.positions, self.velocities):
                if pos[0] < 0:
                    pos[0] = self.dimensions[0] - 1
                if pos[1] < 0:
                    pos[1] = self.dimensions[1] - 1
                if pos[0] > self.dimensions[0]:
                    pos[0] = 1
                if pos[1] > self.dimensions[1]:
                    pos[1] = 1
