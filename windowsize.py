import os
import tkinter as tk
import math
from PIL import ImageTk, Image

imagedir = 'Book/'

root = tk.Tk()

sWidth = root.winfo_screenwidth()
sHeight = root.winfo_screenheight()

print(f"Monitor Width = {sWidth}px, Monitor Height = {sHeight}px")

entries = os.listdir(imagedir)

for x in range(len(entries)):
	imname = entries[x]
	image = Image.open(f"{imagedir}{imname}")
	iWidth,iHeight = image.size
	#print(f"Page Filename = {imname}, Page Width = {iWidth}px, Page Height = {iHeight}px")
	dict = {
		'name': imname,
		'width': iWidth,
		'height': iHeight
	}
	print(dict)