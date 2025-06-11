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