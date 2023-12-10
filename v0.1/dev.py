# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APRL_GUIv0_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(912, 777)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.valveBox = QtWidgets.QGroupBox(self.centralwidget)
        self.valveBox.setGeometry(QtCore.QRect(490, 350, 391, 381))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.valveBox.setFont(font)
        self.valveBox.setStyleSheet("")
        self.valveBox.setAlignment(QtCore.Qt.AlignCenter)
        self.valveBox.setObjectName("valveBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.valveBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.isoValLabel = QtWidgets.QLabel(self.valveBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isoValLabel.sizePolicy().hasHeightForWidth())
        self.isoValLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.isoValLabel.setFont(font)
        self.isoValLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.isoValLabel.setObjectName("isoValLabel")
        self.verticalLayout_2.addWidget(self.isoValLabel)
        self.isoValLabels = QtWidgets.QHBoxLayout()
        self.isoValLabels.setObjectName("isoValLabels")
        self.isoVal1Label = QtWidgets.QLabel(self.valveBox)
        self.isoVal1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.isoVal1Label.setObjectName("isoVal1Label")
        self.isoValLabels.addWidget(self.isoVal1Label)
        self.isoVal2Label = QtWidgets.QLabel(self.valveBox)
        self.isoVal2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.isoVal2Label.setObjectName("isoVal2Label")
        self.isoValLabels.addWidget(self.isoVal2Label)
        self.verticalLayout_2.addLayout(self.isoValLabels)
        self.isoRow = QtWidgets.QHBoxLayout()
        self.isoRow.setObjectName("isoRow")
        self.isoTog1 = AnimatedToggle(self.valveBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isoTog1.sizePolicy().hasHeightForWidth())
        self.isoTog1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.isoTog1.setFont(font)
        self.isoTog1.setObjectName("isoTog1")
        self.isoRow.addWidget(self.isoTog1)
        self.isoTog2 = AnimatedToggle(self.valveBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.isoTog2.setFont(font)
        self.isoTog2.setObjectName("isoTog2")
        self.isoRow.addWidget(self.isoTog2)
        self.verticalLayout_2.addLayout(self.isoRow)
        self.mainValLabel = QtWidgets.QLabel(self.valveBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainValLabel.sizePolicy().hasHeightForWidth())
        self.mainValLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mainValLabel.setFont(font)
        self.mainValLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainValLabel.setObjectName("mainValLabel")
        self.verticalLayout_2.addWidget(self.mainValLabel)
        self.mainValLabels = QtWidgets.QHBoxLayout()
        self.mainValLabels.setObjectName("mainValLabels")
        self.mainVal1Label = QtWidgets.QLabel(self.valveBox)
        self.mainVal1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.mainVal1Label.setObjectName("mainVal1Label")
        self.mainValLabels.addWidget(self.mainVal1Label)
        self.mainVal2Label = QtWidgets.QLabel(self.valveBox)
        self.mainVal2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.mainVal2Label.setObjectName("mainVal2Label")
        self.mainValLabels.addWidget(self.mainVal2Label)
        self.verticalLayout_2.addLayout(self.mainValLabels)
        self.mainRow = QtWidgets.QHBoxLayout()
        self.mainRow.setObjectName("mainRow")
        self.mainTog1 = AnimatedToggle(self.valveBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mainTog1.setFont(font)
        self.mainTog1.setObjectName("mainTog1")
        self.mainRow.addWidget(self.mainTog1)
        self.mainTog2 = AnimatedToggle(self.valveBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mainTog2.setFont(font)
        self.mainTog2.setObjectName("mainTog2")
        self.mainRow.addWidget(self.mainTog2)
        self.verticalLayout_2.addLayout(self.mainRow)
        self.ventValLabel = QtWidgets.QLabel(self.valveBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ventValLabel.setFont(font)
        self.ventValLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ventValLabel.setObjectName("ventValLabel")
        self.verticalLayout_2.addWidget(self.ventValLabel)
        self.ventValLabels = QtWidgets.QHBoxLayout()
        self.ventValLabels.setObjectName("ventValLabels")
        self.ventValLabel1 = QtWidgets.QLabel(self.valveBox)
        self.ventValLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.ventValLabel1.setObjectName("ventValLabel1")
        self.ventValLabels.addWidget(self.ventValLabel1)
        self.ventValLabel2 = QtWidgets.QLabel(self.valveBox)
        self.ventValLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.ventValLabel2.setObjectName("ventValLabel2")
        self.ventValLabels.addWidget(self.ventValLabel2)
        self.verticalLayout_2.addLayout(self.ventValLabels)
        self.ventRow = QtWidgets.QHBoxLayout()
        self.ventRow.setObjectName("ventRow")
        self.ventTog1 = AnimatedToggle(self.valveBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ventTog1.setFont(font)
        self.ventTog1.setObjectName("ventTog1")
        self.ventRow.addWidget(self.ventTog1)
        self.ventTog2 = AnimatedToggle(self.valveBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ventTog2.setFont(font)
        self.ventTog2.setObjectName("ventTog2")
        self.ventRow.addWidget(self.ventTog2)
        self.verticalLayout_2.addLayout(self.ventRow)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.rsoRow = QtWidgets.QHBoxLayout()
        self.rsoRow.setObjectName("rsoRow")
        self.armButton = QtWidgets.QPushButton(self.valveBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.armButton.setFont(font)
        self.armButton.setStyleSheet("QPushButton#armButton {background-color: rgb(170, 255, 0);}\n"
"QPushButton#armButton:checked {background-color: rgb(209, 21, 7); }")
        self.armButton.setCheckable(True)
        self.armButton.setChecked(False)
        self.armButton.setObjectName("armButton")
        self.rsoRow.addWidget(self.armButton)
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
        self.rsoRow.addWidget(self.abortButton)
        self.verticalLayout_2.addLayout(self.rsoRow)
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
        self.calibButton = QtWidgets.QPushButton(self.commandBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calibButton.setFont(font)
        self.calibButton.setObjectName("calibButton")
        self.verticalLayout.addWidget(self.calibButton)
        self.pressButton = QtWidgets.QPushButton(self.commandBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pressButton.setFont(font)
        self.pressButton.setObjectName("pressButton")
        self.verticalLayout.addWidget(self.pressButton)
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
        self.timer = QtWidgets.QLabel(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(10, 140, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.timer.setFont(font)
        self.timer.setFrameShape(QtWidgets.QFrame.Panel)
        self.timer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer.setLineWidth(4)
        self.timer.setAlignment(QtCore.Qt.AlignCenter)
        self.timer.setObjectName("timer")
        self.commandClear = QtWidgets.QPushButton(self.centralwidget)
        self.commandClear.setGeometry(QtCore.QRect(540, 310, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.commandClear.setFont(font)
        self.commandClear.setObjectName("commandClear")
        self.commandSave = QtWidgets.QPushButton(self.centralwidget)
        self.commandSave.setGeometry(QtCore.QRect(700, 310, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.commandSave.setFont(font)
        self.commandSave.setObjectName("commandSave")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(490, 20, 401, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 399, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.log = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.log.setGeometry(QtCore.QRect(0, 0, 391, 281))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.log.setFont(font)
        self.log.setFrameShape(QtWidgets.QFrame.Panel)
        self.log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.log.setLineWidth(4)
        self.log.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.log.setObjectName("log")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 912, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.valveBox.setTitle(_translate("MainWindow", "Valve Control Panel"))
        self.isoValLabel.setText(_translate("MainWindow", "Isolator Valves"))
        self.isoVal1Label.setText(_translate("MainWindow", "Kero"))
        self.isoVal2Label.setText(_translate("MainWindow", "LOX"))
        self.isoTog1.setText(_translate("MainWindow", "CheckBox"))
        self.isoTog2.setText(_translate("MainWindow", "CheckBox"))
        self.mainValLabel.setText(_translate("MainWindow", "Main Valves"))
        self.mainVal1Label.setText(_translate("MainWindow", "Kero"))
        self.mainVal2Label.setText(_translate("MainWindow", "LOX"))
        self.mainTog1.setText(_translate("MainWindow", "CheckBox"))
        self.mainTog2.setText(_translate("MainWindow", "CheckBox"))
        self.ventValLabel.setText(_translate("MainWindow", "Vent Valves"))
        self.ventValLabel1.setText(_translate("MainWindow", "Kero"))
        self.ventValLabel2.setText(_translate("MainWindow", "LOX"))
        self.ventTog1.setText(_translate("MainWindow", "CheckBox"))
        self.ventTog2.setText(_translate("MainWindow", "CheckBox"))
        self.armButton.setText(_translate("MainWindow", "Arm"))
        self.abortButton.setText(_translate("MainWindow", "Abort"))
        self.commandBox.setTitle(_translate("MainWindow", "Engine Commands"))
        self.calibButton.setText(_translate("MainWindow", "Valve Calibration"))
        self.pressButton.setText(_translate("MainWindow", "Pressurize Tanks"))
        self.leakButton.setText(_translate("MainWindow", "Leak Check"))
        self.purgeButton.setText(_translate("MainWindow", "Purge"))
        self.startupButton.setText(_translate("MainWindow", "Startup"))
        self.timer.setText(_translate("MainWindow", "Timer"))
        self.commandClear.setText(_translate("MainWindow", "Clear"))
        self.commandSave.setText(_translate("MainWindow", "Save"))
        self.log.setText(_translate("MainWindow", "Awaiting commands..."))
from qtwidgets import AnimatedToggle


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())