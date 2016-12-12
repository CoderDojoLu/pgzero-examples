# Expose pgzero objects as a builtins
from pgzero.builtins import *
from pgzero.runner import *
import pgzero.screen


def run_pgzero():
    pygame.init()
    PGZeroGame(sys.modules['__main__']).run()
    pygame.quit()


# Pygame won't run from a normal virtualenv copy of Python on a Mac
##if not check_python_ok_for_pygame():
##    substitute_full_framework_python()
if __debug__:
    warnings.simplefilter('default', DeprecationWarning)
path = sys.argv[0]
loaders.set_root(path)

screen= pgzero.screen.Screen(pygame.display.set_mode((1, 1), DISPLAY_FLAGS))
