from machine import Pin
import dht
from time import sleep

data_pin = dht.DHT11(Pin(18))

while True:
    print("Temperatura: ", data_pin.temperature(), " | Umidade: ", data_pin.humidity())
    sleep(1)
    
