from tkinter import ttk
from tkinter.tix import PopupMenu
import settings
import tkinter as tk

def height_prct(percentage):
  return (settings.height / 100) * percentage

def width_prct(percentage):
    return (settings.width / 100) * percentage
  
def popupmsg(msg, title):
    root = tk.Tk()
    root.title(title)
    label = ttk.Label(root, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(root, text="Restart", command = root.destroy)
    B1.pack()
    PopupMenu.mainloop()
