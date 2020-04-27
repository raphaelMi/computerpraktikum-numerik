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
            for pos, vel in zip(self.positions, self.velocities):
                if pos[0] < 0 and vel[0] < 0:
                    vel[0] *= -1
                if pos[1] < 0 and vel[1] < 0:
                    vel[1] *= -1
                if pos[0] > self.dimensions[0] and vel[0] > 0:
                    vel[0] *= -1
                if pos[1] > self.dimensions[1] and vel[1] > 0:
                    vel[1] *= -1
