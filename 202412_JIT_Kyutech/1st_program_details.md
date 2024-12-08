# 1st Program Details

**How was the 1st RBoard program?**

## Blocks

The 1st program was like this:<br>
![1st program](/images/step2.png)

`GPIO` stands for general purpose input and output, which is directly connected to a pin (or a wire) on the RBoard.

First select `input` or `output` for GPIO. This is the 1st row of blocks. Set LED1, which is a green LED, to output.

Then blink an LED forever, use the forever block and turn LED1 on and off with a short wait. LED1 is a green LED.

## mruby program

Your implemented blocks are automatically converted to mruby source code.

You can see the converted code by clicking on the "Ruby" tab.

![mruby code](/images/mruby_code.png)

## Note

Now we control real device! 

For a real device (or a real product), time (or timing) is important.

In microcontroller programming, concerning time is implemented by the "sleep" function. The "sleep" function is "wait xx seconds" in block programming.

Wait time accept floting point number.

## Practice

1. Change the blinking speed.
2. Change the LED.
3. Blink two LEDs.



<hr/>

[**Move to next**](./2nd_circuit.md)

[**Back to top**](./README.md)
