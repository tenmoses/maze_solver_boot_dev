from typing import List, Tuple
from typing import Self
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
        self.bottom_left_point = Point(x, y + self.height)
        self.bottom_right_point = Point(x + self.width, y + self.height)
    
    def how_to_draw(self) -> List[Line]:
        lines = []

        if self.has_left_wall:
            lines.append(Line(self.top_left_point, self.bottom_left_point))

        if self.has_right_wall:
            lines.append(Line(self.top_right_point, self.bottom_right_point))

        if self.has_top_wall:
            lines.append(Line(self.top_left_point, self.top_right_point))

        if self.has_bottom_wall:
            lines.append(Line(self.bottom_left_point, self.bottom_right_point))

        return lines
    
    def get_center(self) -> Point:
        center_x = self.top_left_point.x + self.height / 2
        center_y = self.top_left_point.y + self.width / 2

        return Point(center_x, center_y)
    
    def get_top_left_tuple(self) -> Tuple[int, int]:
        return (self.top_left_point.x, self.top_left_point.y)
    
    def break_top(self) -> Line:
        self.has_top_wall = False
        return Line(self.top_left_point, self.top_right_point)
    
    def break_bottom(self) -> Line:
        self.has_bottom_wall = False
        return Line(self.bottom_left_point, self.bottom_right_point)
    
    def get_broken_walls(self) -> List:
        broken = []

        if not self.has_bottom_wall:
            broken.append("bottom")

        if not self.has_left_wall:
            broken.append("left")

        if not self.has_right_wall:
            broken.append("right")

        if not self.has_top_wall:
            broken.append("top")

        return broken
    
    def get_num_walls(self) -> int:
        return int(self.has_bottom_wall) + int(self.has_top_wall) + int(self.has_left_wall) + int(self.has_right_wall)
    
    def merge(self, m: Self) -> Line:
        if self.top_left_point == m.top_right_point and self.bottom_left_point == m.bottom_right_point:
            self.has_left_wall = False
            m.has_right_wall = False
            return Line(self.top_left_point, self.bottom_left_point)

        if self.top_right_point == m.top_left_point and self.bottom_right_point == m.bottom_left_point:
            self.has_right_wall = False
            m.has_left_wall = False
            return Line(self.top_right_point, self.bottom_right_point)
        
        if self.bottom_left_point == m.top_left_point and self.bottom_right_point == m.top_right_point:
            self.has_bottom_wall = False
            m.has_top_wall = False
            return Line(self.bottom_left_point, self.bottom_right_point)
        
        if self.top_left_point == m.bottom_left_point and self.top_right_point == m.bottom_right_point:
            self.has_top_wall = False
            m.has_bottom_wall = False
            return Line(self.top_left_point, self.top_right_point)
        
        raise Exception(f"Cells {self} and {m} cannot be merged")
    
    def __repr__(self):
        return f"(x:{self.top_left_point.x},y:{self.top_left_point.y})"
    
    def __eq__(self, cell):
        return self.top_left_point == cell.top_left_point
