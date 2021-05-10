from tkinter import *
import tkinter as tk
import os


class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

		self.iterate = 1

		entries = os.listdir('Book/')
		self.pagename = entries[0]
		# Book/silent_sinner_prologue_01.jpg
		# :-4
		# -4
		print(f'Book/{self.pagename[:-6]}{self.pagename[-4:]}')
		self.image = PhotoImage(file=f'Book/{self.pagename[:-4]}')
		self.label = Label(image=self.image)

		self.pagetext = f"Page {self.iterate}"
		self.pagenumber = Label(text=self.pagetext)

		self.pagenumber.pack()
		self.label.pack()
		
	def create_widgets(self):
		self.nextpage = tk.Button(self)
		self.nextpage["text"] = "Next Page"
		self.nextpage.pack(side="top")
		self.nextpage["command"] = self.next_page
		self.lastpage = tk.Button(self)
		self.lastpage["text"] = "Last Page"
		self.lastpage.pack(side="top")
		self.lastpage["command"] = self.last_page

	def set_page(self):
		try:
			self.pagetext = f"Page {self.iterate}"
			self.pagenumber.text = self.pagetext
			self.image2 = PhotoImage(file=f"Book/page_0{self.iterate}.png")
			print(f"page_0{self.iterate}.png")
			self.label.configure(image=self.image2)
			self.label.image = self.image2
		except:
			pass

	def next_page(self):
		self.iterate += 1
		self.set_page()

	def last_page(self):
		self.iterate -= 1
		self.set_page()


root = tk.Tk()
root.geometry("700x800")
app = Application(master=root)
app.mainloop()
