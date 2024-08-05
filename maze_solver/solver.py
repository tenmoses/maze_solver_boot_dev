from typing import List
from maze_solver.grid import Grid
from maze_solver.maze import Maze
from maze_solver.graphics.line import Line
from maze_solver.graphics.cell import Cell

class Solver:
    def __init__(self, grid: Grid, maze: Maze) -> None:
        self.grid = grid
        self.maze = maze
        self.blueprint = []
        self.solved = False
        self.visited = []

    def solve(self):
        return self._solve_r(self.grid.get_cell(0, 0))

    def _solve_r(self, cell: Cell):       
        self.visited.append(cell)
        if self.maze.is_end(cell):
            return True
        
        x, y = cell.get_top_left_tuple()
        j = int((x - self.grid.x1)  / self.grid.cell_size_x)
        i = int((y - self.grid.y1) / self.grid.cell_size_y)
        
        for wall in cell.get_broken_walls():
            if wall == "bottom":
                if self._connect_cells(cell, i + 1, j):
                    return True
            if wall == "left":
                if self._connect_cells(cell, i, j - 1):
                    return True
            if wall == "right":
                if self._connect_cells(cell, i, j + 1):
                    return True
            if wall == "top":
                if self._connect_cells(cell, i - 1, j):
                    return True

    def _connect_cells(self, cell, i, j):
        try:
            next_cell = self.grid.get_cell(i, j)
            if next_cell not in self.visited:
                self.blueprint.append((Line(cell.get_center(), next_cell.get_center()), "red"))
                result = self._solve_r(next_cell)

                if result:
                    return True

                self.blueprint.append((Line(cell.get_center(), next_cell.get_center()), "gray"))
        except Exception:
            pass       


    def get_blueprint(self) -> List[Line]:
        return self.blueprint        

