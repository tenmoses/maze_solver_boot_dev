import unittest
from maze_solver.graphics.cell import Cell

class CellTest(unittest.TestCase):
    def test_merge_bottom(self):
        wall_len = 10
        target = Cell(wall_len * 2, wall_len * 2, [True, True, True, True], wall_len, wall_len)

        merge_with = Cell(wall_len * 2, wall_len * 3, [True, True, True, True], wall_len, wall_len)

        line = target.merge(merge_with)
        self.assertEqual(f"{line}", "20,30 --> 30,30")

    def test_merge_top(self):
        wall_len = 10
        target = Cell(wall_len * 2, wall_len * 2, [True, True, True, True], wall_len, wall_len)

        merge_with = Cell(wall_len * 2, wall_len * 1, [True, True, True, True], wall_len, wall_len)

        line = target.merge(merge_with)
        self.assertEqual(f"{line}", "20,20 --> 30,20")

    def test_merge_left(self):
        wall_len = 10
        target = Cell(wall_len * 2, wall_len * 2, [True, True, True, True], wall_len, wall_len)

        merge_with = Cell(wall_len * 1, wall_len * 2, [True, True, True, True], wall_len, wall_len)

        line = target.merge(merge_with)
        self.assertEqual(f"{line}", "20,20 --> 20,30")

    def test_merge_right(self):
        wall_len = 10
        target = Cell(wall_len * 2, wall_len * 2, [True, True, True, True], wall_len, wall_len)

        merge_with = Cell(wall_len * 3, wall_len * 2, [True, True, True, True], wall_len, wall_len)

        line = target.merge(merge_with)
        self.assertEqual(f"{line}", "30,20 --> 30,30")        



if __name__ == "__main__":
    unittest.main()