from tkinter import Tk, BOTH, Canvas
import time
from graphics.line import Line

class Window:
    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(height=height, width=width)
        self.__canvas.pack()
        self.__window_is_running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_is_running = True

        while self.__window_is_running:
            self.redraw()

    def close(self):
        self.__window_is_running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)