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

    # Create a line using those points
    line = Line(point1, point2)
    win.draw_line(line ,'red')
    
    win.wait_for_close()
  