from cell import Cell
from enums import Color, Shapes


class Block:
    def __init__(self, pos: tuple, shape: str, scale=1, rotation=0):
        self.pos = pos
        self.scale = scale

        cell_info = Shapes[shape].value
        self.color = cell_info[0]

        self.cells = [Cell(self.pos + (cell_info[1] * self.scale), self.color, self.scale),
                      Cell(self.pos + (cell_info[2] * self.scale), self.color, self.scale),
                      Cell(self.pos + (cell_info[3] * self.scale), self.color, self.scale),
                      Cell(self.pos + (cell_info[4] * self.scale), self.color, self.scale)]

    def draw(self):