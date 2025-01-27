from window import Window
from maze import Maze

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
    maze = Maze(0,0,20,20,20,20, win)
    maze._create_cells()
    maze.solve()
    
    win.wait_for_close()
  