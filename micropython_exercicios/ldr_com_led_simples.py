from machine import Pin
from time import sleep

ldr = Pin(21, Pin.IN)
led = Pin(18, Pin.OUT)

while True:
    led.value(ldr.value())
    print(ldr.value())
    sleep(0.1)
