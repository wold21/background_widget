import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QMovie


class Sticker(QtWidgets.QMainWindow):
    def __init__(self, img_path, xy, size=1.0, on_top=False):
        super(Sticker, self).__init__()

        self.img_path = img_path
        self.xy = xy
        self.from_xy = xy
        self.to_xy = xy
        self.speed = 60
        self.direction = [0, 0]  # x: 0(left), 1(right), y: 0(up), 1(down)
        self.size = size
        self.on_top = on_top

        self.setupUi()
        self.show()

    def walk(self, from_xy, to_xy, speed=60):
        self.from_xy = from_xy
        self.to_xy = to_xy
        self.speed = speed

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.__walkHandler)
        self.timer.start(1000 / self.speed)

    def __walkHandler(self):
        if self.xy[0] >= self.to_xy[0]:
            self.direction[0] = 0
        elif self.xy[0] < self.from_xy[0]:
            self.direction[0] = 1

        if self.direction[0] == 0:
            self.xy[0] -= 1
        else:
            self.xy[0] += 1

        if self.xy[1] >= self.to_xy[1]:
            self.direction[1] = 0
        elif self.xy[1] < self.from_xy[1]:
            self.direction[1] = 1

        if self.direction[1] == 0:
            self.xy[1] -= 1
        else:
            self.xy[1] += 1

        self.move(*self.xy)

    def setupUi(self):
        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)

        flags = QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint if self.on_top else QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        label = QtWidgets.QLabel(centralWidget)
        movie = QMovie(self.img_path)
        label.setMovie(movie)
        movie.start()
        movie.stop()

        w = int(movie.frameRect().size().width() * self.size)
        h = int(movie.frameRect().size().height() * self.size)
        movie.setScaledSize(QtCore.QSize(w, h))
        movie.start()

        self.setGeometry(self.xy[0], self.xy[1], w, h)

    def mouseDoubleClickEvent(self, e):
        QtWidgets.qApp.quit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    s = Sticker('gif/giphy.gif', xy=[1780, 200], size=0.3, on_top=True)
    s.walk(from_xy=[1780, 200], to_xy=[1780, 220], speed=12)

    # s1 = Sticker('gif/giphy (1).gif', xy=[1000, 500], size=0.3, on_top=True)

    s2 = Sticker('gif/giphy (2).gif', xy=[1700, 1000], size=0.5, on_top=True)

    s3 = Sticker('gif/giphy (3).gif', xy=[300, 1000], size=0.5, on_top=True)

    s4 = Sticker('gif/giphy (4).gif', xy=[200, 1000], size=0.5, on_top=True)

    s5 = Sticker('gif/giphy (6).gif', xy=[250, 900], size=0.3, on_top=True)

    s6 = Sticker('gif/giphy (5).gif', xy=[1710, 980], size=0.2, on_top=True)

    sys.exit(app.exec_())
