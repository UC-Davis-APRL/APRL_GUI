import serial, serial.tools.list_ports

#arduino_path = serial.tools.list_ports.comports()[0].device

for x in serial.tools.list_ports.comports():
    print(x.device)

path = input("Enter the device you want to use\n")

connection = serial.Serial(path, 115200, timeout=1)

file = open("test.txt", "w")

def write_read(x):
    print(bytes(x, 'utf-8') + b'\n')
    connection.write(bytes(x, 'utf-8') + b'\n')
    data = connection.readline()
    return data

flag = True

while flag:
    num = input("Enter a number: ")
    file.write(write_read(num).decode())
    if(input("Continue? y/n") == 'n'):
        flag = False

file.close()