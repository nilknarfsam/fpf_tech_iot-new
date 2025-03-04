from machine import Pin
from time import sleep

#setando os pins
a = Pin(2, Pin.OUT)
b = Pin(15, Pin.OUT)
c = Pin(17, Pin.OUT)
d = Pin(5, Pin.OUT)
e = Pin(18, Pin.OUT)
f = Pin(4, Pin.OUT)
g = Pin(16, Pin.OUT)

pins = [a,b,c,d,e,f,g]

#### = [a,b,c,d,e,f,g]
num0 = [1,1,1,1,1,1,0]
num1 = [0,1,1,0,0,0,0]
num2 = [1,1,0,1,1,0,1]
num3 = [1,1,1,1,0,0,1]
num4 = [0,1,1,0,0,1,1]
num5 = [1,0,1,1,0,1,1]
num6 = [1,0,1,1,1,1,1]
num7 = [1,1,1,0,0,0,0]
num8 = [1,1,1,1,1,1,1]
num9 = [1,1,1,1,0,1,1]
noff = [0,0,0,0,0,0,0]

def ligar_led (led, time):
    led.on()
    sleep(time)
    led.off()
    sleep(time)
    
def numbers (num):
    for i, seg7 in zip (pins, num):
        i.value(seg7)
    
while True:
    numbers(num0)
    sleep(20)