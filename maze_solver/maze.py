from maze_solver.graphics.cell import Cell

class Maze:
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
    
    def make_entrance(self):
        
        return self.cells[0][0].break_top()
    
    def make_exit(self):
        x = self.num_cols - 1
        y = self.num_rows - 1
        return self.cells[y][x].break_bottom()
    