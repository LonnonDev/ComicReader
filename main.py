import tkinter as tk
from tkinter import Label
import os
from os import path
from PIL import ImageTk, Image
import sys
import size

root = tk.Tk()

try:
	pagedir = (f"{sys.argv[1]}/")
except IndexError:
	print('No folder was launched with ComicReader, attempting to open the folder "Book"; To open ComicReader properly, drag and drop a folder containing images onto the executable.')
	if not path.exists('Book/'):
		sys.exit()
	pagedir = 'Book/'

sWidth,sHeight = root.winfo_screenwidth(), root.winfo_screenheight()

WIDTH, HEIGHT, SCALEW, SCALEH = size.start(pagedir,sWidth,sHeight)

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

		self.iterate = 0

		self.entries = os.listdir(pagedir)
		self.pagename = self.entries[self.iterate]
		self.image = ImageTk.PhotoImage(Image.open(f'{pagedir}{self.pagename}').resize((int(WIDTH/SCALEW), int(HEIGHT/SCALEH))))
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
			self.image2 = ImageTk.PhotoImage(Image.open(f'{pagedir}{self.pagename}').resize((int(WIDTH/SCALEW), int(HEIGHT/SCALEH))))
			self.pagetext = f"Page {self.iterate+1}"
			self.pagenumber.configure(text=self.pagetext)
			self.pagenumber.text = self.pagetext
			self.label.configure(image=self.image2)
			self.label.image = self.image2
		except:
			pass

	def next_page(self):
		if self.iterate == len(self.entries)-1:
			self.iterate = len(self.entries)-2
		self.iterate += 1
		print(f"Turned to page {self.iterate+1}.")
		self.set_page()

	def last_page(self):
		if self.iterate <= 1:
			self.iterate = 1
		self.iterate -= 1
		print(f"Turned to page {self.iterate+1}.")
		self.set_page()

	def formatnumber(self, number):
		if len(str(number)) <= 1:
			formattednumber = f"0{number}"
		return formattednumber

root.title('ComicReader')
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg='#3d3d3d')
app = Application(master=root)
app.mainloop()