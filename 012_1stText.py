try:
    from colors import *
except ImportError:
    raise ImportError('please use the python interpreter directly, pgzrun has issues with local module imports: python3 -m pgzero 012_1stText.py')

import emoji

alienEmoji = Actor('alien_emoji')

MAIN_COLOR = GREEN

WIDTH=320
HEIGHT=200

score = 1337

# Some example on how to add an emoji to the output console. The console needs to support this UTF Character, otherwise you will see only a box.
print(emoji.emojize(':alien: might win', use_aliases=True))

def draw():
    screen.draw.text(
                ': {0}'.format(score),
                color=MAIN_COLOR,
                center=(alienEmoji.width + (WIDTH/4) - 20, alienEmoji.height/2),
                fontsize=48
            )
    alienEmoji.draw()
