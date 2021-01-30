from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl

app = QApplication([])
view = QQuickView()
url = QUrl("3_about_qml.qml")

view.setSource(url)
# NOTE 아래 줄은 데스크탑용으로 개발할 때 추가해주라던데 용도는 모르겠음
view.setResizeMode(QQuickView.SizeRootObjectToView) 
view.show()
app.exec_()