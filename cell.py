from point import Point
from line import Line

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