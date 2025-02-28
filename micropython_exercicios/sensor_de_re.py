from hcsr04 import HCSR04
from machine import Pin
from time import sleep

buzzer = Pin(18, Pin.OUT)
sensor = HCSR04(trigger_pin=21, echo_pin=19)

def toca_buzzer (time):
    buzzer.on()
    sleep(time/2)
    buzzer.off()
    sleep(time/2 )

while True:
    distancia = sensor.distance_cm()
    print(distancia)
    
    if distancia <= 6:
        buzzer.on()
    elif 5 < distancia <= 10:
        toca_buzzer(0.25)
    elif 10 < distancia <= 25:
        toca_buzzer(0.5)
    elif 25 < distancia <= 50:
        toca_buzzer(1)
    else:
        buzzer.off()
