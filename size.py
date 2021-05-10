import os
import tkinter as tk
from PIL import Image

def start(imagedir,sWidth,sHeight):

	try:
		entries = os.listdir(imagedir)
	except FileNotFoundError:
		print("No image directory.")
		return

	pagesizes = {}

	for x in range(len(entries)):
		imagename = entries[x]
		image = Image.open(f"{imagedir}{imagename}")
		iWidth,iHeight = image.size
		
		dict = {
			'name': imagename,
			'width': iWidth,
			'height': iHeight
		}
		
		pagesizes[x] = dict

	widths = []
	heights = []
	
	for x in range(len(pagesizes)):
		widths.insert(x,pagesizes[x]['width'])
		heights.insert(x,pagesizes[x]['height'])

	maxwidth = (max(widths))
	minwidth = (min(widths))
	maxheight = (max(heights))
	minheight = (min(heights))
	
	scalew = 2
	scaleh = 1.2

	return sWidth,sHeight,scalew,scaleh