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
        self.start = None
        self.end = None
        random.seed(seed)
        self._break_walls()

    def _break_walls(self):
        self.start = self.grid.get_cell(0, 0)
        self.blueprint.append(self.start.break_top())
        last_i, last_j = map(lambda num: num - 1, self.grid.get_size())
        self.end = self.grid.get_cell(last_i, last_j)
        self.blueprint.append(self.end.break_bottom())
        self._break_walls_r(0, 0)

    def _break_walls_r(self, i, j):
        current = self.grid.get_cell(i, j)
        self.visited.update({f"{current.get_center()}": current})
        to_visit = list(filter(self._filter_not_visited_cell, self.grid.get_adjacent(i, j)))

        while len(list(filter(self._filter_not_visited_cell, to_visit))) > 0:
            next_cell = random.choice(list(filter(self._filter_not_visited_cell, to_visit)))
            to_visit.remove(next_cell)
            
            self.visited.update({f"{next_cell.get_center()}": next_cell})
            self.blueprint.append(current.merge(next_cell))

            next_x, next_y = next_cell.get_top_left_tuple()
            next_j = int((next_x - self.grid.x1)  / self.grid.cell_size_x)
            next_i = int((next_y - self.grid.y1) / self.grid.cell_size_y)
            self._break_walls_r(next_i, next_j)

        return


    def _filter_not_visited_cell(self, cell: Cell):
        return not f"{cell.get_center()}" in self.visited
    
    def _filter_visited_cell(self, cell: Cell):
        if f"{cell.get_center()}" in self.visited:
            return cell.get_num_walls() >= 3
        
        return False
    
    def is_end(self, cell: Cell) -> bool:
        return self.end == cell

    def get_blueprint(self) -> List[Line]:
        return self.blueprint
        