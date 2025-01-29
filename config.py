"""
Configuration settings for the logo bouncing simulation.

Constants:
    WIDTH, HEIGHT: Window size, determined dynamically.
    PAUSE: Time in seconds between animation frames.
    COLORS: List of colors for random logo generation.
    NUMBER_OF_LOGOS: Number of logos displayed simultaneously.
    LOGO_TEXT: Text displayed inside each logo.
"""

import bext

WIDTH, HEIGHT = bext.size()
PAUSE = 0.1
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
NUMBER_OF_LOGOS = 15
LOGO_TEXT = 'DVD'
