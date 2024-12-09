# PWM

The PWM is a power control method for digital microcontrollers. Generally, digital microcontrollers can only set the output voltage to HIGH or LOW. 
The PEM can control the output smoothly.

The PWM stands for Pulse Width Modulation, the output of the PWM signal is changing its HIGH and LOW voltage rapidly, and the ratio of HIGH and LOW can be controlled.

![PWM signal](/images/pwm.png)

## PWM program

The PWM block can output pwm signal.

![PWM program](/images/pwm_program.png)

The Ruby code is as follows:


- You can set the duty ratio 0 to 100, which is 0% power to 100% power output.

## Smooth control

If you use variables, you can control LED brightness smoothly. Use the "variable" block and the "repeat until" block.


## Practice

1. Control the LED on the breadboard.<br>
Pin number for PWM is passed by parameter of `PWM.new`.

<hr/>

[**Move to next**](./4th_sensor.md)

[**Back to top**](./README.md)
