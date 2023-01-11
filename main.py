import pygame
from pygame.locals import *

import numpy as np

from math import sin, cos, pi


WIN_SIZE = 1280, 720
WIN_WIDTH, WIN_HEIGHT = WIN_SIZE
TARGET_FPS = 60


class Application:

    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Racing")
        self.surface = pygame.display.set_mode(WIN_SIZE)
        self.is_running = False

        # sin to circle
        amplitude = 100
        # offset = 150, 150
        self.total_samples = 44100
        self.local_xs = np.linspace(0, 100 * pi, self.total_samples)  #+ offset[0]
        self.local_ys = amplitude * np.sin(self.local_xs / 16)  # + offset[1]

        self.wrap_around_circle = [(WIN_WIDTH // 2, WIN_HEIGHT // 2), 250]
        self.angles = np.linspace(0, 360, self.total_samples)

    def run(self):
        self.is_running = True
        while self.is_running:

            frame_time = self.clock.tick()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stop()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.stop()

            self.surface.fill((255, 255, 255))
            # circle
            # for angle in range(0, 360, 15):
            i = 0
            for angle in self.angles:
                pygame.draw.circle(self.surface,
                                   (0, 0, 0),
                                   (self.wrap_around_circle[0][0] + cos(angle / 180 * pi) * self.wrap_around_circle[1],
                                    self.wrap_around_circle[0][1] + sin(angle / 180 * pi) * (self.wrap_around_circle[1] + self.local_ys[i])),
                                   1
                                   )
                i += 1
            # sin
            # for x, y in zip(self.local_xs, self.local_ys):
            #     pygame.draw.circle(self.surface, (0, 0, 0), (x, y), 1)
            pygame.display.update()

        pygame.quit()
        exit()

    def stop(self):
        self.is_running = False


if __name__ == '__main__':
    Application().run()
