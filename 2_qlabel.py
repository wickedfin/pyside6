import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.show()
# NOTE 아래 같은 html 형식의 입력도 가능함
label2 = QLabel("<font color=red size=40>Hello World!</font>")
label2.show()
app.exec_()