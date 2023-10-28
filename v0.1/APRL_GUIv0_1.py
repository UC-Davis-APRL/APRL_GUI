# APRL_GUI v0.1
# @author Jason Huang
# 
# A PyQt5 frontend for controlling the engine and viewing telemetry.

# AUTOGENERATED CODE:
#   Form implementation generated from reading ui file 'APRL_GUIv0_1.ui'
#   Created by: PyQt5 UI code generator 5.15.10


# Required Qt5 libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer

# Custom widget library by Martin Fitzpatrick (mfitzp) available on pypi 
from qtwidgets import AnimatedToggle

# Time library for the clock
import time


class Ui_MainWindow(object):

    ### AUTOGENERATED BY PYUIC5 ###

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 777)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.valveBox = QtWidgets.QGroupBox(self.centralwidget)
        self.valveBox.setGeometry(QtCore.QRect(490, 350, 391, 381))

        font = QtGui.QFont()
        font.setPointSize(11)

        # valveBox (box containing valve controls)
        self.valveBox.setFont(font)
        self.valveBox.setAlignment(QtCore.Qt.AlignCenter)
        self.valveBox.setObjectName("valveBox") 

        # Layout of items inside valveBox
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.valveBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.valveBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        # First row of valveBox 
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.isoTog1 = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isoTog1.sizePolicy().hasHeightForWidth())
        self.isoTog1.setSizePolicy(sizePolicy)
        self.isoTog1.setObjectName("isoTog1")
        self.horizontalLayout.addWidget(self.isoTog1)
        self.isoTog2 = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.isoTog2.setObjectName("isoTog2")
        self.horizontalLayout.addWidget(self.isoTog2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.valveBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        # Second row of valveBox
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainTog1 = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.mainTog1.setObjectName("mainTog1")
        self.horizontalLayout_2.addWidget(self.mainTog1)
        self.mainTog2 = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.mainTog2.setObjectName("mainTog2")
        self.horizontalLayout_2.addWidget(self.mainTog2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)

        # Third row of valveBox
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.valveBox)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.purgeTog = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.purgeTog.setObjectName("purgeTog")
        self.horizontalLayout_3.addWidget(self.purgeTog)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)

        # Fourth row of valveBox
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.armButton = QtWidgets.QPushButton(self.valveBox, clicked=lambda: armAbort())
        font = QtGui.QFont()
        font.setPointSize(11)
        self.armButton.setFont(font)
        self.armButton.setStyleSheet("QPushButton#armButton {background-color: rgb(170, 255, 0);}\n"
"QPushButton#armButton:checked {background-color: rgb(209, 21, 7); }")
        self.armButton.setCheckable(True)
        self.armButton.setChecked(False)
        self.armButton.setObjectName("armButton")
        self.horizontalLayout_4.addWidget(self.armButton)
        self.abortButton = QtWidgets.QPushButton(self.valveBox)
        self.abortButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.abortButton.setFont(font)
        self.abortButton.setStyleSheet("QPushButton#abortButton:enabled {background-color: rgb(170, 255, 0);}\n"
"QPushButton#abortButton:checked {background-color: rgb(209, 21, 7); }")
        self.abortButton.setCheckable(True)
        self.abortButton.setChecked(False)
        self.abortButton.setFlat(False)
        self.abortButton.setObjectName("abortButton")
        self.horizontalLayout_4.addWidget(self.abortButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        # commandBox (box with command sequence buttons)
        self.commandBox = QtWidgets.QGroupBox(self.centralwidget)
        self.commandBox.setGeometry(QtCore.QRect(10, 350, 391, 381))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.commandBox.setFont(font)
        self.commandBox.setAlignment(QtCore.Qt.AlignCenter)
        self.commandBox.setFlat(False)
        self.commandBox.setObjectName("commandBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.commandBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leakButton = QtWidgets.QPushButton(self.commandBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leakButton.setFont(font)
        self.leakButton.setObjectName("leakButton")
        self.verticalLayout.addWidget(self.leakButton)
        self.purgeButton = QtWidgets.QPushButton(self.commandBox)
        self.purgeButton.setObjectName("purgeButton")
        self.verticalLayout.addWidget(self.purgeButton)
        self.startupButton = QtWidgets.QPushButton(self.commandBox)
        self.startupButton.setObjectName("startupButton")
        self.verticalLayout.addWidget(self.startupButton)


        # Timer widget in upper left corner
        
        self.timer = QtWidgets.QLabel(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(10, 140, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.timer.setFont(font)
        self.timer.setFrameShape(QtWidgets.QFrame.Panel)
        self.timer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer.setLineWidth(4)
        self.timer.setAlignment(QtCore.Qt.AlignCenter)
        self.timer.setObjectName("timer")


        self.clock = QTimer()
        self.clock.timeout.connect(self.setClock)
        self.clock.start(1000)

        
        # Logging widget in upper right corner
        self.log = QtWidgets.QLabel(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(490, 20, 391, 281))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.log.setFont(font)
        self.log.setFrameShape(QtWidgets.QFrame.Panel)
        self.log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.log.setLineWidth(4)
        self.log.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.log.setObjectName("log")
        self.commandClear = QtWidgets.QPushButton(self.centralwidget)
        self.commandClear.setGeometry(QtCore.QRect(540, 310, 131, 31))
        self.commandClear.setObjectName("commandClear")
        self.commandSave = QtWidgets.QPushButton(self.centralwidget)
        self.commandSave.setGeometry(QtCore.QRect(700, 310, 131, 31))
        self.commandSave.setObjectName("commandSave")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 20))
        self.menubar.setObjectName("menubar")

        # Text buffer holding the action log
        log = ""

        # Menu and status bar (default with MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # Enables the ABORT button when ARM is pressed 
        def armAbort():
            armButtonStatus = self.armButton.isChecked()
            self.abortButton.setEnabled(armButtonStatus)
            

    # Clock function for timer 
    def setClock(self):
        t = time.time()
        self.timer.setText(f"{time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(t))}")

    
    # Toggle function for logging
    def logAction(self, objectName, action):

        t = time.time()
        currentTime = f"{time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(t))}"

        actionLog += f"{currentTime}\n"
        self.log.setText(actionLog)



    ### AUTOGENERATED BY PYUIC5 ###
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.valveBox.setTitle(_translate("MainWindow", "Valve Control Panel"))
        self.label.setText(_translate("MainWindow", "Isolator Valves"))
        self.isoTog1.setText(_translate("MainWindow", "CheckBox"))
        self.isoTog2.setText(_translate("MainWindow", "CheckBox"))
        self.label_2.setText(_translate("MainWindow", "Main Valves"))
        self.mainTog1.setText(_translate("MainWindow", "CheckBox"))
        self.mainTog2.setText(_translate("MainWindow", "CheckBox"))
        self.label_3.setText(_translate("MainWindow", "Purge Valve"))
        self.purgeTog.setText(_translate("MainWindow", "CheckBox"))
        self.armButton.setText(_translate("MainWindow", "Arm"))
        self.abortButton.setText(_translate("MainWindow", "Abort"))
        self.commandBox.setTitle(_translate("MainWindow", "Engine Commands"))
        self.leakButton.setText(_translate("MainWindow", "Leak Check"))
        self.purgeButton.setText(_translate("MainWindow", "Purge"))
        self.startupButton.setText(_translate("MainWindow", "Startup"))
        self.timer.setText(_translate("MainWindow", "Timer"))
        self.log.setText(_translate("MainWindow", "Awaiting commands..."))
        self.commandClear.setText(_translate("MainWindow", "Clear"))
        self.commandSave.setText(_translate("MainWindow", "Save"))




### AUTOGENERATED BY PYUIC ###
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
