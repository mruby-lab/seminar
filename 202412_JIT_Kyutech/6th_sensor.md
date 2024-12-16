# Using a Temperature Sensor

Use a Temperature sensor "LM61", thermistor IC.

![LM61](/images/lm61.png)

The document of the sensor is: https://www.ti.com/lit/gpn/lm61

![MCP9701](/images/temp-sensor.png)

|RBoard Pins|LM61 Pins|
|---|---|
|3V3|1 V_DD|
|P15|2 V_out|
|GND|3 GND|

The output voltage is by following equation.

$$ Temperature[{}^{\circ}C] = (\, V_{out}[V]-0.6 \,) \times 100 $$

## Practice

1. Output temperature (in degree of Celsius).
1. Control LEDs by temperature, like a thermo alert.

<hr/>

[**Back to top**](./README.md)
