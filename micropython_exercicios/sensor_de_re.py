from hcsr04 import HCSR04
from machine import Pin
from time import sleep

buzzer = Pin(18, Pin.OUT)
sensor = HCSR04(trigger_pin=21, echo_pin=19)

def toca_buzzer (time):
    buzzer.on()
    sleep(time)
    buzzer.off()
    sleep(time)

while True:
    distancia = sensor.distance_cm()
    print(distancia)

    if distancia < 5:
        toca_buzzer(0.2)
    elif 5 < distancia < 10:
        toca_buzzer(0.5)
    elif 10 < distancia < 15:
        toca_buzzer(1)
    else:
        sleep(0.1)
