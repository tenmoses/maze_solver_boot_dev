from tkinter import Canvas
from maze_solver.graphics.point import Point

class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)

    def __eq__(self, line) -> bool:
        return self.start.x == line.start.x and self.start.y == line.start.y and self.end.y == line.end.y and self.end.x == line.end.x
    
    def __hash__(self) -> int:
        x = f"{self.start.x}{self.end.x}"
        y = f"{self.start.y}{self.end.y}"
        return hash(x + y)