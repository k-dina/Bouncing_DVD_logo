import sys, time, bext
from logo_model import LogoNest
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
    This is the main program loop. It creates a LogoNest instance, loops over the logos
    in LogoNest, performs a step on them and displays the result. It also displays the current amount of
    corner bounces at each iteration. Press Ctrl + C to exit.
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
