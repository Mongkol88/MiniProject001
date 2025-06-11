# Windows App Example: For Python + PyQt5
```
pip install PyQt5
```
## Write a Simple App for Windows (Example: PyQt5) -------
```
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# Step 1: Create the application object
app = QApplication(sys.argv)

# Step 2: Create the main window
window = QWidget()
window.setWindowTitle('My First PyQt5 App')
window.setGeometry(100, 100, 300, 200)  # x, y, width, height

# Step 3: Add a label widget
label = QLabel('<h1>Hello, Windows with PyQt5!</h1>', parent=window)
label.move(50, 80)

# Step 4: Show the window
window.show()

# Step 5: Start the event loop
sys.exit(app.exec_())
```
## Run it:
```
python3 my_first_app.py
```
## Package as a Windows Executable
Use PyInstaller to create a .exe file.
```
pip install pyinstaller
```
## Build
Make a standalone executable
```
python -m PyInstaller --onefile --windowed my_first_app.py
```
## Executable file should be here:
```
Drive:\<YourPath>\basic-programming\first_win_coding\dist
```
## Run it:
```
Drive:\<YourPath>\basic-programming\first_win_coding\dist\my_first_app.exe
```

![Alt text](./my_first_app.png?raw=true "my_first_app")

The End.
