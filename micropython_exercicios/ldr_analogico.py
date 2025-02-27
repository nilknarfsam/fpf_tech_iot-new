from machine import ADC, Pin
from time import sleep

ldr = ADC(Pin(4))
led = Pin(21, Pin.OUT)

while True:
    print(ldr.read())    
    if ldr.read() < 1000:
        led.off()
    else:
        led.on()
    sleep(0.2)
