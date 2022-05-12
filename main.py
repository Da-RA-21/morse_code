from controller import *

"""
project idea: https://www.youtube.com/watch?v=delJJ9zHXio&t=140s
added: slightly expanded library to handle more characters, simple GUI app to gather input from user,
       time is handled a little differently from the originally for a more real feel in my opinion
"""

def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
