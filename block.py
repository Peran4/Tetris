from cell import Cell
from enums import Shapes
from math import cos, sin, pi


class Block:
    def __init__(self, pos: tuple, shape: str, scale=1, rotation=0):
        self.center_pos = pos
        self.scale = scale

        cell_info = Shapes[shape].value
        self.color = cell_info[0]

        self.cells = []

        for z in range(4):
            self.cells.append(
                Cell(tuple(x + y for x, y in zip(self.center_pos, tuple(x * self.scale for x in cell_info[z+1]))),
                     self.color, self.scale))

        self.rotation = 0
        self.rotate(rotation)
        # self.cells[0].change_to_white()

    def draw_block(self, screen):
        for cell in self.cells:
            cell.draw(screen)

    def rotate(self, rotation):
        if self.color == "YELLOW":
            return

        self.rotation = rotation
        beta = (self.rotation % 4) * pi / 2

        for cell in self.cells:
            x = cell.pos[0] - self.center_pos[0]
            y = cell.pos[1] - self.center_pos[1]

            new_x = round(x * cos(beta) - y * sin(beta))
            new_y = round(x * sin(beta) + y * cos(beta))

            new_x += self.center_pos[0]
            new_y += self.center_pos[1]

            cell.update_pos((new_x, new_y))

    def trow_shade(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass

    def move_down(self):
        pass

    def shatter(self):
        return self.cells
