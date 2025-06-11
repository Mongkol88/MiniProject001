import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# Step 1: Create the application object
app = QApplication(sys.argv)

# Step 2: Create the main window
window = QWidget()
window.setWindowTitle('My First PyQt5 App')
window.setGeometry(100, 100, 500, 200)  # x, y, width, height

# Step 3: Add a label widget
label = QLabel('<h1>Hello, Windows with PyQt5!</h1>', parent=window)
label.move(50, 80)

# Step 4: Show the window
window.show()

# Step 5: Start the event loop
sys.exit(app.exec_())
