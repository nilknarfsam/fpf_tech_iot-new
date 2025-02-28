from machine import Pin
from time import sleep

def simultaneo (led, led_fixo, time):
    led.on() 
    led_fixo.on() #led que fica fixo
    sleep(time)
    led.off()
       
def pisca_led (led, time, vezes):
    for i in range(vezes):
        led.on()
        sleep(time)
        led.off()
        sleep(time)

#semanforo 1
led_green = Pin (13, Pin.OUT)
led_yellow = Pin (12, Pin.OUT)
led_red = Pin (14, Pin.OUT)

#semaforo 2
led2_green = Pin (27, Pin.OUT)
led2_yellow = Pin (26, Pin.OUT)
led2_red = Pin (25, Pin.OUT)

while True:
    simultaneo(led_green, led2_red, 4)
    pisca_led(led_green, 0.25, 6)
    simultaneo(led_yellow, led2_red, 3)
    led2_red.value(0)
    simultaneo(led2_green, led_red, 4)
    pisca_led(led2_green, 0.25, 6)
    simultaneo(led_red, led2_yellow, 3)
    led2_yellow.value(0)
    simultaneo(led2_red, led2_red, 1) 
