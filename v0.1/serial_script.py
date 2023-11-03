import serial, serial.tools.list_ports

arduino_path = serial.tools.list_ports.comports()[0].device

print(arduino_path)

s = serial.Serial(arduino_path, 115200, timeout=1)

print(s.read(1000))

s.write(b'1')
