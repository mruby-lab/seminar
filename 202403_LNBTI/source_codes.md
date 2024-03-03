
# Sample codes

## Blink LED (Pin.0)

```Ruby
led1 = GPIO.new(0)

while true do
  led1.write 1
  sleep 0.5
  led1.write 0
  sleep 0.5
end
```

## Blink two LEDs

```Ruby
led1 = GPIO.new(0)
led2 = GPIO.new(5)

while true do
  led1.write 1
  sleep 0.5
  led1.write 0
  sleep 0.5
  led2.write 1
  sleep 0.5
  led2.write 0
  sleep 0.5
end
```

## Blink LED (Pin.15)

```Ruby
led1 = GPIO.new(15)
led1.setmode(0)

while true do
  led1.write 1
  sleep 0.5
  led1.write 0
  sleep 0.5
end
```

## PWM

```Ruby
led1 = PWM.new(15)
led1.frequency 10000

while true do
  led1.duty 100
  sleep 0.5
  led1.duty 300
  sleep 0.5
  led1.duty 500
  sleep 0.5
  led1.duty 700
  sleep 0.5
end
```

## PWM

```Ruby
led1 = PWM.new(15)
led1.frequency 10000

while true do
  for i in 0..1023 do
    led1.duty i
    sleep 0.001
  end
  for i in 0..1023 do
    led1.duty 1023-i
    sleep 0.001
  end
end
```

## CdS

```Ruby
led1 = GPIO.new(0)
adc = ADC.new(20)

while true do
  v = adc.read
  if v<0.5 then
    led1.write 1
  else
    led1.write 0
  end
  sleep 0.1
end
```
