a semi guided project through boot.dev
running it locally requires a tkinter library and python3
current issues to fix:
  large classes are not refined so hard to read
  tests are linked to the old way of running so need to be changed to work with separated classes
  not deployed to a git pages area
  not in my pinned projects/ potential put in my portfolio page
  try to add a video demo with a gif of it working on a basic maze
  should really be more tests
#how to set up
I use tkinter library

Let's start by just making sure that your tkinter installation is working. Tkinter is a Python library that allows us to create graphical user interfaces (GUIs) for our programs.

For most systems, tkinter will work out of the box. Run the following command in your terminal to see if it's installed:

python3 -m tkinter

#If you do have issues, read on.

Problems With Tkinter? Install Missing Dependencies
If you're seeing an error like this you may need to install some dependencies: 
ModuleNotFoundError: No module named '_tkinter'. First, check to see which version of python you are using:

python3 --version
You should be on 3.10 or higher. If you're not, update your Python version.

Next, it's important to understand that tkinter depends on the Tcl/Tk library. I've found that installing the tk-dev or python-tk packages are usually the easiest way to install and link it to your Python version. On Ubuntu (Linux), run:

sudo apt-get install python3-tk

On macOS, make sure you have Homebrew installed, and then run:

brew install python-tk
Your versions of python-tk and python should match!

Now, if python3 -m tkinter still isn't working, you may need to uninstall and reinstall Python so that it links to the now-available Tcl/Tk library. If you're still having issues, try googling the error messages you're encountering.



#how to run
  if the setup has gone well.
  open terminal in the mazesolver folder and run
  python3 index.py
  you should see a window open and a bunch of square cells appear these are preprogramed and can be edited in the window folder
  then the maze will form and a red line should be drawn from entry to exit. if any mistakes are made a grey line will appear and backtrack to a place with more options.

#how to test
make sure the setup has gone well
open terminal in the mavesolver folder and run
python3 tests.py 
this will open up a window and draw two mazes on top of each other and then automatically close the window itself once the test conditions are met.

ENJOY!
