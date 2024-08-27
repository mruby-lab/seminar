# Web application

## setup Flask

- Install `Flask` into your environment.
    - Flask is a web framework written in Python.
    - 
```
pip install Flask
```

## Simple web server

- A simple web server
    - access to http://localhost:5000/ then the message is shown on your browser.
    - `@app.route("/")` describes the request path `/`,<br>
    and following function `home` responses the request.
    - access to http://localhost:5000/hello, `Hello` will be shown.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello() -> str:
    return "Web server is working."

@app.route("/hello")
def home() -> str:
    return "Hello"

if __name__ == "__main__":
    app.run()
```

## Using web server and serial communication

- two loops<br>
    - web server `app.run()`
    - serial port `while`
- Execute two loops concurrently
    - Using `threading`

## Thread sample

```python
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
```
