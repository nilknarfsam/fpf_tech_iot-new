#usando esp32

from machine import Pin
from time import sleep

def acionar_led (led, time):
    led.on()
    sleep(time)
    led.off()
    
led_green = Pin (13, Pin.OUT)
led_yellow = Pin (12, Pin.OUT)
led_red = Pin (14, Pin.OUT)

while True:
    acionar_led(led_green, 4)
    
    for i in range(6):
        acionar_led(led_green, 0.25)
        sleep(0.25)
        
    acionar_led(led_yellow, 3)
    acionar_led(led_red, 7)