# Using External Circuit

Let's implement our own circuit. Here we control an LED with RBoard.

## LED

LED stands for Light Emitting Diode. It emits light when current flows through the LED. However, we must keep the maximum current for LED.

The simplest circuit is as follows, but this is the wrong circuit!

![wrong circuit](/images/curcuit_1.drawio.png)

We need to limit the current flowing to the LED. We add a resistor to the circuit.

![LED circuit](/images/curcuit_2.drawio.png)

## Make your curcuit

To build your circuit, we use the breadboard. The breadboard can connect electrical parts by inserting holes on the board. The holes on the same row are connected.

Look at the breadboard. The green boxed holes are connected, and the red boxed holes are also connected. However, the green and red holes are **not** connected.

![Connection](/images/breadboard_connection.jpg)

The Rboard can control the output voltage of the pins. The pin number is printed near the pins.

The curcuit is as follows:

![LED circuit](/images/curcuit_3.drawio.png)

With one LED, one resistor and two jumper wires you can create your own circuit.
The completed circuit looks like this:

![completed circuit](/images/completed_circuit.jpg)

**Note the LED connection.**

LED pins are oriented in a specific direction.
Current flows through the LED in the direction from the longest LED pin to the shortest LED pin.
No current flows in the opposite direction, so the LED will not work.

![LED connection](/images/led_direction.png)

![current in the cuicuit](/images/current_direction.png)



## LED blinking code

- To control LED circuit, use GPIO block in `microcom` extension.

![alt text](/images/use_gpio_block.png)


## Practice

1. Blink two LEDs on the breadboard.

<hr/>
<!--
[**Move to next**](./3rd_pwm.md)
-->

[**Back to top**](./README.md)
