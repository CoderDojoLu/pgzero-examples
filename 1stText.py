from colors import *
import emoji

MAIN_COLOR = GREEN

WIDTH=320
HEIGHT=200

score = 1337

# Some example on how to add an emoji to the output console. The console needs to support this UTF Character, otherwise you will see only a box.
print(emoji.emojize(':alien: might win', use_aliases=True))

def draw():
    screen.draw.text(
                'Alien: {0}'.format(score),
                color=MAIN_COLOR,
                center=(WIDTH/4 - 20, 20),
                fontsize=48
            )
