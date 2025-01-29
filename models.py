import pydoc
import random, bext
import numpy as np
from config import COLORS, WIDTH, HEIGHT


class Logo:
    """
    Represents a moving logo in the simulation.

    This class stores the logo's properties, including its position, direction,
    color, and the number of corner bounces.
    """

    def __init__(self, id):
        """
        Initializes a logo with a random position, direction, and color.
        :param id: unique logo id (should be used for debugging)
        """
        self.id = id
        self.color = random.choice(COLORS)
        x = random.randint(1, (WIDTH - 3))
        y = random.randint(1, HEIGHT - 1)
        self.pos = np.array([x, y])
        self.direction = np.array([random.choice((1, -1)), random.choice((1, -1))])
        self.corner_bounces = 0

    def step(self):
        """
        Moves the logo one step in its current direction.

        If the logo reaches an edge, it bounces by reversing direction
        and changing color. If it bounces off a corner, it increments
        the `corner_bounces` counter.
        """
        corner_bounce = False

        if (self.pos[0], self.direction[0]) in ((0, -1), (WIDTH - 3, 1)):
            self.direction[0] *= -1
            self.color = random.choice(COLORS)
            corner_bounce = True
        if (self.pos[1], self.direction[1]) in ((0, -1), (HEIGHT - 1, 1)):
            self.direction[1] *= -1
            self.color = random.choice(COLORS)
            if corner_bounce:
                self.corner_bounces += 1

        self.pos += self.direction

    def __repr__(self):
        return f"Logo(id={self.id}, pos={self.pos.tolist()}, dir={self.direction.tolist()}, color={self.color})"


class LogoNest:
    """
    Manages multiple Logo instances.

    This class is responsible for creating, storing, and iterating over
    multiple Logo objects. It also provides utilities for tracking
    corner bounces and clearing the console.

    """

    def __init__(self, number_of_logos):
        self.logos = []
        self.number_of_logos = number_of_logos
        self._create_logos()

    def _create_logos(self):
        for i in range(self.number_of_logos):
            self.logos.append(Logo(i))

    def __iter__(self):
        """
        Returns an iterator over the stored logos.
        """
        return self.logos.__iter__()

    def cleanup(self):
        """
        Clears the console
        """
        for logo in self.logos:
            bext.goto(*logo.pos)
            print('   ', end='')

    @property
    def total_bounces(self):
        return sum(logo.corner_bounces for logo in self.logos)

