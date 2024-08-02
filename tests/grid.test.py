import unittest
from maze_solver.grid import Grid

class GridTest(unittest.TestCase):
    cellsVariants = [
        (
            (1, 1),
            "[(x:10,y:20), (x:20,y:10), (x:10,y:0), (x:0,y:10)]"
        ),
        (
            (0, 1),
            "[(x:10,y:10), (x:20,y:0), (x:0,y:0)]"
        ),
        (
            (9, 9),
            "[(x:100,y:90), (x:90,y:80), (x:80,y:90)]"
        ),
        (
            (10, 10),
            "[]"
        ),                       
    ]

    def test_grid_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Grid(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )

    def test_grid_get_adjacent(self):
        num_cols = 12
        num_rows = 10
        m1 = Grid(0, 0, num_rows, num_cols, 10, 10)

        for variant in self.cellsVariants:
            adjacent1 = m1.get_adjacent(*variant[0])
            self.assertEqual(f"{adjacent1}", variant[1])

if __name__ == "__main__":
    unittest.main()
