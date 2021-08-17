import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFileDialog, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap

app = QApplication([])

def closeApp():
    sys.exit() 

widget = QWidget()
widget.setWindowTitle("PICTURE_VIEW")


label = QtWidgets.QLabel(widget)
btn =QtWidgets.QPushButton(label)
btn.setText('push2quit')
btn.clicked.connect(closeApp)
options = QFileDialog.Options()
options |= QFileDialog.DontUseNativeDialog
fileName, _ = QFileDialog.getOpenFileName(widget,"Wybierz plik obrazu","","JPG Files (*.jpg);;png Files (*.png)", options=options)
if fileName:
    pixmap = QPixmap(fileName)
    label.setPixmap(pixmap)
    widget.resize(pixmap.width(),pixmap.height())
else:
    closeApp()

widget.show()
btn.show()
sys.exit(app.exec_())