from PyQt5 import QtWidgets,QtGui
app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle("hello")
window.setWindowIcon(QtGui.QIcon("icon.jpg"))
window.show()
app.exec()