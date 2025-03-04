from machine import Pin
from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
atuador = Pin(4, Pin.OUT)
atuador.value(0)

while True:
    distance = sensor.distance_cm()
    print(distance)
    if distance <= 5 and distance > 0:
        atuador.value(1)
    elif distance > 5 and distance <= 10:
        atuador.value(1)
        sleep(0.25)
        atuador.value(0)
        sleep(0.25)
    elif distance > 10 and distance <= 25:
        atuador.value(1)
        sleep(0.5)
        atuador.value(0)
        sleep(0.5)
    elif distance > 25 and distance <= 50:
        atuador.value(1)
        sleep(1)
        atuador.value(0)
        sleep(1)
    sleep(0.1)
