from tkinter import Tk, BOTH, Canvas
import time
import random

class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y

class Line:
  def __init__(self,point1, point2):
    self.point1 = point1
    self.point2 = point2
  def draw(self, canvas, fill_color):
    canvas.create_line(
      self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill= fill_color, width=2
    )

class Cell:
  def __init__(self, x1, y1, x2, y2, win, visited=False):
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2
    self._win = win
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self.visited = visited
  def draw(self):
    if self.has_left_wall:
      point1 = Point(self._x1, self._y1)
      point2 = Point(self._x1, self._y2)
      line = Line(point1,point2)
      self._win.draw_line(line ,'black')
    else:
      point1 = Point(self._x1, self._y1)
      point2 = Point(self._x1, self._y2)
      line = Line(point1,point2)
      self._win.draw_line(line ,'#d9d9d9')
    if self.has_top_wall:
      point1 = Point(self._x1, self._y1)
      point2 = Point(self._x2, self._y1)
      line = Line(point1,point2)
      self._win.draw_line(line ,'black')
    else:
      point1 = Point(self._x1, self._y1)
      point2 = Point(self._x2, self._y1)
      line = Line(point1,point2)
      self._win.draw_line(line ,'#d9d9d9')
    if self.has_bottom_wall:
      point1 = Point(self._x1, self._y2)
      point2 = Point(self._x2, self._y2)
      line = Line(point1,point2)
      self._win.draw_line(line ,'black')
    else:
      point1 = Point(self._x1, self._y2)
      point2 = Point(self._x2, self._y2)
      line = Line(point1,point2)
      self._win.draw_line(line ,'#d9d9d9')
    if self.has_right_wall:
      point1 = Point(self._x2, self._y1)
      point2 = Point(self._x2, self._y2)
      line = Line(point1,point2)
      self._win.draw_line(line ,'black')
    else:
      point1 = Point(self._x2, self._y1)
      point2 = Point(self._x2, self._y2)
      line = Line(point1,point2)
      self._win.draw_line(line ,'#d9d9d9')
  
  def draw_move(self, to_cell, undo=False):
    center_x1 = (self._x1 + self._x2)/2
    center_y1 = (self._y1 + self._y2)/2
    cell_center1 = Point(center_x1, center_y1)
    
    center_x2 = (to_cell._x1 + to_cell._x2)/2
    center_y2 = (to_cell._y1 + to_cell._y2)/2
    cell_center2 = Point(center_x2, center_y2)
    
    line = Line(cell_center1, cell_center2)
    line_color = 'red'
    if undo:
      line_color = 'gray'
    self._win.draw_line(line,line_color)





class Window:
  def __init__(self, width, height):
    #initialise the window with paramaters.
    self.width = width
    self.height = height
    self.__root = Tk()
    self.__root.title("MazeWindow")
    self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
    self.__canvas.pack(fill=BOTH)
    self.__running = False
    self.__root.protocol("WM_DELETE_WINDOW", self.close)

  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()
    
  def wait_for_close(self):
    self.__running = True
    while self.__running:
      self.redraw()
  def close(self):
    self.__running = False
  
  def draw_line(self, line, fill_color):
    line.draw(self.__canvas, fill_color)

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

    

  def _draw_cell(self, i, j):
    self._cells[i][j].draw()
    self._animate()

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
        cell.draw()
        self._animate()
      self._cells.append(row_cells)
    self._break_entrance_and_exit()
    self._break_walls_r(0,0)
    for i in range(self._height):
      for j in range(self._width):
        self._cells[i][j].draw()
    if self._win:
      self._win.redraw()
    self._reset_cells_visited(0,0)
    
  def _animate(self):
    self._win.redraw()
    time.sleep(0.05)
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









if __name__ == "__main__":
    # create window
    win = Window(800, 600)
    # Create points
    # point1 = Point(11, 22)  # Replace with actual coordinates
    # point2 = Point(33, 45)  # Replace with actual coordinates
    # point3 = Point(110, 220)  # Replace with actual coordinates
    # point4 = Point(330, 450)  # Replace with actual coordinates
    # point5 = Point(115, 22)  # Replace with actual coordinates
    # point6 = Point(335, 45)  # Replace with actual coordinates

    # # Create a line using those points
    # line1 = Line(point1, point2)
    # win.draw_line(line1 ,'red')
    # line2 = Line(point3, point4)
    # win.draw_line(line2 ,'green')
    # line3 = Line(point5, point6)
    # win.draw_line(line3 ,'blue')

    # # Creating a test cell
    # cell1 = Cell(20,20,40,40, win)
    # cell1.draw()
    # cell2 = Cell(40,20,60,40, win)
    # cell2.draw()
    # cell1.draw_move(cell2, True)
    # cell3 = Cell(760,560,780,580, win)
    # cell3.draw()
    # cell4 = Cell(760,540,780,560, win)
    # cell4.draw()
    # cell4.draw_move(cell3)

    # creating a test maze with multiple cells
    maze = Maze(0,0,12,12,20,20, win)
    maze._create_cells()



    
    win.wait_for_close()
  