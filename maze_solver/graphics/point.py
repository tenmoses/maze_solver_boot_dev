class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __eq__(self, point) -> bool:
        return self.x == point.x and self.y == point.y