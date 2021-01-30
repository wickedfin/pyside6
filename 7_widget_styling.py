import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

# NOTE QFontDatabase의 families() 함수로 사용 가능 폰트 확인할 수 있다는데 잘 안됨
# # if __name__ == "__main__":
#     app = QApplication()
#     w = QLabel("This is a placeholder text")
#     w.setAlignment(Qt.AlignCenter)
#     w.show()
#     sys.exit(app.exec_())

# NOTE 아래처럼 css 형식으로도 스타일링을 할 수 있음
if __name__ == "__main__":
    app = QApplication()
    w = QLabel("This is a placeholder text")
    w.setAlignment(Qt.AlignCenter)
    w.setStyleSheet("""
        background-color: #262626;
        color: #FFFFFF;
        font-family: Times New Roman;
        font-size: 18px;
    """)
    w.show()
    sys.exit(app.exec_())