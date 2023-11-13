from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from qtwidgets import AnimatedToggle
from dev import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.isoTog1 = AnimatedToggle(self.ui.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.ui.isoRow.replaceWidget(self.ui.isoTog1, AnimatedToggle(self.ui.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7"))
        #self.ui.isoTog1.hide()






if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    