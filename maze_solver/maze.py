from typing import List
import random
from maze_solver.grid import Grid
from maze_solver.graphics.line import Line
from maze_solver.graphics.cell import Cell

class Maze:
    def __init__(
            self,
            grid: Grid,
            seed=None
        ) -> None:
        self.grid = grid
        self.blueprint = []
        self.visited = {}
        self.current = None
        random.seed(seed)
        self._break_walls()

    def _break_walls(self):
        self.current = self.grid.get_cell(0, 0)
        self.blueprint.append(self.current.break_top())
        last_i, last_j = map(lambda num: num - 1, self.grid.get_size())
        self.blueprint.append(self.grid.get_cell(last_i, last_j).break_bottom())
        self._break_walls_r(0, 0)

    def _break_walls_r(self, i, j):
        self.visited.update({f"{self.current.get_center()}": self.current})
        to_visit = [] + list(filter(self._filter_cell, self.grid.get_adjacent(i, j)))

        if len(to_visit):
            next_cell = random.choice(to_visit)
            self.visited.update({f"{next_cell.get_center()}": next_cell})
            self.blueprint.append(self.current.merge(next_cell))
            next_x, next_y = next_cell.get_top_left_tuple()
            next_j = int((next_x - self.grid.x1)  / self.grid.cell_size_x)
            next_i = int((next_y - self.grid.y1) / self.grid.cell_size_y)
            self.current = next_cell
            self._break_walls_r(next_i, next_j)

    def _filter_cell(self, cell: Cell):
        return not f"{cell.get_center()}" in self.visited        

    def get_blueprint(self) -> List[Line]:
        return self.blueprint
        