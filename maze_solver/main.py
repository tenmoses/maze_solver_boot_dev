from typing import Tuple
import time
from maze_solver.window import Window
from maze_solver.grid import Grid
from maze_solver.maze import Maze
from maze_solver.graphics.cell import Cell
from maze_solver.graphics.line import Line

def main():
    win = Window(800, 600)

    grid = Grid(5, 5, 10, 12, 40, 40)

    for line in grid.get_blueprint():
        win.draw_line(line, "black")
        # time.sleep(0.05)
        win.redraw()

    maze = Maze(grid, 1)

    for line in maze.get_blueprint():
        win.draw_line(line, "white")
        time.sleep(0.05)
        win.redraw()

    win.wait_for_close()


def get_move(from_cell: Cell, to_cell: Cell, undo=False) -> Tuple[Line, str]:
    return Line(from_cell.get_center(), to_cell.get_center()), "gray" if undo else "red"

main()