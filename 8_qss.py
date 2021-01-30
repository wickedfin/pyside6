import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QLabel, QListWidget, QPushButton, QVBoxLayout,
                               QListWidgetItem, QHBoxLayout, QWidget, QApplication)

class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem("Item {}".format(i))
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)

        text = ("placeholder placeholder placeholder\n"
                "placeholder placeholder placeholder\n"
                "placeholder placeholder placeholder")

        # NOTE 아래 주석처럼 하면 되긴 함
        # text_widget = QLabel(text, alignment=Qt.AlignCenter)
        text_widget = QLabel(text)
        button = QPushButton("Something")

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])

    widget = Widget()
    widget.resize(800, 600)
    widget.show()
    
    with open("8_qss_file.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec_())