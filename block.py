from cell import Cell
from enums import Shapes
from math import cos, sin, pi


class Block:
    def __init__(self, pos: tuple, shape: str, scale=1, rotation=0):
        self.center_pos = pos
        self.scale = scale

        self.cell_info = Shapes[shape].value
        self.color = self.cell_info[0]

        self.cells = []

        for z in range(4):
            self.cells.append(
                Cell(
                    tuple(x + y for x, y in zip(self.center_pos, tuple(x * self.scale for x in self.cell_info[z + 1]))),
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

        self.change_pos((self.center_pos[0] + 40, self.center_pos[1]))
        pass

    def move_left(self):
        self.change_pos((self.center_pos[0] - 40, self.center_pos[1]))
        pass

    def move_down(self):
        self.change_pos((self.center_pos[0], self.center_pos[1] + 40))
        pass

    def change_pos(self, new_pos: tuple):
        self.center_pos = new_pos
        for z in range(4):
            self.cells[z].update_pos(
                tuple(x + y for x, y in zip(self.center_pos, tuple(x * self.scale for x in self.cell_info[z + 1]))))
        self.rotate(0)

    def shatter(self):
        return self.cells
