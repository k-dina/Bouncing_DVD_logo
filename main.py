import sys, time, bext
from models import LogoNest
from config import NUMBER_OF_LOGOS, PAUSE, LOGO_TEXT

"""
Logo Bouncing Simulation.

This script simulates multiple logos bouncing off the edges of the console.
Each logo changes direction and color upon impact, and corner bounces are counted.

Classes:
    - Logo: Represents a single bouncing logo.
    - LogoNest: Manages multiple logos and tracks corner bounces.

Requires:
    - bext
    - numpy
    - config.py (for COLORS, WIDTH, HEIGHT)
"""


def main():
    """
    Main program loop for displaying animated logos.

    This script creates an instance of the LogoNest class, which manages multiple logos.
    The program enters an infinite loop where it:
    1. Updates the positions and states of the logos (via their 'step' method).
    2. Clears the screen and re-renders the logos in their new positions.
    3. Displays the current number of corner bounces that have occurred, reflecting the number of times any logo has bounced off a corner.

    The loop continues indefinitely until interrupted by the user (Ctrl + C).

    Press Ctrl + C to exit the program.
    """
    bext.clear()
    logos = LogoNest(NUMBER_OF_LOGOS)

    while True:
        logos.cleanup()

        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', logos.total_bounces, end='')

        for logo in logos:
            logo.step()
            bext.goto(*logo.pos)
            bext.fg(logo.color)
            print(LOGO_TEXT, end='')

        bext.goto(0, 0)
        sys.stdout.flush()
        time.sleep(PAUSE)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD logo')
        sys.exit()
