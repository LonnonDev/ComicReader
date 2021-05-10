import PyInstaller.__main__

PyInstaller.__main__.run([
	'--windowed',
	'--distpath ./',
	'--clean',
	'--onefile',
	'main.py'
])