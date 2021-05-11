@ECHO OFF
pyinstaller --onefile main.py
"C:\Program Files\7-Zip\7z.exe" a -tzip -r "ComicReaderX.X.X.zip" ".\dist\*"
