import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter

class NumberDisplayApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compteur de Nombres")
        self.setGeometry(0, 0, 800, 600)
        self.showFullScreen()

        self.square_size = 20  # Taille plus petite des carrés
        self.squares = []

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.number_label = QLabel("0", alignment=Qt.AlignCenter)
        font = self.number_label.font()
        font.setPointSize(150)
        self.number_label.setFont(font)
        layout.addWidget(self.number_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_display)
        self.current_number = 0  # Compteur actuel
        self.timer.start(10)

    def update_display(self):
        self.current_number +=2
        self.number_label.setText(str(self.current_number))
        self.add_square()

        if self.current_number >= 2600:
            self.timer.stop()

        self.update()

    def add_square(self):
        x = random.randint(0, self.width() - self.square_size)
        y = random.randint(0, self.height() - self.square_size)



         # Vérifier si la position du carré chevauche la zone du compteur
        counter_x = self.number_label.geometry().x()
        counter_y = self.number_label.geometry().y()
        counter_width = self.number_label.geometry().width()
        counter_height = self.number_label.geometry().height()

        while counter_x < x < counter_x + counter_width and counter_y < y < counter_y + counter_height:
            x = random.randint(0, self.width() - self.square_size)
            y = random.randint(0, self.height() - self.square_size)

        self.squares.append((x, y))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for x, y in self.squares:
            painter.fillRect(x, y, self.square_size, self.square_size, QColor("red"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumberDisplayApp()
    window.show()
    sys.exit(app.exec_())
