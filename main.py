from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		load = Image.open("page_01.png")
		render = ImageTk.PhotoImage(load)
		panel = tk.Label(root, image=img)
		panel.pack(side="bottom", fill="both", expand="yes")
		self.img = Label(root, image=render)
		self.img.image = render
		self.img.place(x=700/2.5, y=800/2.5)
		self.iterate = 1
		
	def create_widgets(self):
		self.nextpage = tk.Button(self)
		self.nextpage["text"] = "Next Page"
		self.nextpage.pack(side="top")
		self.nextpage["command"] = self.next_page
		self.lastpage = tk.Button(self)
		self.lastpage["text"] = "Last Page"
		self.lastpage.pack(side="top")
		self.lastpage["command"] = self.last_page

	def next_page(self):
		load = Image.open(f"page_0{self.iterate}.png")
		print(f"page_0{self.iterate}.png")
		render = ImageTk.PhotoImage(load)
		self.img.image = render
		self.img.place(x=700/2.5, y=800/2.5)

	def last_page(self):
		load = Image.open(f"page_0{self.iterate}.png")
		print(f"page_0{self.iterate}.png")
		render = ImageTk.PhotoImage(load)
		self.img.image = render
		self.img.place(x=700/2.5, y=800/2.5)



root = tk.Tk()
root.geometry("700x800")
app = Application(master=root)
app.mainloop()
