import threading
import time
from flask import Flask
import serial
import json


app = Flask(__name__)

ser = serial.Serial('COM4', 19200, timeout=3)

line_buffer = []

def serial_loop():
    global ser, line_buffer
    while True:
        line = ser.readline() 
        print(line)
        line_buffer.append( line )
        time.sleep(1)


@app.route("/")
def hello() -> str:
    global line_buffer
    data = line_buffer
    line_buffer = []
    return str(data)


if __name__ == "__main__":
    thread1 = threading.Thread(target=serial_loop)
    thread1.start()

    app.run()
