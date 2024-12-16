# Using a Piezoelectric device

- Piezoelectric device can make a sound at the specified frequency.

## Piezoelectric devices

In piezoelectric device, the thickness of the device changes when voltage is applied. So the circuit to drive a piezoelectric device is simple.

![piezo](/images/piezo_device.png)

![piezo circuit](/images/piezo.drawio.png)

## Make a sound 

- To make a sound with a piezoelectric device, the voltage should be repeatedly applied.

The following program is one idea about making a sound.

![suond program 1](/images/sound1.png)

- By changing the `wait` time, the sound can be changed.
- For example, setting both to 0.002 will result in a lower sound.

However, this method is difficult to make a variety of sounds.

## Make a sound at specific frequency

- This program is only by ruby code. Change programming tab to "Ruby".

![Change to Ruby tab](/images/ruby_tab.png)

- Then write the following program code.

```Ruby
pwm15 = PWM.new( 15 )
pwm15.duty( 50 )
loop do
  pwm15.frequency( 440 )
  sleep(1)
  pwm15.frequency( 880 )
  sleep(1)
end
```

![suond program 2](/images/sound2.png)

## Practice

- Change the sound, if possible, play short music!
- To increase the sound frequency, it becomes to the ultrasonic. Of course, we can not hear the ultrasonic. Check the frequency of ultrasonic.

<hr/>

[**Move to next**](./6th_sensor.md)

[**Back to top**](./README.md)
