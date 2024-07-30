from typing import Tuple
import time
from maze_solver.window import Window
from maze_solver.maze import Maze
from maze_solver.graphics.cell import Cell
from maze_solver.graphics.line import Line

def main():
    win = Window(800, 600)

    maze = Maze(5, 5, 10, 12, 40, 40)

    for line in maze.get_blueprint():
        win.draw_line(line, "black")
        time.sleep(0.05)
        win.redraw()

    win.draw_line(maze.make_entrance(), "white")
    time.sleep(0.05)
    win.redraw()

    win.draw_line(maze.make_exit(), "white")
    time.sleep(0.05)
    win.redraw()

    win.wait_for_close()


def get_move(from_cell: Cell, to_cell: Cell, undo=False) -> Tuple[Line, str]:
    return Line(from_cell.get_center(), to_cell.get_center()), "gray" if undo else "red"

main()