from tkinter import Tk, BOTH, Canvas

class Window:
  def __init__(self, width, height):
    #initialise the window with paramaters.
    self.width = width
    self.height = height
    self.__root = Tk()
    self.__root.title("MazeWindow")
    self.__canvas = Canvas(self.__root, Width=self.width, Height=self.height)
    self.__canvas.pack(fill=BOTH)
    self.__running = False
    self.__root.protocol("WM_DELETE_WINDOW", self.close)

  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()

