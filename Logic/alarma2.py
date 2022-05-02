import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import pygame




class App(QWidget):

    def __init__(self):
        pygame.init()
        song = pygame.mixer.Sound('tarzan-ruft-seine.mp3')
        clock = pygame.time.Clock()
        song.play()

        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 300
        self.top = 50
        self.width = 1248
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('achtung2.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.show()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())




