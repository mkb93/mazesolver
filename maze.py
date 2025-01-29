import random, time
from cell import Cell
class Maze:
  def __init__(
    self,
    x1,
    y1,
    num_rows,
    num_cols,
    cell_size_x,
    cell_size_y,
    win,
    seed=None
  ):
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._height = num_rows
    self._width = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    if seed is not None:
      random.seed(seed)

    

  def _draw_cell(self, rows=1):
      for row in range(self._num_rows):
        for col in range(self._num_cols):
          self._cells[row][col].draw()
          self._animate(rows)


  def _create_cells(self):
    self._cells = []
    for row in range(self._num_rows):
      row_cells = []
      for col in range(self._num_cols):
        x1 = self._x1 + (col * self._cell_size_x)
        y1 = self._y1 + (row * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell = Cell(x1,y1,x2,y2, self._win)
        row_cells.append(cell)
        # cell.draw()
        # self._animate()
      self._cells.append(row_cells)
    self._draw_cell(self._num_rows)
    self._break_entrance_and_exit()
    self._break_walls_r(0,0)
    for i in range(self._height):
      for j in range(self._width):
        self._cells[i][j].draw()
    if self._win:
      self._win.redraw()
    self._reset_cells_visited(0,0)

    
  def _animate(self,rows=1):
    if rows<5:
      self._win.redraw()
      time.sleep(0.05)
    else:
      self._win.redraw()
      time.sleep(0.005)

  def _break_entrance_and_exit(self):
    #create a entrance cell
    entrance_cell = self._cells[0][0]
    last_cell = self._cells[-1][-1]
    entrance_cell.has_top_wall = False
    last_cell.has_bottom_wall = False
    entrance_cell.draw()
    last_cell.draw()
  def _break_walls_r(self, i, j):
    self._cells[i][j].visited = True
    while True:
      possible_direction = []
      new_i = i-1
      new_j = j
      if 0 <= new_i < self._height and 0 <= new_j < self._width:
        if not self._cells[new_i][new_j].visited:
          possible_direction.append((new_i, new_j))
      new_i = i+1
      new_j = j
      if 0 <= new_i < self._height and 0 <= new_j < self._width:
        if not self._cells[new_i][new_j].visited:
          possible_direction.append((new_i, new_j))
      new_i = i
      new_j = j-1
      if 0 <= new_i < self._height and 0 <= new_j < self._width:
        if not self._cells[new_i][new_j].visited:
          possible_direction.append((new_i, new_j))
      new_i = i
      new_j = j+1
      if 0 <= new_i < self._height and 0 <= new_j < self._width:
        if not self._cells[new_i][new_j].visited:
          possible_direction.append((new_i, new_j))
      if len(possible_direction) == 0:
        return
      chosen_index = random.randrange(len(possible_direction))
      next_i, next_j = possible_direction[chosen_index]
      #break_wall
      if next_i < i: #moving up
        self._cells[i][j].has_top_wall = False
        self._cells[next_i][next_j].has_bottom_wall = False
      elif next_i > i: #moving down
        self._cells[next_i][next_j].has_top_wall = False
        self._cells[i][j].has_bottom_wall = False
      elif next_j < j: #moving left
        self._cells[i][j].has_left_wall = False
        self._cells[next_i][next_j].has_right_wall = False
      elif next_j > j: #moving right
        self._cells[i][j].has_right_wall = False
        self._cells[next_i][next_j].has_left_wall = False
      self._break_walls_r(next_i,next_j)
  def _reset_cells_visited(self,i,j):
    for i in range(self._height):
      for j in range(self._width):
        self._cells[i][j].visited = False
  def solve(self):
    return self._solve_r(0,0)
  def _solve_r(self,i,j):
    if self._cells[i][j] == self._cells[-1][-1]:
      return True
    self._animate()
    self._cells[i][j].visited = True
    new_i, new_j = i, j
    new_i = i+1
    if 0 <= new_i < self._height:
      if not self._cells[i][j].has_bottom_wall:
        if not self._cells[new_i][new_j].visited:
          self._cells[i][j].draw_move(self._cells[new_i][new_j])
          if self._solve_r(new_i, new_j):
            return True
          self._cells[i][j].draw_move(self._cells[new_i][new_j], True)
    new_i = i-1
    if 0 <= new_i < self._height:
      if not self._cells[i][j].has_top_wall:
        if not self._cells[new_i][new_j].visited:
          self._cells[i][j].draw_move(self._cells[new_i][new_j])
          if self._solve_r(new_i, new_j):
            return True
          self._cells[i][j].draw_move(self._cells[new_i][new_j], True)
    new_j = j+1
    if 0 <= new_j < self._width:
      if not self._cells[i][j].has_right_wall:
        if not self._cells[i][new_j].visited:
          self._cells[i][j].draw_move(self._cells[i][new_j])
          if self._solve_r(i, new_j):
            return True
          self._cells[i][j].draw_move(self._cells[i][new_j], True)
    new_j = j-1
    if 0 <= new_j < self._width:
      if not self._cells[i][j].has_left_wall:
        if not self._cells[i][new_j].visited:
          self._cells[i][j].draw_move(self._cells[i][new_j])
          if self._solve_r(i, new_j):
            return True
          self._cells[i][j].draw_move(self._cells[i][new_j], True)
    return False