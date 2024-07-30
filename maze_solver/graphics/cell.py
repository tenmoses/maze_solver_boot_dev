from typing import List
from maze_solver.graphics.line import Line
from maze_solver.graphics.point import Point

class Cell:
    def __init__(self, x: int, y: int, walls: List, width = 40, height =40) -> None:
        """walls[left, righ, top, bottom]"""
        self.has_left_wall = walls[0]
        self.has_right_wall = walls[1]
        self.has_top_wall = walls[2]
        self.has_bottom_wall = walls[3]

        self.width = width
        self.height = height

        self.top_left_point = Point(x, y)
        self.top_right_point = Point(x + self.width, y)
        self.bottom_left_pont = Point(x, y + self.height)
        self.bottom_right_pont = Point(x + self.width, y + self.height)
    
    def how_to_draw(self) -> List[Line]:
        lines = []

        if self.has_left_wall:
            lines.append(Line(self.top_left_point, self.bottom_left_pont))

        if self.has_right_wall:
            lines.append(Line(self.top_right_point, self.bottom_right_pont))

        if self.has_top_wall:
            lines.append(Line(self.top_left_point, self.top_right_point))

        if self.has_bottom_wall:
            lines.append(Line(self.bottom_left_pont, self.bottom_right_pont))

        return lines
    
    def get_center(self) -> Point:
        center_x = self.top_left_point.x + self.height / 2
        center_y = self.top_left_point.y + self.width / 2

        return Point(center_x, center_y)
    
    def break_top(self) -> Line:
        self.has_top_wall = False
        return Line(self.top_left_point, self.top_right_point)
    
    def break_bottom(self) -> Line:
        self.has_bottom_wall = False
        return Line(self.bottom_left_pont, self.bottom_right_pont)
    
    def __repr__(self):
        return f"Cell with top left point at x: {self.top_left_point.x} and y: {self.top_left_point.y}"
