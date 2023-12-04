import sqlite3 as sql
import serial, serial.tools.list_ports 
import time
import random

i = 0

for x in serial.tools.list_ports.comports():
    print(f"{i}. {x}")
    i += 1

i = int(input("Enter the device you want to use"))

connect = serial.Serial(serial.tools.list_ports.comports()[i].device, 250000, timeout=1)



con = sql.connect("telemetry.db")
cur = con.cursor()

'''
Guide to Table Names:

NitroT - Nitrogen Tank transducer
KeroIso - Kero isolation transducer
LOXIso - LOX isolation transducer
KeroMani - Kero manifold transducer
LOXMani - LOX manifold transducer

KeroFlow - Kero Flow meter
LOXFlow - LOX Flow meter
'''


cur.execute("CREATE TABLE IF NOT EXISTS data(time, NitroT, LOXIso, KeroIso, LOXMani, KeroMani, LOXFlow, KeroFlow, engine)")

time.sleep(5)

while(True):
    input = connect.readline()
    print(input)
    try:
        nitrot, loxi, keroi, loxman, keroman, loxf, kerof, engine = input.decode('utf-8').strip().split()
        #print(f"INSERT INTO data VALUES ({time.time()}, {nitrot}, {loxi}, {keroi}, {loxman}, {keroman}, {loxf}, {kerof}, {engine});")
        cur.execute(f"INSERT INTO data VALUES ({time.time()}, {nitrot}, {loxi}, {keroi}, {loxman}, {keroman}, {loxf}, {kerof}, {engine});")
        con.commit()
        print("good insert")
    except:
        print("reliable protocol lmao")
        continue
