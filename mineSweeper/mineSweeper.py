from tkinter import *

import settings
import utils
from cell import Cell

root = Tk()
#Adjust window settings
root.configure(bg="black")
root.geometry(f'{settings.width}x{settings.height}')
root.title('Minesweeper')
root.resizable(False,False)

top_frame = Frame(
  root,
  bg="black",
  width=settings.width,
  height=utils.height_prct(25)
  )

top_frame.place(x=0,y=0)

left_frame = Frame(
  root,
  bg="black",
  width=utils.width_prct(25),
  height=utils.height_prct(75)
)

left_frame.place(x=0,y=utils.height_prct(25))

center_frame = Frame(
  root,
  bg="black",
  width=utils.width_prct(75), 
  height=utils.height_prct(75)
)

center_frame.place(
  x=utils.width_prct(25),
  y=utils.height_prct(25)
)
for x in range(settings.Grid_size):
  for y in range(settings.Grid_size):
    c = Cell(x,y)
    c.create_btn_object(center_frame)
    c.cell_btn_object.grid(
      column=x,
      row=y
    )
    
Cell.randomize_mines()
  

#Create the window
root.mainloop()