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

# PySerial library for microcontroller access
import serial, serial.tools.list_ports


class Ui_MainWindow(object):

    ### AUTOGENERATED BY PYUIC5 ###

    def setupUi(self, MainWindow):

        # Initialize the log
        self.actionLog = ""

        # Initialize the serial connection
        self.arduino_path = serial.tools.list_ports.comports()[0].device
        self.connection = serial.Serial(self.arduino_path, 115200, timeout=1)    

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

        # First row of valveBox 

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



        self.isoValLabels = QtWidgets.QHBoxLayout()
        self.isoValLabels.setObjectName("isoValLabels")
        self.isoTog1 = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isoTog1.sizePolicy().hasHeightForWidth())
        self.isoTog1.setSizePolicy(sizePolicy)
        self.isoTog1.setObjectName("isoTog1")

        self.isoTog1.clicked.connect(lambda: self.toggleValve("Kero Isol valve (K1)", self.isoTog1.isChecked()))


        self.isoValLabels.addWidget(self.isoTog1)
        self.isoTog2 = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.isoTog2.setObjectName("isoTog2")

        self.isoTog2.clicked.connect(lambda: self.toggleValve("LOX Isol valve (K2)", self.isoTog2.isChecked()))


        self.isoValLabels.addWidget(self.isoTog2)
        self.verticalLayout_2.addLayout(self.isoValLabels)
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

        # Second row of valveBox

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
    

        self.mainValLabels = QtWidgets.QHBoxLayout()
        self.mainValLabels.setObjectName("mainValLabels")
        self.mainTog1 = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.mainTog1.setObjectName("mainTog1")

        self.mainTog1.clicked.connect(lambda: self.toggleValve("Kero main valve (K5)", self.mainTog1.isChecked()))


        self.mainRow.addWidget(self.mainTog1)
        self.mainTog2 = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.mainTog2.setObjectName("mainTog2")

        self.mainTog2.clicked.connect(lambda: self.toggleValve("LOX Main valve (K6)", self.mainTog2.isChecked()))

        self.mainRow.addWidget(self.mainTog2)
        self.verticalLayout_2.addLayout(self.mainRow)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)

        # Third row of valveBox
        self.purgeRow = QtWidgets.QHBoxLayout()
        self.purgeRow.setObjectName("purgeRow")
        self.purgeValLabel = QtWidgets.QLabel(self.valveBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.purgeValLabel.setFont(font)
        self.purgeValLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.purgeValLabel.setObjectName("purgeValLabel")
        self.verticalLayout_2.addWidget(self.purgeValLabel)

        self.purgeValLabels = QtWidgets.QHBoxLayout()
        self.purgeValLabels.setObjectName("purgeValLabels")
        self.purgeValLabel1 = QtWidgets.QLabel(self.valveBox)
        self.purgeValLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.purgeValLabel1.setObjectName("purgeValLabel1")
        self.purgeValLabels.addWidget(self.purgeValLabel1)
        self.purgeValLabel2 = QtWidgets.QLabel(self.valveBox)
        self.purgeValLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.purgeValLabel2.setObjectName("purgeValLabel2")
        self.purgeValLabels.addWidget(self.purgeValLabel2)
        self.verticalLayout_2.addLayout(self.purgeValLabels)

        self.purgeRow = QtWidgets.QHBoxLayout()
        self.purgeRow.setObjectName("purgeRow")

        self.purgeTog1 = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        
        self.purgeTog1.clicked.connect(lambda: self.toggleValve("Kero Purge valve (K3)", self.purgeTog1.isChecked()))

        font = QtGui.QFont()
        font.setPointSize(11)
        self.purgeTog1.setFont(font)
        self.purgeTog1.setObjectName("purgeTog1")
        self.purgeRow.addWidget(self.purgeTog1)

        self.purgeTog2 = AnimatedToggle(self.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        
        self.purgeTog2.clicked.connect(lambda: self.toggleValve("LOX Purge valve (K4)", self.purgeTog2.isChecked()))
        
        font = QtGui.QFont()
        font.setPointSize(11)
        self.purgeTog2.setFont(font)
        self.purgeTog2.setObjectName("purgeTog2")
        self.purgeRow.addWidget(self.purgeTog2)
        self.verticalLayout_2.addLayout(self.purgeRow)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)

        # Fourth row of valveBox
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
        self.armButton.clicked.connect(self.armAbort)


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
        self.abortButton.clicked.connect(self.abort)

        self.verticalLayout_2.addLayout(self.rsoRow)


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

        self.leakButton.clicked.connect(lambda: self.sequence("Leak check"))

        self.verticalLayout.addWidget(self.leakButton)
        self.purgeButton = QtWidgets.QPushButton(self.commandBox)

        self.purgeButton.clicked.connect(lambda: self.sequence("Engine purge"))

        self.purgeButton.setObjectName("purgeButton")
        self.verticalLayout.addWidget(self.purgeButton)
        self.startupButton = QtWidgets.QPushButton(self.commandBox)
        self.startupButton.setObjectName("startupButton")

        self.startupButton.clicked.connect(lambda: self.sequence("Engine startup"))

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
        font.setPointSize(11)
        self.log.setFont(font)
        self.log.setFrameShape(QtWidgets.QFrame.Panel)
        self.log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.log.setLineWidth(4)
        self.log.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.log.setObjectName("log")

        self.scrollArea.setWidget(self.log)
        MainWindow.setCentralWidget(self.centralwidget)
            
        self.commandClear = QtWidgets.QPushButton(self.centralwidget)
        self.commandClear.setGeometry(QtCore.QRect(540, 310, 131, 31))
        self.commandClear.setObjectName("commandClear")

        self.commandClear.clicked.connect(self.clearLog)

        self.commandSave = QtWidgets.QPushButton(self.centralwidget)
        self.commandSave.setGeometry(QtCore.QRect(700, 310, 131, 31))
        self.commandSave.setObjectName("commandSave")

        self.commandSave.clicked.connect(self.saveLog)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 20))
        self.menubar.setObjectName("menubar")


        # Menu and status bar (default with MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    # Enables the ABORT button when ARM is pressed 
    def armAbort(self):
        armButtonStatus = self.armButton.isChecked()
        self.abortButton.setEnabled(armButtonStatus)
        

    # Clock function for timer 
    def setClock(self):
        t = time.time()
        self.timer.setText(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))}")

    
    # Function for logging
    def logAction(self, name, state=''):

        t = time.time()
        currentTime = f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))}"

        self.actionLog += f"{currentTime} - {name} {state}\n"
        self.log.setText(self.actionLog)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

    
    # Clear the log
    def clearLog(self):
        self.actionLog = ""
        self.log.setText(self.actionLog)


    def abort(self):
        
        # Send abort through serial     
        self.connection.write(b'9\n')
        
        self.logAction("Abort Called")

    def toggleValve(self, name, state):

        valveStatus = "opened" if state else "closed"
        self.logAction(name, valveStatus)

        match(name):
            case "Kero Isol valve (K1)":
                self.connection.write(b'1\n')
                
            case "LOX Isol valve (K2)":
                self.connection.write(b'2\n')

            case "Kero Purge valve (K3)":
                self.connection.write(b'3\n')

            case "LOX Purge valve (K4)":
                self.connection.write(b'4\n')
                
            case "Kero Main valve (K5)":
                self.connection.write(b'5\n')
                
            case "LOX Main valve (K6)":
                self.connection.write(b'6\n')
                
            
        

        
    def sequence(self, name):

        self.logAction(name, "commanded")

        match(name):
            case "Leak check":
                self.connection.write(b'7\n')

                # Update button state
                self.isoTog1.toggle()
                QTimer.singleShot(1000, lambda: self.isoTog1.toggle())

                QTimer.singleShot(1000, lambda: self.isoTog2.toggle())      
                QTimer.singleShot(2000, lambda: self.isoTog2.toggle())

                QTimer.singleShot(2000, lambda: self.purgeTog1.toggle())      
                QTimer.singleShot(3000, lambda: self.purgeTog1.toggle())

                QTimer.singleShot(3000, lambda: self.purgeTog2.toggle())      
                QTimer.singleShot(4000, lambda: self.purgeTog2.toggle())

                QTimer.singleShot(4000, lambda: self.mainTog1.toggle())      
                QTimer.singleShot(5000, lambda: self.mainTog1.toggle())

                QTimer.singleShot(5000, lambda: self.mainTog2.toggle())      
                QTimer.singleShot(6000, lambda: self.mainTog2.toggle())
                 

            case "Engine purge":
                self.connection.write(b'9\n')
                self.purgeTog1.toggle()
                self.purgeTog2.toggle()
                self.mainTog1.toggle()
                self.mainTog2.toggle()
                
            case "Engine startup":
                self.connection.write(b'8\n')
                self.mainTog1.toggle()
                self.mainTog2.toggle()
                

        
        
        


    def saveLog(self):

        # For some reason, getSaveFileName returns a tuple. I found this workaround on StackOverflow lolololol
        fileName, filter = QtWidgets.QFileDialog.getSaveFileName(None, "Save log file", None, "(*.txt)")
        with open(fileName + ".txt", 'w') as save_file:
            save_file.write(self.actionLog)

    ### AUTOGENERATED BY PYUIC5 ###
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
        self.purgeValLabel.setText(_translate("MainWindow", "Purge Valves"))
        self.purgeValLabel1.setText(_translate("MainWindow", "Kero"))
        self.purgeValLabel2.setText(_translate("MainWindow", "LOX"))
        self.purgeTog1.setText(_translate("MainWindow", "CheckBox"))
        self.purgeTog2.setText(_translate("MainWindow", "CheckBox"))
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
