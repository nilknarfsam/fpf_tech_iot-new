import machine
import time

red_led = machine.Pin(5, machine.Pin.OUT)
yellow_led = machine.Pin(4, machine.Pin.OUT)
green_led = machine.Pin(2, machine.Pin.OUT)

while True:
    red_led.value(1)
    time.sleep(7)
    red_led.value(0)
    
    green_led.value(1)
    time.sleep(7)
    green_led.value(0)
    
    for i in range(6): # funcao para piscar
        green_led.value(1)
        time.sleep(0.25)
        green_led.value(0)
        time.sleep(0.25)
        
    yellow_led.value(1)
    time.sleep(3)
    yellow_led.value(0)