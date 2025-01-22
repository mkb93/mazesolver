from tkinter import Tk, BOTH, Canvas

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
  def __init__(self, x1, y1, x2, y2, win):
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2
    self._win = win
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
  def draw(self):
    if self.has_left_wall:
      point1 = Point(self._x1, self._y1)
      point2 = Point(self._x1, self._y2)
      line = Line(point1,point2)
      self._win.draw_line(line ,'black')
    if self.has_top_wall:
      point1 = Point(self._x1, self._y1)
      point2 = Point(self._x2, self._y1)
      line = Line(point1,point2)
      self._win.draw_line(line ,'black')
    if self.has_bottom_wall:
      point1 = Point(self._x1, self._y2)
      point2 = Point(self._x2, self._y2)
      line = Line(point1,point2)
      self._win.draw_line(line ,'black')
    if self.has_right_wall:
      point1 = Point(self._x2, self._y1)
      point2 = Point(self._x2, self._y2)
      line = Line(point1,point2)
      self._win.draw_line(line ,'black')
  
  def draw_move(self, to_cell, undo=False):
    center_x1 = (self._x1 + self._x2)/2
    center_y1 = (self._y1 + self._y2)/2
    cell_center1 = Point(center_x1, center_y1)
    
    center_x2 = (to_cell._x1 + to_cell._x2)/2
    center_y2 = (to_cell._y1 + to_cell._y2)/2
    cell_center2 = Point(center_x2, center_y2)
    
    line = Line(cell_center1, cell_center2)
    if undo:
      self._win.draw_line(line, 'gray')
    else:
      self._win.draw_line(line, 'red')





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



if __name__ == "__main__":
    # create window
    win = Window(800, 600)
    # Create points
    point1 = Point(11, 22)  # Replace with actual coordinates
    point2 = Point(33, 45)  # Replace with actual coordinates
    point3 = Point(110, 220)  # Replace with actual coordinates
    point4 = Point(330, 450)  # Replace with actual coordinates
    point5 = Point(115, 22)  # Replace with actual coordinates
    point6 = Point(335, 45)  # Replace with actual coordinates

    # Create a line using those points
    line1 = Line(point1, point2)
    win.draw_line(line1 ,'red')
    line2 = Line(point3, point4)
    win.draw_line(line2 ,'green')
    line3 = Line(point5, point6)
    win.draw_line(line3 ,'blue')

    # Creating a test cell
    cell1 = Cell(20,20,40,40, win)
    cell1.draw()
    cell2 = Cell(40,20,60,40, win)
    cell2.draw()
    cell1.draw_move(cell2, True)


    
    win.wait_for_close()
  