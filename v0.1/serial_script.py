import serial, serial.tools.list_ports

arduino_path = serial.tools.list_ports.comports()[0].device

s = serial.Serial(arduino_path, 115200, timeout=1)

def write_read(x):
    print(bytes(x, 'utf-8') + b'\n')
    s.write(bytes(x, 'utf-8') + b'\n')
    data = s.readline()
    return data

while True:
    num = input("Enter a number: ")
    value  = write_read(num)
    print(value)