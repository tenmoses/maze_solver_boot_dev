from typing import Tuple, List
from maze_solver.graphics.cell import Cell

class Grid:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.cells = []
        self.to_update = []

        self._create_cells()

    def _create_cells(self):
        current_y = self.y1
        for row_i in range(0, self.num_rows):
            self.cells.append([])
            current_x = self.x1

            for col_i in range(0, self.num_cols):
                cell = Cell(current_x, current_y, [True, True, True, True], self.cell_size_x, self.cell_size_y)
                self.cells[row_i].append(cell)
                current_x += self.cell_size_x

            current_y += self.cell_size_y

    def get_blueprint(self):
        lines = set();
        for cell_row in self.cells:
            for cell in cell_row:
                lines.update(cell.how_to_draw())

        return lines
    
    def get_cell(self, i, j) -> Cell:
        if i > -1 and j > -1:
            return self.cells[i][j]
        else:
            raise Exception("No cell")
    
    def get_size(self) -> Tuple[int, int]:
        return (self.num_rows, self.num_cols)
    
    def get_adjacent(self, i, j) -> List[Cell]:
        cells = []
        if i <= self.num_rows - 1 and j <= self.num_cols - 1:
            if i + 1 < self.num_rows:
                cells.append(self.cells[i + 1][j])

            if j + 1 < self.num_cols:
                cells.append(self.cells[i][j + 1])

            if i - 1 >= 0:
                cells.append(self.cells[i - 1][j])

            if j - 1 >= 0:
                cells.append(self.cells[i][j - 1])   

        return cells
    
    def __repr__(self) -> str:
        border = '|'.rjust(15, '-')
        print_lines = []

        print_lines.append("\n")

        for _ in range(0, self.num_cols):
            print_lines.append(border)

        print_lines.append("\n")

        for i in range(0, len(self.cells) - 1):
            cell_row = self.cells[i]
            for j in range(0, len(cell_row) - 1):
                cell = cell_row[j]
                print_lines.append("{:<15}".format(f"{cell}"))

            print_lines.append("\n")

            for j in range(0, len(cell_row) - 1):
                cell = cell_row[j]
                print_lines.append("{:<15}".format(f"i:{i},j:{j}"))

            print_lines.append("\n")          

            for _ in range(0, self.num_cols):
                print_lines.append(border)

            print_lines.append("\n")

        return ''.join(print_lines)
    