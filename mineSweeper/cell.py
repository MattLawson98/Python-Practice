from tkinter import Button, Label, font, messagebox
import settings
import random




class Cell:
  all = []
  cell_count = settings.Cell_count
  cell_count_label = None
  def __init__(self,x,y, is_mine=False):
    self.is_mine = is_mine
    self.is_opened = False
    self.is_mine_candidate = False
    self.cell_btn_object = None
    self.x = x
    self.y = y
    
    #Add object to cell.all list
    Cell.all.append(self)
    
  def create_btn_object(self,location):
    btn = Button(
      location,
      width=12,
      height=4,
      bg = 'light grey'
    )
    btn.bind('<Button-1>',self.left_click_actions)#Left click
    btn.bind('<Button-3>',self.right_click_actions)#Right click
    self.cell_btn_object = btn
    
  
  @staticmethod 
  def create_cell_count_label(location):
    lbl = Label(
      location,
      bg='black',
      fg='white',
      text=f"Cells Left:{Cell.cell_count}",
      font=("",30)
    )
    Cell.cell_count_label = lbl
  
      
  def left_click_actions(self, event):
   if self.is_mine:
     self.show_mine()
   else:
     if self.surrounded_cells_mines == 0:
       for cell_obj in self.surrounded_cells:
         cell_obj.show_cell()
     self.show_cell()
     
  def right_click_actions(self, event):
    if not self.is_mine_candidate:
      self.cell_btn_object.configure(
        bg='orange'
      )
      self.is_mine_candidate = True
    else:
      self.cell_btn_object.configure(
        bg='light grey'
      )
      self.is_mine_candidate = False
    
      
  
  def get_cell_by_axis(self, x,y):
    #Return cell values based off x and y values
    for cell in Cell.all:
      if cell.x == x and cell.y == y:
        return cell


  @property
  def surrounded_cells(self):
    cells = [
      self.get_cell_by_axis(self.x - 1, self.y - 1),
      self.get_cell_by_axis(self.x - 1, self.y),
      self.get_cell_by_axis(self.x - 1, self.y + 1),
      self.get_cell_by_axis(self.x , self.y - 1),
      self.get_cell_by_axis(self.x + 1, self.y - 1),
      self.get_cell_by_axis(self.x + 1, self.y ),
      self.get_cell_by_axis(self.x + 1, self.y + 1),
      self.get_cell_by_axis(self.x, self.y + 1),
    ]
        
    cells = [cell for cell in cells if cell is not None] 
    return cells
  
  @property
  def surrounded_cells_mines(self):
    counter = 0
    for cell in self.surrounded_cells:
      if cell.is_mine:
        counter += 1
        
    return counter
  
  def show_cell(self):
    if not self.is_opened:
      Cell.cell_count -= 1
      self.cell_btn_object.configure(text=self.surrounded_cells_mines)
      # Adjust cell count on click event
      if Cell.cell_count_label:
        Cell.cell_count_label.configure(
          text=f"Cells Left:{Cell.cell_count}"
        )
        #If this is seleted as possible mine revert color
        self.cell_btn_object.configure(
          bg='light grey' 
        )
      # Adjust the cell to be opened in logic
      self.is_opened = True
  
  #Need to interupt game and display game over
  def show_mine(self):
    self.cell_btn_object.configure(
        bg='red'
    )
    messagebox.showinfo("Game Over", "You Clicked a mine")
    exit()
   
    
  
  
  @staticmethod
  def randomize_mines():
    picked_cells = random.sample(
      Cell.all, settings.Mines_count
    )
    for picked_cell in picked_cells:
      picked_cell.is_mine = True
      
  
  def __repr__(self):
    return f"Cell({self.x}, {self.y})"
     
