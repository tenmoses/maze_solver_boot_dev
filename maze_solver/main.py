import time
from maze_solver.window import Window
from maze_solver.grid import Grid
from maze_solver.maze import Maze
from maze_solver.solver import Solver

def main():
    win = Window(1000, 1000)

    grid = Grid(5, 5, 9, 9, 40, 40)

    for line in grid.get_blueprint():
        win.draw_line(line, "black")
        time.sleep(0.05)
        win.redraw()

    maze = Maze(grid)

    for line in maze.get_blueprint():
        win.draw_line(line, "white")
        time.sleep(0.1)
        win.redraw()

    solver = Solver(grid, maze);

    solver.solve()

    for line in solver.get_blueprint():
        win.draw_line(line[0], line[1])
        time.sleep(0.1)
        win.redraw()

    win.wait_for_close()

main()