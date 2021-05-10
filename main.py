import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		
	def create_widgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Hello World\n(click me)"
		self.hi_there.pack(side="top")

root = tk.Tk()
root.geometry("700x800")
app = Application(master=root)
app.mainloop()