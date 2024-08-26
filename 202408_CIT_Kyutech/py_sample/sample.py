import serial

readSer = serial.Serial('COM4', 19200, timeout=3)

while True:
    line = readSer.readline()
    print(line)
readSer.close()
