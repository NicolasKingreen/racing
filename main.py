import pygame
from pygame.locals import *

import numpy as np

from math import sin, cos, pi


WIN_SIZE = 1280, 720
WIN_WIDTH, WIN_HEIGHT = WIN_SIZE
TARGET_FPS = 0


class Application:

    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Racing")
        self.surface = pygame.display.set_mode(WIN_SIZE)
        self.is_running = False

        # sin to circle
        amplitude = 10
        # offset = 150, 150
        period = 1
        self.total_samples = 2500  # few thousands is ok; 1k is dotted
        self.local_xs = np.linspace(0, 100 * pi, self.total_samples)  # + offset[0]
        self.local_ys = amplitude * np.sin(self.local_xs / period)  # + offset[1]

        self.angles = np.linspace(0, 360, self.total_samples)
        self.current_angle = 0
        self.angular_speed = 10  # in deg

        self.min_radius = 100
        self.max_radius = 250
        self.shrink_speed = 10

        self.wrap_around_circle = [(WIN_WIDTH // 2, WIN_HEIGHT // 2), self.min_radius]

    def run(self):
        self.is_running = True
        while self.is_running:

            frame_time_ms = self.clock.tick(TARGET_FPS)
            frame_time_s = frame_time_ms / 1000.

            print(f"FPS: {self.clock.get_fps():.2f}")

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stop()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.stop()

            self.current_angle += self.angular_speed * frame_time_s
            if self.wrap_around_circle[1] > self.max_radius or self.wrap_around_circle[1] < self.min_radius:
                self.shrink_speed *= -1
            self.wrap_around_circle[1] += self.shrink_speed * frame_time_s

            self.surface.fill((255, 255, 255))
            # circle
            # for angle in range(0, 360, 15):
            i = 0
            for angle in self.angles:
                angle += self.current_angle
                pygame.draw.circle(self.surface,
                                   (0, 0, 0),
                                   (self.wrap_around_circle[0][0] + cos(angle / 180 * pi) * (self.wrap_around_circle[1] + self.local_ys[i]),
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
