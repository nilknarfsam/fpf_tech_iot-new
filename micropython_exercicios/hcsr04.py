from hcsr04 import HCSR04
from machine import Pin
from time import sleep

sensor = HCSR04(trigger_pin=21, echo_pin=19)

led = Pin(4, Pin.OUT)



while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(1)
    
    if distance < 10:
        led.value(1)
    else:
        led.value(0)
