import sys

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, \
    QApplication


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(510,500)

        # add chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 490, 400)
        self.chat_area.setReadOnly(True)

        # add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 420, 420, 40)

        # add send button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(440, 420, 60, 40)

        self.show()


app = QApplication(sys.argv)
main_window = GUI()
sys.exit(app.exec())