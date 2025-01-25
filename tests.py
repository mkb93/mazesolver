import unittest
from window import Maze, Window
win = Window(800,500)
class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)

    m1._create_cells()
    self.assertEqual(
      len(m1._cells),
      num_rows,
    )
    self.assertEqual(
      len(m1._cells[0]),
      num_cols,
    )
  
    for i in range(num_rows):
      for j in range(num_cols):
        self.assertEqual(
          m1._cells[i][j].visited, False
        )
  def test_maze_2(self):
    num_cols = 24
    num_rows = 20
    
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)

    m1._create_cells()
    self.assertEqual(
      len(m1._cells),
      num_rows,
    )
    self.assertEqual(
      len(m1._cells[0]),
      num_cols,
    )

if __name__ == "__main__":
  unittest.main()
