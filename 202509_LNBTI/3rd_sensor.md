# Using a Sensor

We'll use a brightness sensor called a photo-resistor, also known as a CdS sensor.

The resistance value of the CdS sensor varies with brightness. The following circuit can detect the brightness.

![cds circuit](/images/adc_circuit.png)

- 3V3 pin outputs constant voltage of 3.3V.
- A0 is connected to ADC which can measure the voltage of A0.

## ADC

- ADC(Analog Digital Converter) measures the voltage at specified pin.
- Because the voltage is analog value, the conversion to digital value is needed.

## ADC Program

ADC (Analog Digital Converter) is a device that can measure the connected input voltage.

The following block program measures the brightness (voltage of P20).

![cds block program](/images/adc_program_stm.png)

Source code of this program:

```Ruby
gpio13 = GPIO.new( 13, GPIO::OUT )
adc0 = ADC.new( 0 )
loop do
  if adc0.read_raw > 200
    gpio13.write( 1 )
  else
    gpio13.write( 0 )
  end
  sleep(0.1)
end
```

## Practice

1. Turn on (or off) an external LED by brightness, it's like an automatic light.
2. Turn on red/green LED by brightness. If the condition is dark, turn on the red LED, otherwise turn on the green LED. 

<hr/>


[**Back to top**](./README.md)
