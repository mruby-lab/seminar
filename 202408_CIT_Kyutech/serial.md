# Serial Communication

## setup pyserial

- Install `pyserial` into your environment.
    - Serial communication lib.
    - Connect RBoard and your python program
    - Documents in https://github.com/pyserial/pyserial

```
pip install pyserial
```


## simple serial program

- Get lines from RBoard via serial
    - `COM4` is a serial port name, which depends on your laptop
- [source code](./py_sample/sample.py)

```python
import serial

ser = serial.Serial('COM4', 19200, timeout=3)

for _ in range(10):
    line = ser.readline()
    print(line)

ser.readline()
```

- `serial.Serial` creates serial access object
    - params are port name, serial speed
- `readline` read one line from serial
- `close` closes serial port

## Practice

- Output temperature value on your console
- Output "Hot", "Cool", or "Cold" by the temperature
    - using condition in python program<br>
      do not change your Rboard program

## Problems

- Sometimes miss the getting data
- Acquired data is string
    - temperature is floating point value

## Misc

- Showing serial port list
- [source code](./py_sample/port_list.py)

```python
import serial
from serial.tools import list_ports

ports = list_ports.comports() 

for port in ports:
    print( port.device, ":", port )
```

