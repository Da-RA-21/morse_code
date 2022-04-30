from PyQt5.QtWidgets import *
from morse_gui import Ui_MainWindow
from morse import *
from playsound import playsound
from time import sleep

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.translateButton.clicked.connect(lambda: self.translate_text())
        self.playButton.clicked.connect(lambda: self.play_morse())

    def translate_text(self):
        string = self.translateInput.toPlainText()

        self.morseOutput.setPlainText(translate(string))

    def play_morse(self):
        for char in self.morseOutput.toPlainText():
            if char in morse_dict:
                if char == '.':
                    playsound(r'\Users\rasha\PycharmProjects\morse_code\dit.mp3')
                elif char == '-':
                    playsound(r'\Users\rasha\PycharmProjects\morse_code\dah.mp3')
                else:
                    sleep(0.5)
            else:
                continue
