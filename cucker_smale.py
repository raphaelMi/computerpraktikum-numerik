import numpy as np
import init

init.LENGTH_FACTOR = 25  # The ratio between pixels and simulation length units
init.SHARK_DIST = 100  # The distance at which the shark influences the fish


class Flock:
    def __init__(self, population=50):
        self.population = population

        self.positions = np.zeros((population, 2))  # Fish positions
        self.velocities = np.zeros((population, 2))  # Fish velocitiers
        self.directions = np.zeros((population, 2))  # Normalized fish velocities

        self.dimensions = (800, 600) # Simulation area
        self.color = (0, 0, 0, 255) # Flock color (eventually used for rendering)

        self.deviations = [] # Deviations used for plotting

    def do_frame(self, millis=16.7, shark_pos=False):
        # The equation from the cucker-smale model
        psi = np.array([[(vel_i - vel_j) / (1 + 1 / init.LENGTH_FACTOR ** 2 * np.linalg.norm(pos_i - pos_j) ** 2)
                         for pos_i, vel_i in zip(self.positions, self.velocities)]
                        for pos_j, vel_j in zip(self.positions, self.velocities)])

        # Simulate the shark - an area fishes want to avoid
        shark_force = np.zeros((self.population, 2))
        if shark_pos:
            shark_force = np.array([(fish_pos - shark_pos) * init.SHARK_DIST**4 / np.linalg.norm(fish_pos - shark_pos)**4
                                    for fish_pos in self.positions])

        # Explicit Euler-Integration from acceleration to velocities
        self.velocities += millis / 1000 * (init.LAMBDA / self.population * np.sum(psi, axis=1) + shark_force)

        # Explicit Euler-Integration from velocity to positions
        self.positions += millis / 1000 * self.velocities
        self.directions = self.velocities / np.linalg.norm(self.velocities, axis=1, keepdims=True)

        # If the fishes leave the defined area, they'll be placed at the opposite sides again
        if init.TORUS_WORLD:
            for pos, vel in zip(self.positions, self.velocities):
                if pos[0] < 0:
                    pos[0] = self.dimensions[0] - 1
                if pos[1] < 0:
                    pos[1] = self.dimensions[1] - 1
                if pos[0] > self.dimensions[0]:
                    pos[0] = 1
                if pos[1] > self.dimensions[1]:
                    pos[1] = 1

        # Mean velocity for plotting
        v_bar = np.sum(self.velocities, axis=0) / self.population

        # The deviation of the fishes from the mean velocity
        self.deviations.append(np.sum(np.linalg.norm(self.velocities - v_bar, axis=1)))

