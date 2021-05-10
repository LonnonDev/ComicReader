from tkinter import *
import tkinter as tk
import os
from PIL import ImageTk, Image

WIDTH, HEIGHT = 700, 800

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

		self.iterate = 0

		self.entries = os.listdir('Book/')
		self.pagename = self.entries[self.iterate]
		self.image = ImageTk.PhotoImage(Image.open(f'Book/{self.pagename}').resize((int(WIDTH/1.2), int(HEIGHT/1.2))))
		self.label = Label(image=self.image)
		self.pagetext = f"Page {self.iterate+1}"
		self.pagenumber = Label(text=self.pagetext)

		self.pagenumber.pack()
		self.label.pack()
		
	def create_widgets(self):
		self.nextpage = tk.Button(self, bd=2, bg="#707070")
		self.nextpage["text"] = "Next Page"
		self.nextpage.pack(side="top")
		self.nextpage["command"] = self.next_page
		self.lastpage = tk.Button(self, bd=2, bg="#707070")
		self.lastpage["text"] = "Last Page"
		self.lastpage.pack(side="top")
		self.lastpage["command"] = self.last_page

	def set_page(self):
		self.pagename = self.entries[self.iterate]
		try:
			self.image2 = ImageTk.PhotoImage(Image.open(
				f'Book/{self.pagename}').resize((int(WIDTH/1.2), int(HEIGHT/1.2))))
			self.pagetext = f"Page {self.iterate+1}"
			self.pagenumber.configure(text=self.pagetext)
			self.pagenumber.text = self.pagetext
			self.label.configure(image=self.image2)
			self.label.image = self.image2
		except:
			pass

	def next_page(self):
		if self.iterate+1 == len(self.entries)-1:
			self.iterate = -1
		if self.iterate <= -1:
			self.iterate = len(self.entries)-1
		self.iterate += 1
		print(self.iterate)
		self.set_page()

	def last_page(self):
		if self.iterate+1 == len(self.entries)-1:
			self.iterate = -1
		if self.iterate <= -1:
			self.iterate = len(self.entries)-1
		self.iterate -= 1
		print(self.iterate)
		self.set_page()

	def formatnumber(self, number):
		if len(str(number)) <= 1:
			formattednumber = f"0{number}"
		return formattednumber


root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg='#3d3d3d')
app = Application(master=root)
app.mainloop()
