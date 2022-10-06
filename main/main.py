import os
import sys
import PIL
from PIL import Image
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic, QtCore, QtGui, QtWidgets

app = QApplication(sys.argv)

class ImgComp(QMainWindow):
    def __init__(self):
        super(ImgComp, self).__init__()
        uic.loadUi("mainui.ui", self)

        self.actionQuit.triggered.connect(lambda x: app.quit())
        self.actionAdd.triggered.connect(self.open)

        self.add.clicked.connect(self.open)

    def open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.jpg)')
        print(fname)
        img = Image.open(fname[0])
        Height, Width = img.size

        img_resized = img.resize((Height, Width), Image.Resampling.LANCZOS)
        save_path = QFileDialog.getSaveFileName(self, 'Save Image', '', 'All files (*)')
        
        print(save_path)

        img.save(save_path[0] + "_compressed.jpg")


def main():
    window = ImgComp()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()