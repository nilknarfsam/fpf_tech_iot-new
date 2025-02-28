from machine import Pin, PWM
from time import sleep

LED_PIN = 21

ldr = ADC(Pin(4))

led = PWM(Pin(LED_PIN))
led.freq(1000)

brightness = 0 
fade_step = 5 

while True:  
    led.duty_u16(int(brightness * 4095 / 255)) 

    
    brightness = brightness + fade_step

    
    if ldr.read() <= 1000 or brightness >= 255:
        fade_step = -fade_step

    
    sleep(0.03)

