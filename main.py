import sys, time, bext
from logo_model import LogoNest
from config import NUMBER_OF_LOGOS, PAUSE


def main():
    bext.clear()

    logos = LogoNest(NUMBER_OF_LOGOS)

    while True:
        # main program loop
        logos.cleanup()

        # Display number of corner bounces
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', logos.total_bounces, end='')

        for logo in logos:
            logo.step()
            # draw the logos at their new location
            bext.goto(*logo.pos)
            bext.fg(logo.color)
            print('DVD', end='')
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
