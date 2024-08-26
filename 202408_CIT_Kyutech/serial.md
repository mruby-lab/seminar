# Serial Communication

## setup python

- Install `pyserial` into your environment.
    - Serial communication lib.
    - Connect RBoard and your python program
- Documents in https://github.com/pyserial/pyserial

```
pip install pyserial
```

## simple serial program

- Get lines from RBoard via serial
    - `COM4` is serial port name, which depends on your laptop
    - 

```python
import serial

readSer = serial.Serial('COM4', 19200, timeout=3)

while True:
    line = readSer.readline()
    print(line)
readSer.close()
```

