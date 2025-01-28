import random, bext
import numpy as np
from config import COLORS, WIDTH, HEIGHT


class Logo:
    def __init__(self, id):
        self.id = id
        self.color = random.choice(COLORS)
        x = random.randint(1, (WIDTH - 3))  # // 2 * 2 # random x but has to be even
        y = random.randint(1, HEIGHT - 1)
        self.pos = np.array([x, y])
        self.direction = np.array([random.choice((1, -1)), random.choice((1, -1))])
        self.corner_bounces = 0

    def __next__(self):
        corner_bounce = False

        # check if about to bounce off the edge of corner and change direction
        if (self.pos[0], self.direction[0]) in ((0, -1), (WIDTH - 3, 1)):
            self.direction[0] *= -1
            self.color = random.choice(COLORS)
            corner_bounce = True
        if (self.pos[1], self.direction[1]) in ((0, -1), (HEIGHT - 1, 1)):
            self.direction[1] *= -1
            self.color = random.choice(COLORS)
            if corner_bounce:
                self.corner_bounces += 1  # if both conditions succeed and both x and y directions are changed, it's a corner bounce

        self.pos += self.direction  # * (2, 1)


class LogoNest:
    def __init__(self, number_of_logos):
        self.logos = []
        self.number_of_logos = number_of_logos
        self._create_logos()

    def _create_logos(self):
        for i in range(self.number_of_logos):
            self.logos.append(Logo(i))

    def __iter__(self):
        self._iterable = self.logos.__iter__()
        return self

    def __next__(self):
        try:
            logo = self._iterable.__next__()
            logo.__next__()
            return logo
        except StopIteration:
            raise StopIteration

    def cleanup(self):
        for logo in self.logos:
            bext.goto(*logo.pos)
            print('   ', end='')

    @property
    def total_bounces(self):
        return sum(logo.corner_bounces for logo in self.logos)
