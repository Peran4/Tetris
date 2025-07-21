from enum import Enum
from paths import *


class Color(Enum):
    WHITE = white_block_path
    GRAY = gray_block_path
    BLUE = blue_block_path
    CYAN = cyan_block_path
    GREEN = green_block_path
    YELLOW = yellow_block_path
    ORANGE = orange_block_path
    RED = red_block_path
    PURPLE = purple_block_path


class Shapes(Enum):
    O = ["YELLOW", (0, 0), (-80, 0), (-80, -80), (0, -80)]
    I = ["CYAN", (0, 0), (0, 80), (0, 160), (0, 240)]
    S = ["GREEN", (0, 0), (0, 80), (-80, 80), (80, 0)]
    Z = ["RED", (0, 0), (0, 80), (80, 80), (-80, 0)]
    L = ["ORANGE", (0, 0), (0, 80), (0, 160), (80, 160)]
    J = ["BLUE", (0, 0), (0, 80), (0, 160), (-80, 160)]
    T = ["PURPLE", (0, 0), (-80, 0), (80, 0), (0, 80)]
