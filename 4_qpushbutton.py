#!/usr/bin/python

import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

# NOTE 아래는 slot들을 위한 decorator임. 기능은 잘모르지만 이렇게 해주래
@Slot()
def say_hello():
    print("Button clicked, Hello!")

# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()
# Run the main Qt loop
app.exec_()