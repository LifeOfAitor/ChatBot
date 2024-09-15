import sys

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, \
    QApplication
from backednd import ChatBot
import threading


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = ChatBot()
        self.setMinimumSize(510, 500)

        # add chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 490, 400)
        self.chat_area.setReadOnly(True)

        # add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 420, 420, 40)
        # implement send message with enter key
        self.input_field.returnPressed.connect(self.send_message)
        
        # add send button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(440, 420, 60, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text()
        self.chat_area.append(f"User: {user_input}")
        self.input_field.clear()
        # create a thread for bot response
        thread = threading.Thread(target=self.get_bot_response,
                                  args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        # connect with openai API
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"Bot: {response}")


app = QApplication(sys.argv)
main_window = GUI()
sys.exit(app.exec())
