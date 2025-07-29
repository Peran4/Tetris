from cells import Cell, ShadeCell
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

        self.shade_cells = []
        for z in range(4):
            self.shade_cells.append(
                ShadeCell(
                    tuple(x + y for x, y in zip(self.center_pos, tuple(x * self.scale for x in self.cell_info[z + 1]))),
                    self.color, self.scale))

        self.rotation = rotation
        self.__rotate()

    def draw_block(self, screen):
        for cell in self.cells:
            cell.draw(screen)

    def __rotate(self):
        if self.color == "YELLOW":
            return

        for z in range(4):
            self.cells[z].update_pos(
                tuple(x + y for x, y in zip(self.center_pos, tuple(x * self.scale for x in self.cell_info[z + 1]))))

        beta = (self.rotation % 4) * pi / 2

        for cell, shade_cell in zip(self.cells, self.shade_cells):
            x = cell.pos[0] - self.center_pos[0]
            y = cell.pos[1] - self.center_pos[1]

            new_x = round(x * cos(beta) - y * sin(beta))
            new_y = round(x * sin(beta) + y * cos(beta))

            new_x += self.center_pos[0]
            new_y += self.center_pos[1]

            cell.update_pos((new_x, new_y))

    def draw_shade(self, screen):
        for cell in self.shade_cells:
            cell.draw(screen)

    def change_pos_center(self, new_pos: tuple):
        self.center_pos = new_pos
        positions = []
        for z in range(4):
            positions.append(
                tuple(x + y for x, y in zip(self.center_pos, tuple(x * self.scale for x in self.cell_info[z + 1]))))

        self.change_all_pos(positions)
        self.change_shade_pos(positions)

    def change_all_pos(self, new_positions):
        self.center_pos = new_positions[0]

        i = 0
        for cell in self.cells:
            cell.update_pos(new_positions[i])
            i += 1

    def change_shade_pos(self, new_positions):
        i = 0
        for shade_cell in self.shade_cells:
            shade_cell.update_pos(new_positions[i])
            i += 1

    def shatter(self):
        return self.cells
