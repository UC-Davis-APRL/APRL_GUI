# Required Qt5 libraries
from re import I
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer

# Custom widget library by Martin Fitzpatrick (mfitzp) available on pypi 
from qtwidgets import AnimatedToggle

# Time library for the clock and sleep functions
import time
from time import sleep

# PySerial library for microcontroller access
import serial, serial.tools.list_ports

# Import pglive libraries for live data plotting
from pglive.sources.data_connector import DataConnector
from pglive.sources.live_plot import LiveLinePlot
from pglive.sources.live_axis_range import LiveAxisRange
import pyqtgraph

# Threading library for multi-thread plotting
from threading import Thread

# Library for SQL access
import sqlite3 as sql

# Pandas for converting SQL to csv
from pandas import read_sql_query

# Import the UI python files generated by pyuic5
from mainscreen import Ui_MainWindow
from telemetryscreen import Ui_telemetryScreen

# Set DPI scaling to play nice with Windows (I found this on StackOverflow)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.telemetry(self)


        # Replace all the default AnimatedToggles in the autogen file WHY IS THERE NO METHOD TO SPECIFY CONSTRUCTOR PARAMS GRRR
        # Scuffed but it works and hey it has color yippee.mp5
        self.ui.isoTog1 = AnimatedToggle(self.ui.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.ui.isoRow.replaceWidget(self.ui.isoTog1_old, self.ui.isoTog1)
        self.ui.isoTog1_old.deleteLater()
        self.ui.isoTog2 = AnimatedToggle(self.ui.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.ui.isoRow.replaceWidget(self.ui.isoTog2_old, self.ui.isoTog2)
        self.ui.isoTog2_old.deleteLater()
        self.ui.mainTog1 = AnimatedToggle(self.ui.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.ui.mainRow.replaceWidget(self.ui.mainTog1_old, self.ui.mainTog1)
        self.ui.mainTog1_old.deleteLater()
        self.ui.mainTog2 = AnimatedToggle(self.ui.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.ui.mainRow.replaceWidget(self.ui.mainTog2_old, self.ui.mainTog2)
        self.ui.mainTog2_old.deleteLater()
        self.ui.ventTog1 = AnimatedToggle(self.ui.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.ui.ventRow.replaceWidget(self.ui.ventTog1_old, self.ui.ventTog1)
        self.ui.ventTog1_old.deleteLater()
        self.ui.ventTog2 = AnimatedToggle(self.ui.valveBox, checked_color="#1b9611", bar_color=Qt.red, pulse_unchecked_color="#f1807e", pulse_checked_color="#a9f0d7")
        self.ui.ventRow.replaceWidget(self.ui.ventTog2_old, self.ui.ventTog2)
        self.ui.ventTog2_old.deleteLater()

        # Set default valve states
        self.ui.ventTog1.setChecked(True)
        self.ui.ventTog2.setChecked(True)

        # Button connections
        self.ui.isoTog1.clicked.connect(lambda: self.toggleValve("Kero Isol valve (K1)", self.ui.isoTog1.isChecked()))
        self.ui.isoTog2.clicked.connect(lambda: self.toggleValve("LOX Isol valve (K2)", self.ui.isoTog2.isChecked()))
        self.ui.mainTog1.clicked.connect(lambda: self.toggleValve("Kero Main valve (K3)", self.ui.mainTog1.isChecked()))
        self.ui.mainTog2.clicked.connect(lambda: self.toggleValve("LOX Main valve (K4)", self.ui.mainTog2.isChecked()))
        self.ui.ventTog1.clicked.connect(lambda: self.toggleValve("Kero Vent valve (K5)", self.ui.ventTog1.isChecked()))
        self.ui.ventTog2.clicked.connect(lambda: self.toggleValve("LOX Vent valve (K6)", self.ui.ventTog2.isChecked()))
        self.ui.armButton.clicked.connect(self.armAbort)
        self.ui.abortButton.clicked.connect(self.abort)
        self.ui.calibButton.clicked.connect(lambda: self.sequence("Valve calibration"))
        self.ui.pressButton.clicked.connect(lambda: self.sequence("Pressurize tanks"))
        self.ui.leakButton.clicked.connect(lambda: self.sequence("Leak check"))
        self.ui.purgeButton.clicked.connect(lambda: self.toggleValve("Engine purge valve (K7)", self.ui.purgeButton.isChecked()))
        self.ui.startupButton.clicked.connect(lambda: self.sequence("Engine startup"))
        self.ui.commandClear.clicked.connect(self.clearLog)
        self.ui.commandSave.clicked.connect(self.saveLog)
        self.ui.openStart.clicked.connect(self.connect_database)
        self.ui.stopClose.clicked.connect(self.close_database)
        self.ui.exportFrom.clicked.connect(self.export_database)

        # Clock
        self.clock = QTimer()
        self.clock.timeout.connect(self.setClock)
        self.clock.start(1000)



        # Initialize the log
        self.actionLog = ""

        # Initialize the serial connection
        self.arduino_path = serial.tools.list_ports.comports()[0].device
        self.connection = serial.Serial(self.arduino_path, 250000, timeout=1)
        self.connection.reset_output_buffer() # Nuke the output buffer in case crap is leftover from other instances

        # Initialize the graphs
        self.running = False

        self.tele.nitroGraph.setTitle("Nitrogen Tank Pressure")
        self.tele.nitroGraph.setLabel("left", "Pressure", units="PSI")
        self.tele.nitroGraph.setAxisItems({'bottom': pyqtgraph.DateAxisItem()})
        self.tele.nitroGraph.y_range_controller=LiveAxisRange(fixed_range=[0, 3000])
        self.tele.nitroPen = pyqtgraph.mkPen('#2DFE54', width=2)
        self.tele.nitroLine = LiveLinePlot(pen=self.tele.nitroPen)
        self.tele.nitroGraph.addItem(self.tele.nitroLine)
        self.nitroConnector = DataConnector(self.tele.nitroLine, max_points=100, update_rate=5)

        
        self.tele.tankGraph.setTitle("Kerosene / LOX Tank Pressures")
        self.tele.tankGraph.setLabel("left", "Pressure", units="PSI")
        self.tele.tankGraph.setAxisItems({'bottom': pyqtgraph.DateAxisItem()})
        self.tele.tankGraph.y_range_controller=LiveAxisRange(fixed_range=[0,1000])
        
        self.tele.keroPen = pyqtgraph.mkPen('#FF6700', width=2)
        self.tele.keroTankLine = LiveLinePlot(pen=self.tele.keroPen)
        self.tele.tankGraph.addItem(self.tele.keroTankLine)
        self.keroTankConnector = DataConnector(self.tele.keroTankLine, max_points=100, update_rate=5)
        
        self.tele.loxPen = pyqtgraph.mkPen('#8AC7DB', width=2)
        self.tele.loxTankLine = LiveLinePlot(pen=self.tele.loxPen)
        self.tele.tankGraph.addItem(self.tele.loxTankLine)
        self.loxTankConnector = DataConnector(self.tele.loxTankLine, max_points=100, update_rate=5)


        self.tele.manifoldGraph.setTitle("Kerosene / LOX Manifold Pressures")
        self.tele.manifoldGraph.setLabel("left", "Pressure", units="PSI")
        self.tele.manifoldGraph.setAxisItems({'bottom': pyqtgraph.DateAxisItem()})
        self.tele.manifoldGraph.y_range_controller=LiveAxisRange(fixed_range=[0,900])

        self.tele.keroInjLine = LiveLinePlot(pen=self.tele.keroPen)
        self.tele.manifoldGraph.addItem(self.tele.keroInjLine)
        self.keroInjConnector = DataConnector(self.tele.keroInjLine, max_points=100, update_rate=5)

        self.tele.loxInjLine = LiveLinePlot(pen=self.tele.loxPen)
        self.tele.manifoldGraph.addItem(self.tele.loxInjLine)
        self.loxInjConnector = DataConnector(self.tele.loxInjLine, max_points=100, update_rate=5)

        
        self.tele.flowGraph.setTitle("Kerosene / LOX Flow Rates")
        self.tele.flowGraph.setLabel("left", "Flow Rate", units="L/min")
        self.tele.flowGraph.setAxisItems({'bottom': pyqtgraph.DateAxisItem()})
        self.tele.flowGraph.y_range_controller=LiveAxisRange(fixed_range=[0,25])
        

        self.tele.keroFlow = LiveLinePlot(pen=self.tele.keroPen)
        self.tele.flowGraph.addItem(self.tele.keroFlow)
        self.keroFlowConnector = DataConnector(self.tele.keroFlow, max_points=100, update_rate=5)

        self.tele.loxFlow = LiveLinePlot(pen=self.tele.loxPen)
        self.tele.flowGraph.addItem(self.tele.loxFlow)
        self.loxFlowConnector = DataConnector(self.tele.loxFlow, max_points=100, update_rate=5)

        # Lock the controls
        self.enableControls(self.running)        



    # Enables the ABORT button when ARM is pressed 
    def armAbort(self):
        armButtonStatus = self.ui.armButton.isChecked()
        self.ui.abortButton.setEnabled(armButtonStatus)
        

    # Clock function for timer 
    def setClock(self):
        t = time.time()
        self.ui.timer.setText(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))}")

    
    # Function for logging
    def logAction(self, name, state=''):

        t = time.time()
        currentTime = f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))}"

        self.actionLog += f"{currentTime} - {name} {state}\n"
        self.ui.log.setText(self.actionLog)
        self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum())

    
    # Clear the log
    def clearLog(self):
        self.actionLog = ""
        self.ui.log.setText(self.actionLog)


    def abort(self):
        
        # Send abort through serial     
        self.connection.write(b'9\n')
        self.logAction("Abort Called")
        self.ui.purgeButton.toggle()   

    def toggleValve(self, name, state):

        valveStatus = "opened" if state else "closed"
        self.logAction(name, valveStatus)

        match(name):
            case "Kero Isol valve (K1)":
                self.connection.write(b'1\n')
                
            case "LOX Isol valve (K2)":
                self.connection.write(b'2\n')

            case "Kero Main valve (K3)":
                self.connection.write(b'3\n')
                
            case "LOX Main valve (K4)":
                self.connection.write(b'4\n')

            case "Kero Vent valve (K5)":
                self.connection.write(b'5\n')

            case "LOX Vent valve (K6)":
                self.connection.write(b'6\n')

            case "Engine purge valve (K7)":
                self.connection.write(b'9\n')
                
            
    
            
        

        
    def sequence(self, name):

        self.logAction(name, "commanded")

        match(name):
            case "Valve calibration":
                self.connection.write(b'7\n')

                # Update button state
                self.ui.isoTog1.toggle()
                self.ui.isoTog2.toggle()      
                self.ui.mainTog1.toggle()      
                self.ui.mainTog2.toggle()      
                self.ui.ventTog1.toggle()
                self.ui.ventTog2.toggle()   

                QTimer.singleShot(5000, lambda: self.ui.isoTog1.toggle())
                QTimer.singleShot(5000, lambda: self.ui.isoTog2.toggle())
                QTimer.singleShot(5000, lambda: self.ui.mainTog1.toggle())                      
                QTimer.singleShot(5000, lambda: self.ui.mainTog2.toggle())
                QTimer.singleShot(5000, lambda: self.ui.ventTog1.toggle())
                QTimer.singleShot(5000, lambda: self.ui.ventTog2.toggle())
                 

                
            case "Engine startup":
                self.connection.write(b'8\n')
                
                # Open mains, fire 5 seconds
                self.ui.mainTog1.toggle()
                self.ui.mainTog2.toggle()

                # Close mains + isol, open vent 
                QTimer.singleShot(5000, lambda: self.ui.isoTog1.toggle())
                QTimer.singleShot(5000, lambda: self.ui.isoTog2.toggle())
                QTimer.singleShot(5000, lambda: self.ui.mainTog1.toggle())                      
                QTimer.singleShot(5000, lambda: self.ui.mainTog2.toggle())
                QTimer.singleShot(5000, lambda: self.ui.ventTog1.toggle())
                QTimer.singleShot(5000, lambda: self.ui.ventTog2.toggle())


            # NO LEAK CHECK IN INO CODE YET
            case "Leak check":
                self.connection.write(b'\n')

            case "Pressurize tanks":
                self.connection.write(b"10\n")
                self.ui.isoTog1.toggle()
                self.ui.isoTog2.toggle()
                self.ui.ventTog1.toggle()
                self.ui.ventTog2.toggle()
                

        
    def enableControls(self, isRunning):
        # Lock out the controls when serial connection is not open so it doesn't crash
        self.ui.valveBox.setEnabled(isRunning)
        self.ui.commandBox.setEnabled(isRunning)


    def saveLog(self):

        # For some reason, getSaveFileName returns a tuple. I found this workaround on StackOverflow lolololol
        fileName, filter = QtWidgets.QFileDialog.getSaveFileName(None, "Save log file", None, "(*.txt)")
        with open(fileName + ".txt", 'w') as save_file:
            save_file.write(self.actionLog)

    
    def telemetry(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.tele = Ui_telemetryScreen()
        self.tele.setupUi(self.window)
        self.window.show()

    def connect_database(self):

        

        # Get the database file name
        fileName, filter = QtWidgets.QFileDialog.getSaveFileName(None, "Database file", None, "(*.db)")

        # Initialize the database connection
        self.readdatabase = sql.connect(fileName, check_same_thread=False)
        self.writedatabase = sql.connect(fileName, check_same_thread=False)
        self.writecursor = self.writedatabase.cursor()
        self.writecursor.execute("PRAGMA journal_mode=wal")
        self.writecursor.execute("CREATE TABLE IF NOT EXISTS data(time, NitroT, LOXIso, KeroIso, LOXMani, KeroMani, LOXFlow, KeroFlow, engine)")
        self.running = True

        # Unlock controls
        self.enableControls(self.running)

        self.ui.databaseInfo.setText(f"Connected to: {fileName}")

        Thread(target=self.telemetry_writer).start()
        Thread(target=self.telemetry_collector, args=(self.nitroConnector, 1)).start()
        Thread(target=self.telemetry_collector, args=(self.loxTankConnector, 2)).start()
        Thread(target=self.telemetry_collector, args=(self.keroTankConnector, 3)).start()
        Thread(target=self.telemetry_collector, args=(self.loxInjConnector, 4)).start()
        Thread(target=self.telemetry_collector, args=(self.keroInjConnector, 5)).start()
        Thread(target=self.telemetry_collector, args=(self.loxFlowConnector, 6)).start()
        Thread(target=self.telemetry_collector, args=(self.keroFlowConnector, 7)).start()
 


    def close_database(self):
        self.readdatabase.close()
        self.writedatabase.close()
        self.running=False
        self.enableControls(self.running)
        self.ui.databaseInfo.setText(f"Not Connected To Database")

    def export_database(self):
        databaseFilename, filter = QtWidgets.QFileDialog.getSaveFileName(None, "Database file", None, "(*.db)")
        csvFilename, filter = QtWidgets.QFileDialog.getSaveFileName(None, "Database file", None, "(*.csv)")

        # Shamelessly stolen from StackOverflow
        conn = sql.connect(databaseFilename, isolation_level=None, detect_types=sql.PARSE_COLNAMES)
        db_df = read_sql_query("SELECT * FROM data", conn)
        db_df.to_csv(csvFilename, index=False)

        self.ui.databaseInfo.setText(f"{databaseFilename} exported to {csvFilename}")

    
    def telemetry_writer(self):
        while(self.running):
            input = self.connection.readline()
            
            try:
                nitrot, loxi, keroi, loxman, keroman, loxf, kerof, engine = input.decode('utf-8').strip().split()
                #print(f"INSERT INTO data VALUES ({time.time()}, {nitrot}, {loxi}, {keroi}, {loxman}, {keroman}, {loxf}, {kerof}, {engine});")
                self.writecursor.execute(f"INSERT INTO data VALUES ({time.time()}, {nitrot}, {loxi}, {keroi}, {loxman}, {keroman}, {loxf}, {kerof}, {engine});")
                self.writedatabase.commit()
                print("good insert")
            except:
                print("reliable protocol lmao")
                continue
           
    


    def telemetry_collector(self, connector, index):
        while self.running:
            self.readcursor = self.readdatabase.cursor()
            self.output = self.readcursor.execute("SELECT * FROM data ORDER BY time DESC LIMIT 1;")
            for x in self.output:                              
                #volts = (5.0 / 8388608) * float(x[index])
                volts = float(x[index])
                if index == 1:
                    reading = ((volts - 0.48) / 1.92) * 3000
                elif index == 6 or index == 7:
                    reading = ((volts - 0.48) / 1.92) * 20
                else:
                    reading = ((volts - 0.48) / 1.92) * 1000
                
                print(volts)
                print(reading)

                connector.cb_append_data_point(reading, x[0])
            sleep(0.2)
     

    def closeEvent(self, event):
        if self.running:
            self.running = False
            sleep(0.2)
            self.readdatabase.close()
            self.writedatabase.close()
        self.connection.close() 
        QtWidgets.QApplication.quit()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    
    