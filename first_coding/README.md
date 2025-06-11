# Example: For Python + PyQt5
```
sudo apt update
sudo apt install python3 python3-pyqt5
python3 -m pip install PyQt5
sudo apt install python3-venv python3-full
python3 -m venv .venv
source .venv/bin/activate
```
Or if using Tkinter (already included in Python by default):
```
sudo apt install python3-tk
```

## Write a Simple App (Example: PyQt5) -------
```
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('My First Linux Desktop App')
window.setGeometry(100, 100, 300, 200)

label = QLabel('<h1>Hello, Linux!</h1>', parent=window)
label.move(60, 80)

window.show()
sys.exit(app.exec_())
```
## Run it:
```
python3 my_first_app.py
```
## Package It
Later, you can package your app into a .deb file or AppImage to make it easier to distribute.
Tools:
fpm (package builder)

## Install the PyInstaller
```
pip install pyinstaller
```
## Make a standalone executable
```
pyinstaller --onefile \
  --hidden-import PyQt5.QtNetwork \
  my_first_app.py
```




