from machine import Pin
from time import sleep

led_green = Pin (13, Pin.OUT)
led_yellow = Pin (12, Pin.OUT)
led_red = Pin (14, Pin.OUT)

while True:
    #verde
    print ("SIGA")
    led_green.value(1)
    led_yellow.value(0)
    led_red.value(0)
    sleep(7)
    
    #amarelo
    print("ESPERE")
    led_green.value(0)
    led_yellow.value(1)
    led_red.value(0)
    sleep(3)
    
    #vermelho
    print("PARE")
    led_green.value(0)
    led_yellow.value(0)
    led_red.value(1)
    sleep(7)